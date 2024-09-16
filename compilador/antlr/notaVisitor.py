# Generated from nota.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .notaParser import notaParser
else:
    from notaParser import notaParser

# This class defines a complete generic visitor for a parse tree produced by notaParser.

class notaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by notaParser#musica.
    def visitMusica(self, ctx:notaParser.MusicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#declaracoes.
    def visitDeclaracoes(self, ctx:notaParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#declaracao.
    def visitDeclaracao(self, ctx:notaParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#declaracao_acorde.
    def visitDeclaracao_acorde(self, ctx:notaParser.Declaracao_acordeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#acorde.
    def visitAcorde(self, ctx:notaParser.AcordeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#declaracao_frase.
    def visitDeclaracao_frase(self, ctx:notaParser.Declaracao_fraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#frase.
    def visitFrase(self, ctx:notaParser.FraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#evento.
    def visitEvento(self, ctx:notaParser.EventoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#evento_tempo.
    def visitEvento_tempo(self, ctx:notaParser.Evento_tempoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#acorde_ident.
    def visitAcorde_ident(self, ctx:notaParser.Acorde_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#frase_ident.
    def visitFrase_ident(self, ctx:notaParser.Frase_identContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#duracao.
    def visitDuracao(self, ctx:notaParser.DuracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by notaParser#execucao.
    def visitExecucao(self, ctx:notaParser.ExecucaoContext):
        return self.visitChildren(ctx)



del notaParser