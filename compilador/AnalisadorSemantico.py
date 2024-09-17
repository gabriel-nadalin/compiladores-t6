from antlr4 import ParserRuleContext as NoArvore
from antlr4 import TerminalNode
from antlr.notaParser import notaParser


class AnalisadorSemantico:
    def __init__(self) -> None:
        self.tabela_simbolos = {}
        self.erros = []

    def visitar_no(self, no: NoArvore):
        # print(type(no), no.getText())
        if isinstance(no, TerminalNode):
            return

        children = list(no.getChildren())
        match no:
            case notaParser.Declaracao_fraseContext():
                # 'frase' IDENT frase
                self.visitar_no(children[2])        # Visitando subnó da frase
                ident_txt = children[1].getText()
                linha = children[1].symbol.line
                if ident_txt in self.tabela_simbolos.keys():
                    self.erros.append(f"Erro na linha {linha}: O identificador de frase\'{ident_txt}\' já foi definido antes!")
                    return
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
                if ident_txt in self.tabela_simbolos.keys():
                    self.erros.append(f"Erro na linha {linha}: O identificador de acorde\'{ident_txt}\' já foi definido antes!")
                    return
                self.tabela_simbolos[ident_txt] = children[-1]
                
            case notaParser.AcordeContext():
                lista_notas = []
                for nota in children[1:-2]:     # Excluindo o primeiro e o último elementos ('{' e '}')
                    nome_nota = nota.getText()
                    if nome_nota in lista_notas:
                        linha = nota.symbol.line
                        self.erros.append(f"Erro na linha {linha}: A nota \'{nome_nota}\' foi definida multiplas vezes no mesmo acorde")        # TODO: pegar o nome do pai
                        return
                    lista_notas.append(nome_nota)
                
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

    def mostrar_erros(self):
        if len(self.erros) == 0:
            print('Não foi encontrado nenhum erro semântico no código!')
        else:
            print('Foram encontrados os seguintes erro semânticos no código:')
            for erro in self.erros:
                print('* ' + erro)