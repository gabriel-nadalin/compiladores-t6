# Generated from nota.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .notaParser import notaParser
else:
    from notaParser import notaParser

# This class defines a complete listener for a parse tree produced by notaParser.
class notaListener(ParseTreeListener):

    # Enter a parse tree produced by notaParser#musica.
    def enterMusica(self, ctx:notaParser.MusicaContext):
        pass

    # Exit a parse tree produced by notaParser#musica.
    def exitMusica(self, ctx:notaParser.MusicaContext):
        pass


    # Enter a parse tree produced by notaParser#declaracoes.
    def enterDeclaracoes(self, ctx:notaParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by notaParser#declaracoes.
    def exitDeclaracoes(self, ctx:notaParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by notaParser#declaracao.
    def enterDeclaracao(self, ctx:notaParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by notaParser#declaracao.
    def exitDeclaracao(self, ctx:notaParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by notaParser#declaracao_acorde.
    def enterDeclaracao_acorde(self, ctx:notaParser.Declaracao_acordeContext):
        pass

    # Exit a parse tree produced by notaParser#declaracao_acorde.
    def exitDeclaracao_acorde(self, ctx:notaParser.Declaracao_acordeContext):
        pass


    # Enter a parse tree produced by notaParser#acorde.
    def enterAcorde(self, ctx:notaParser.AcordeContext):
        pass

    # Exit a parse tree produced by notaParser#acorde.
    def exitAcorde(self, ctx:notaParser.AcordeContext):
        pass


    # Enter a parse tree produced by notaParser#declaracao_frase.
    def enterDeclaracao_frase(self, ctx:notaParser.Declaracao_fraseContext):
        pass

    # Exit a parse tree produced by notaParser#declaracao_frase.
    def exitDeclaracao_frase(self, ctx:notaParser.Declaracao_fraseContext):
        pass


    # Enter a parse tree produced by notaParser#frase.
    def enterFrase(self, ctx:notaParser.FraseContext):
        pass

    # Exit a parse tree produced by notaParser#frase.
    def exitFrase(self, ctx:notaParser.FraseContext):
        pass


    # Enter a parse tree produced by notaParser#evento.
    def enterEvento(self, ctx:notaParser.EventoContext):
        pass

    # Exit a parse tree produced by notaParser#evento.
    def exitEvento(self, ctx:notaParser.EventoContext):
        pass


    # Enter a parse tree produced by notaParser#evento_tempo.
    def enterEvento_tempo(self, ctx:notaParser.Evento_tempoContext):
        pass

    # Exit a parse tree produced by notaParser#evento_tempo.
    def exitEvento_tempo(self, ctx:notaParser.Evento_tempoContext):
        pass


    # Enter a parse tree produced by notaParser#acorde_ident.
    def enterAcorde_ident(self, ctx:notaParser.Acorde_identContext):
        pass

    # Exit a parse tree produced by notaParser#acorde_ident.
    def exitAcorde_ident(self, ctx:notaParser.Acorde_identContext):
        pass


    # Enter a parse tree produced by notaParser#frase_ident.
    def enterFrase_ident(self, ctx:notaParser.Frase_identContext):
        pass

    # Exit a parse tree produced by notaParser#frase_ident.
    def exitFrase_ident(self, ctx:notaParser.Frase_identContext):
        pass


    # Enter a parse tree produced by notaParser#duracao.
    def enterDuracao(self, ctx:notaParser.DuracaoContext):
        pass

    # Exit a parse tree produced by notaParser#duracao.
    def exitDuracao(self, ctx:notaParser.DuracaoContext):
        pass


    # Enter a parse tree produced by notaParser#execucao.
    def enterExecucao(self, ctx:notaParser.ExecucaoContext):
        pass

    # Exit a parse tree produced by notaParser#execucao.
    def exitExecucao(self, ctx:notaParser.ExecucaoContext):
        pass



del notaParser