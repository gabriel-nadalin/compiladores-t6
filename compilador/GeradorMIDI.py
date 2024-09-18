from antlr4 import ParserRuleContext as NoArvore
from antlr4 import TerminalNode
from mido import Message, MidiFile, MidiTrack, second2tick
from compilador.antlr.notaParser import notaParser


class GeradorMIDI:
    def __init__(self) -> None:
        self.tabela_simbolos = {}
        # self.eventos = []
        # self.traducao_notas {'A'}
        self.pausa_offset = 0
        self.arquivo = MidiFile()
        self.trilha = MidiTrack()
        self.arquivo.tracks.append(self.trilha)
        

    @classmethod
    def note_to_midi(cls, note : str)->int:
    # Pitch class dictionary
        pitch_classes = {
            'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
            'E': 4, 'E#': 5, 'Fb': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8,
            'A': 9, 'A#': 10, 'Bb': 10, 'B': 11, 'B#': 0, 'Cb': 11, 
        }

        # Extract the note and octave from input
        if len(note) == 2:  # e.g. A4, C3
            pitch, octave = note[0], int(note[1])
        else:  # e.g. Bb2, C#5
            pitch, octave = note[:2], int(note[2])

        # Calculate the MIDI note number
        midi_note = (octave + 1) * 12 + pitch_classes[pitch]
        
        return midi_note

    def start_nota(self, nota : str, pausa_offset : int):
        nota_midi = GeradorMIDI.note_to_midi(nota)
        self.trilha.append(Message('note_on', note=nota_midi, time=1000 + pausa_offset))
    
    def stop_nota(self, nota : str, duracao : int):
        nota_midi = GeradorMIDI.note_to_midi(nota)
        self.trilha.append(Message('note_off', note=nota_midi, time=duracao))


    def get_notas_acorde_ident(self, acorde_ident : notaParser.Acorde_identContext):
        child = acorde_ident.getChild(0)
        if isinstance(child, notaParser.AcordeContext):
            lista_notas = []
            for nota in list(child.getChildren())[1:-1]:     # Excluindo o primeiro e o último elementos ('{' e '}')
                lista_notas.append(nota.getText())
            return lista_notas
        return self.tabela_simbolos[child.getText()]

    def visitar_no(self, no: NoArvore):
        if isinstance(no, TerminalNode):
            return

        children = list(no.getChildren())
        match no:
            case notaParser.Evento_tempoContext():
            # (NOTA | acorde_ident | 'pausa') '(' duracao ')';
                child = children[0]
                notas_para_tocar = []
                duracao = second2tick(int(children[2].getText()) / 1000, 480, 500_000)
                if isinstance(child, TerminalNode):
                    print(duracao)

                    if child.getText() == 'pausa':
                        self.pausa_offset += duracao
                        # self.pausa_offset += duracao
                        return
                    notas_para_tocar.append(child.getText())
                    print(self.arquivo)
                else:
                    notas_para_tocar = self.get_notas_acorde_ident(child)
                for nota in notas_para_tocar:
                    self.start_nota(nota, self.pausa_offset)

                for nota in notas_para_tocar:
                    self.stop_nota(nota, duracao)
                
                # self.visitar_no(child)
                # self.pausa_offset += duracao


            case notaParser.Declaracao_fraseContext():
                # 'frase' IDENT frase
                self.visitar_no(children[2])        # Visitando subnó da frase
                self.tabela_simbolos[ident_txt] = children[-1]

            case notaParser.FraseContext():
                # '{' ( '{' N O T A S '}' | ident | 'pausa' ) '(' INT ')' '}'
                for evento in children[1:-2]:     # Excluindo o primeiro e os últimos elementos '{', '}'
                    self.visitar_no(evento)

            case notaParser.Declaracao_acordeContext():
                # 'acorde' IDENT acorde
                self.visitar_no(children[2])        # Visitando subnó do acorde

                ident_txt = children[1].getText()
                linha = children[1].symbol.line
                self.tabela_simbolos[ident_txt] = children[-1]
                
            # case notaParser.AcordeContext():
            #     lista_notas = []
            #     for nota in children[1:-2]:     # Excluindo o primeiro e o último elementos ('{' e '}')
            #         nome_nota = nota.getText()
            #         nota_midi = GeradorMIDI.note_to_midi(child.getText())
            #         self.trilha.append(Message('note_on', note=nota_midi, time=self.pausa_offset))
            #         self.trilha.append(Message('note_off', note=nota_midi, time=duracao))
            #         self.pausa_offset = 0
            #         print(self.arquivo)
                
            case notaParser.Acorde_identContext():
                child = children[0]         # Somente filho único do nó atual
                # Caso seja identificador mesmo
                if isinstance(child, TerminalNode):
                    linha = child.symbol.line

                    if child.getText() not in self.tabela_simbolos.keys():
                        self.erros.append(f"Erro na linha {linha}: O identificado \'{no.getText()}\' foi usado sem ser definido antes")
                        return
                    if not isinstance(self.tabela_simbolos[child.getText()], notaParser.AcordeContext):
                        self.erros.append(f"Erro na linha {linha}: O identificado \'{no.getText()}\' foi definidido como \'frase\' e está sendo chamado como um \'acorde\'")
                        return
                # Caso seja um acorde ou uma frase
                self.visitar_no(child)

            case notaParser.Frase_identContext():
                child = children[0]         # Somente filho único do nó atual
                # Caso seja identificador mesmo
                if isinstance(child, TerminalNode):
                    linha = child.symbol.line
                    if child.getText() not in self.tabela_simbolos.keys():
                        self.erros.append(f"Erro na linha {linha}: O identificado \'{no.getText()}\' foi usado sem ser definido antes")
                        return
                    if not isinstance(self.tabela_simbolos[child.getText()], notaParser.FraseContext):
                        self.erros.append(f"Erro na linha {linha}: O identificado \'{no.getText()}\' foi definidido como \'acorde\' e está sendo chamado como um \'frase\'")
                        return
                
                # Caso seja um acorde ou uma frase
                self.visitar_no(child)

            case _:
                for child in children:
                    self.visitar_no(child)

