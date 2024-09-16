from antlr4 import *
from antlr.notaListener import notaListener
from antlr.notaParser import notaParser
from antlr.notaLexer import notaLexer
from Vocabulario import Vocabulario

class VisitadorArvore(notaListener):
    def __init__(self, context : notaParser.MusicaContext, lexer : notaLexer, out : any) -> None:
        self.vocabulario = Vocabulario('./antlr/nota.tokens')
        self.context = context
        