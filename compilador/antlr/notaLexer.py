# Generated from nota.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,93,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,4,7,54,8,7,11,7,12,7,55,1,8,1,
        8,3,8,60,8,8,1,8,1,8,1,9,1,9,5,9,66,8,9,10,9,12,9,69,9,9,1,10,1,
        10,1,10,1,10,5,10,75,8,10,10,10,12,10,78,9,10,1,10,3,10,81,8,10,
        1,10,1,10,1,10,1,10,1,11,4,11,88,8,11,11,11,12,11,89,1,11,1,11,0,
        0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,
        0,7,1,0,48,57,1,0,65,71,2,0,35,35,98,98,2,0,65,90,97,122,4,0,48,
        57,65,90,95,95,97,122,2,0,10,10,13,13,3,0,9,10,13,13,32,32,98,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,32,1,0,0,0,5,34,1,0,0,0,7,36,1,
        0,0,0,9,42,1,0,0,0,11,48,1,0,0,0,13,50,1,0,0,0,15,53,1,0,0,0,17,
        57,1,0,0,0,19,63,1,0,0,0,21,70,1,0,0,0,23,87,1,0,0,0,25,26,5,97,
        0,0,26,27,5,99,0,0,27,28,5,111,0,0,28,29,5,114,0,0,29,30,5,100,0,
        0,30,31,5,101,0,0,31,2,1,0,0,0,32,33,5,123,0,0,33,4,1,0,0,0,34,35,
        5,125,0,0,35,6,1,0,0,0,36,37,5,102,0,0,37,38,5,114,0,0,38,39,5,97,
        0,0,39,40,5,115,0,0,40,41,5,101,0,0,41,8,1,0,0,0,42,43,5,112,0,0,
        43,44,5,97,0,0,44,45,5,117,0,0,45,46,5,115,0,0,46,47,5,97,0,0,47,
        10,1,0,0,0,48,49,5,40,0,0,49,12,1,0,0,0,50,51,5,41,0,0,51,14,1,0,
        0,0,52,54,7,0,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,16,1,0,0,0,57,59,7,1,0,0,58,60,7,2,0,0,59,58,1,0,0,0,
        59,60,1,0,0,0,60,61,1,0,0,0,61,62,7,0,0,0,62,18,1,0,0,0,63,67,7,
        3,0,0,64,66,7,4,0,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,
        68,1,0,0,0,68,20,1,0,0,0,69,67,1,0,0,0,70,71,5,47,0,0,71,72,5,47,
        0,0,72,76,1,0,0,0,73,75,8,5,0,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,
        1,0,0,0,76,77,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,79,81,5,13,0,0,
        80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,10,0,0,83,84,1,
        0,0,0,84,85,6,10,0,0,85,22,1,0,0,0,86,88,7,6,0,0,87,86,1,0,0,0,88,
        89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,6,11,
        0,0,92,24,1,0,0,0,7,0,55,59,67,76,80,89,1,6,0,0
    ]

class notaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    NUM_INT = 8
    NOTA = 9
    IDENT = 10
    Comentario = 11
    Whitespace = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'acorde'", "'{'", "'}'", "'frase'", "'pausa'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUM_INT", "NOTA", "IDENT", "Comentario", "Whitespace" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "NUM_INT", "NOTA", "IDENT", "Comentario", "Whitespace" ]

    grammarFileName = "nota.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


