# Generated from projeto/compilador/antlr/nota.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,1,2,3,2,39,8,2,1,3,1,
        3,1,3,1,3,1,4,1,4,4,4,47,8,4,11,4,12,4,48,1,4,1,4,1,5,1,5,1,5,1,
        5,1,6,1,6,4,6,59,8,6,11,6,12,6,60,1,6,1,6,1,7,1,7,3,7,67,8,7,1,8,
        1,8,1,8,3,8,72,8,8,1,8,1,8,1,8,1,8,1,9,1,9,3,9,80,8,9,1,10,1,10,
        3,10,84,8,10,1,11,1,11,1,12,5,12,89,8,12,10,12,12,12,92,9,12,1,12,
        0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,90,0,26,1,0,0,0,2,33,
        1,0,0,0,4,38,1,0,0,0,6,40,1,0,0,0,8,44,1,0,0,0,10,52,1,0,0,0,12,
        56,1,0,0,0,14,66,1,0,0,0,16,71,1,0,0,0,18,79,1,0,0,0,20,83,1,0,0,
        0,22,85,1,0,0,0,24,90,1,0,0,0,26,27,3,2,1,0,27,28,3,24,12,0,28,29,
        5,0,0,1,29,1,1,0,0,0,30,32,3,4,2,0,31,30,1,0,0,0,32,35,1,0,0,0,33,
        31,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,33,1,0,0,0,36,39,3,6,3,
        0,37,39,3,10,5,0,38,36,1,0,0,0,38,37,1,0,0,0,39,5,1,0,0,0,40,41,
        5,1,0,0,41,42,5,10,0,0,42,43,3,8,4,0,43,7,1,0,0,0,44,46,5,2,0,0,
        45,47,5,9,0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,
        0,0,0,49,50,1,0,0,0,50,51,5,3,0,0,51,9,1,0,0,0,52,53,5,4,0,0,53,
        54,5,10,0,0,54,55,3,12,6,0,55,11,1,0,0,0,56,58,5,2,0,0,57,59,3,14,
        7,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,62,
        1,0,0,0,62,63,5,3,0,0,63,13,1,0,0,0,64,67,3,16,8,0,65,67,3,20,10,
        0,66,64,1,0,0,0,66,65,1,0,0,0,67,15,1,0,0,0,68,72,5,9,0,0,69,72,
        3,18,9,0,70,72,5,5,0,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,
        72,73,1,0,0,0,73,74,5,6,0,0,74,75,3,22,11,0,75,76,5,7,0,0,76,17,
        1,0,0,0,77,80,3,8,4,0,78,80,5,10,0,0,79,77,1,0,0,0,79,78,1,0,0,0,
        80,19,1,0,0,0,81,84,3,12,6,0,82,84,5,10,0,0,83,81,1,0,0,0,83,82,
        1,0,0,0,84,21,1,0,0,0,85,86,5,8,0,0,86,23,1,0,0,0,87,89,3,14,7,0,
        88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,25,1,
        0,0,0,92,90,1,0,0,0,9,33,38,48,60,66,71,79,83,90
    ]

class notaParser ( Parser ):

    grammarFileName = "nota.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'acorde'", "'{'", "'}'", "'frase'", "'pausa'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM_INT", "NOTA", "IDENT", "Comentario", "Whitespace" ]

    RULE_musica = 0
    RULE_declaracoes = 1
    RULE_declaracao = 2
    RULE_declaracao_acorde = 3
    RULE_acorde = 4
    RULE_declaracao_frase = 5
    RULE_frase = 6
    RULE_evento = 7
    RULE_evento_tempo = 8
    RULE_acorde_ident = 9
    RULE_frase_ident = 10
    RULE_duracao = 11
    RULE_execucao = 12

    ruleNames =  [ "musica", "declaracoes", "declaracao", "declaracao_acorde", 
                   "acorde", "declaracao_frase", "frase", "evento", "evento_tempo", 
                   "acorde_ident", "frase_ident", "duracao", "execucao" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUM_INT=8
    NOTA=9
    IDENT=10
    Comentario=11
    Whitespace=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MusicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracoes(self):
            return self.getTypedRuleContext(notaParser.DeclaracoesContext,0)


        def execucao(self):
            return self.getTypedRuleContext(notaParser.ExecucaoContext,0)


        def EOF(self):
            return self.getToken(notaParser.EOF, 0)

        def getRuleIndex(self):
            return notaParser.RULE_musica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMusica" ):
                listener.enterMusica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMusica" ):
                listener.exitMusica(self)




    def musica(self):

        localctx = notaParser.MusicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_musica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.declaracoes()
            self.state = 27
            self.execucao()
            self.state = 28
            self.match(notaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(notaParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(notaParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return notaParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)




    def declaracoes(self):

        localctx = notaParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==4:
                self.state = 30
                self.declaracao()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_acorde(self):
            return self.getTypedRuleContext(notaParser.Declaracao_acordeContext,0)


        def declaracao_frase(self):
            return self.getTypedRuleContext(notaParser.Declaracao_fraseContext,0)


        def getRuleIndex(self):
            return notaParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)




    def declaracao(self):

        localctx = notaParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.declaracao_acorde()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.declaracao_frase()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_acordeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(notaParser.IDENT, 0)

        def acorde(self):
            return self.getTypedRuleContext(notaParser.AcordeContext,0)


        def getRuleIndex(self):
            return notaParser.RULE_declaracao_acorde

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_acorde" ):
                listener.enterDeclaracao_acorde(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_acorde" ):
                listener.exitDeclaracao_acorde(self)




    def declaracao_acorde(self):

        localctx = notaParser.Declaracao_acordeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao_acorde)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(notaParser.T__0)
            self.state = 41
            self.match(notaParser.IDENT)
            self.state = 42
            self.acorde()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcordeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTA(self, i:int=None):
            if i is None:
                return self.getTokens(notaParser.NOTA)
            else:
                return self.getToken(notaParser.NOTA, i)

        def getRuleIndex(self):
            return notaParser.RULE_acorde

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcorde" ):
                listener.enterAcorde(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcorde" ):
                listener.exitAcorde(self)




    def acorde(self):

        localctx = notaParser.AcordeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_acorde)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(notaParser.T__1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.match(notaParser.NOTA)
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

            self.state = 50
            self.match(notaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_fraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(notaParser.IDENT, 0)

        def frase(self):
            return self.getTypedRuleContext(notaParser.FraseContext,0)


        def getRuleIndex(self):
            return notaParser.RULE_declaracao_frase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_frase" ):
                listener.enterDeclaracao_frase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_frase" ):
                listener.exitDeclaracao_frase(self)




    def declaracao_frase(self):

        localctx = notaParser.Declaracao_fraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracao_frase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(notaParser.T__3)
            self.state = 53
            self.match(notaParser.IDENT)
            self.state = 54
            self.frase()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(notaParser.EventoContext)
            else:
                return self.getTypedRuleContext(notaParser.EventoContext,i)


        def getRuleIndex(self):
            return notaParser.RULE_frase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrase" ):
                listener.enterFrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrase" ):
                listener.exitFrase(self)




    def frase(self):

        localctx = notaParser.FraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_frase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(notaParser.T__1)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.evento()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1572) != 0)):
                    break

            self.state = 62
            self.match(notaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evento_tempo(self):
            return self.getTypedRuleContext(notaParser.Evento_tempoContext,0)


        def frase_ident(self):
            return self.getTypedRuleContext(notaParser.Frase_identContext,0)


        def getRuleIndex(self):
            return notaParser.RULE_evento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvento" ):
                listener.enterEvento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvento" ):
                listener.exitEvento(self)




    def evento(self):

        localctx = notaParser.EventoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_evento)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.evento_tempo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.frase_ident()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Evento_tempoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def duracao(self):
            return self.getTypedRuleContext(notaParser.DuracaoContext,0)


        def NOTA(self):
            return self.getToken(notaParser.NOTA, 0)

        def acorde_ident(self):
            return self.getTypedRuleContext(notaParser.Acorde_identContext,0)


        def getRuleIndex(self):
            return notaParser.RULE_evento_tempo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvento_tempo" ):
                listener.enterEvento_tempo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvento_tempo" ):
                listener.exitEvento_tempo(self)




    def evento_tempo(self):

        localctx = notaParser.Evento_tempoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_evento_tempo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 68
                self.match(notaParser.NOTA)
                pass
            elif token in [2, 10]:
                self.state = 69
                self.acorde_ident()
                pass
            elif token in [5]:
                self.state = 70
                self.match(notaParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 73
            self.match(notaParser.T__5)
            self.state = 74
            self.duracao()
            self.state = 75
            self.match(notaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Acorde_identContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def acorde(self):
            return self.getTypedRuleContext(notaParser.AcordeContext,0)


        def IDENT(self):
            return self.getToken(notaParser.IDENT, 0)

        def getRuleIndex(self):
            return notaParser.RULE_acorde_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcorde_ident" ):
                listener.enterAcorde_ident(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcorde_ident" ):
                listener.exitAcorde_ident(self)




    def acorde_ident(self):

        localctx = notaParser.Acorde_identContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_acorde_ident)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.acorde()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(notaParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Frase_identContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def frase(self):
            return self.getTypedRuleContext(notaParser.FraseContext,0)


        def IDENT(self):
            return self.getToken(notaParser.IDENT, 0)

        def getRuleIndex(self):
            return notaParser.RULE_frase_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrase_ident" ):
                listener.enterFrase_ident(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrase_ident" ):
                listener.exitFrase_ident(self)




    def frase_ident(self):

        localctx = notaParser.Frase_identContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_frase_ident)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.frase()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(notaParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DuracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(notaParser.NUM_INT, 0)

        def getRuleIndex(self):
            return notaParser.RULE_duracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDuracao" ):
                listener.enterDuracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDuracao" ):
                listener.exitDuracao(self)




    def duracao(self):

        localctx = notaParser.DuracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_duracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(notaParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecucaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(notaParser.EventoContext)
            else:
                return self.getTypedRuleContext(notaParser.EventoContext,i)


        def getRuleIndex(self):
            return notaParser.RULE_execucao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecucao" ):
                listener.enterExecucao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecucao" ):
                listener.exitExecucao(self)




    def execucao(self):

        localctx = notaParser.ExecucaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_execucao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1572) != 0):
                self.state = 87
                self.evento()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





