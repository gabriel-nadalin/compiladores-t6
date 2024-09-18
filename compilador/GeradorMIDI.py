from antlr4 import ParserRuleContext as NoArvore
from antlr4 import TerminalNode
from mido import Message, MidiFile, MidiTrack, second2tick
from compilador.antlr.notaParser import notaParser


class GeradorMIDI:
    def __init__(self) -> None:
        self.tabela_simbolos = {}
        # self.eventos = []
        # self.traducao_notas {'A'}
        self.tempo = 0
        self.arquivo = MidiFile()
        self.trilha = MidiTrack()
        self.arquivo.tracks.append(self.trilha)
        

    @classmethod
    def note2midi(cls, note : str)->int:
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

    def visitar_no(self, no: NoArvore):
        if isinstance(no, TerminalNode):
            return

        children = list(no.getChildren())
        match no:
            case notaParser.Evento_tempoContext():
            # (NOTA | acorde_ident | 'pausa') '(' duracao ')';
                evento = children[0]
                duracao = second2tick(int(children[2].getText()) / 1000, 480, 500_000)

                if isinstance(evento, TerminalNode):
                    if evento.getText() == 'pausa':
                        self.tempo += duracao
                        return
                    
                    nota_midi = GeradorMIDI.note2midi(evento.getText())
                    self.trilha.append(Message('note_on', note=nota_midi, time=self.tempo))
                    self.trilha.append(Message('note_off', note=nota_midi, time=duracao))
                    self.tempo = 0
                    return
                
                acorde = evento.children[0]
                if isinstance(acorde, TerminalNode):
                    # recupera notas de um acorde da tabela de simbolos
                    notas = self.tabela_simbolos[acorde.getText()].NOTA()
                else:
                    # recupera notas de um acorde declarado inline
                    notas = acorde.NOTA()

                for nota in notas:
                    nota_midi = GeradorMIDI.note2midi(nota.getText())
                    self.trilha.append(Message('note_on', note=nota_midi, time=self.tempo))
                    self.tempo = 0

                for nota in notas:
                    nota_midi = GeradorMIDI.note2midi(nota.getText())
                    self.trilha.append(Message('note_off', note=nota_midi, time=duracao))
                    duracao = 0

            case notaParser.Declaracao_fraseContext():
                # 'frase' IDENT frase
                ident_txt = children[1].getText()
                self.tabela_simbolos[ident_txt] = children[-1]

            case notaParser.Declaracao_acordeContext():
                # 'acorde' IDENT acorde
                ident_txt = children[1].getText()
                self.tabela_simbolos[ident_txt] = children[-1]

            case notaParser.Frase_identContext():
                frase = children[0]         # Somente filho único do nó atual
                # Caso seja identificador mesmo
                if isinstance(frase, TerminalNode):
                    frase = self.tabela_simbolos[frase.getText()]
                
                self.visitar_no(frase)

            case _:
                for child in children:
                    self.visitar_no(child)
