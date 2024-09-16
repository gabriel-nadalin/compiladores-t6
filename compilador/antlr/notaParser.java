// Generated from ./projeto/compilador/antlr/nota.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class notaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, NUM_INT=8, NOTA=9, 
		IDENT=10, Comentario=11, Whitespace=12;
	public static final int
		RULE_musica = 0, RULE_declaracoes = 1, RULE_declaracao = 2, RULE_declaracao_acorde = 3, 
		RULE_acorde = 4, RULE_declaracao_frase = 5, RULE_frase = 6, RULE_evento = 7, 
		RULE_evento_tempo = 8, RULE_acorde_ident = 9, RULE_frase_ident = 10, RULE_duracao = 11, 
		RULE_execucao = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"musica", "declaracoes", "declaracao", "declaracao_acorde", "acorde", 
			"declaracao_frase", "frase", "evento", "evento_tempo", "acorde_ident", 
			"frase_ident", "duracao", "execucao"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'acorde'", "'{'", "'}'", "'frase'", "'pausa'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "NUM_INT", "NOTA", "IDENT", 
			"Comentario", "Whitespace"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "nota.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public notaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MusicaContext extends ParserRuleContext {
		public DeclaracoesContext declaracoes() {
			return getRuleContext(DeclaracoesContext.class,0);
		}
		public ExecucaoContext execucao() {
			return getRuleContext(ExecucaoContext.class,0);
		}
		public TerminalNode EOF() { return getToken(notaParser.EOF, 0); }
		public MusicaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_musica; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterMusica(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitMusica(this);
		}
	}

	public final MusicaContext musica() throws RecognitionException {
		MusicaContext _localctx = new MusicaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_musica);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			declaracoes();
			setState(27);
			execucao();
			setState(28);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracoesContext extends ParserRuleContext {
		public List<DeclaracaoContext> declaracao() {
			return getRuleContexts(DeclaracaoContext.class);
		}
		public DeclaracaoContext declaracao(int i) {
			return getRuleContext(DeclaracaoContext.class,i);
		}
		public DeclaracoesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracoes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterDeclaracoes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitDeclaracoes(this);
		}
	}

	public final DeclaracoesContext declaracoes() throws RecognitionException {
		DeclaracoesContext _localctx = new DeclaracoesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaracoes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==T__3) {
				{
				{
				setState(30);
				declaracao();
				}
				}
				setState(35);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracaoContext extends ParserRuleContext {
		public Declaracao_acordeContext declaracao_acorde() {
			return getRuleContext(Declaracao_acordeContext.class,0);
		}
		public Declaracao_fraseContext declaracao_frase() {
			return getRuleContext(Declaracao_fraseContext.class,0);
		}
		public DeclaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterDeclaracao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitDeclaracao(this);
		}
	}

	public final DeclaracaoContext declaracao() throws RecognitionException {
		DeclaracaoContext _localctx = new DeclaracaoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracao);
		try {
			setState(38);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				declaracao_acorde();
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 2);
				{
				setState(37);
				declaracao_frase();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Declaracao_acordeContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(notaParser.IDENT, 0); }
		public AcordeContext acorde() {
			return getRuleContext(AcordeContext.class,0);
		}
		public Declaracao_acordeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao_acorde; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterDeclaracao_acorde(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitDeclaracao_acorde(this);
		}
	}

	public final Declaracao_acordeContext declaracao_acorde() throws RecognitionException {
		Declaracao_acordeContext _localctx = new Declaracao_acordeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaracao_acorde);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			match(T__0);
			setState(41);
			match(IDENT);
			setState(42);
			acorde();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AcordeContext extends ParserRuleContext {
		public List<TerminalNode> NOTA() { return getTokens(notaParser.NOTA); }
		public TerminalNode NOTA(int i) {
			return getToken(notaParser.NOTA, i);
		}
		public AcordeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_acorde; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterAcorde(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitAcorde(this);
		}
	}

	public final AcordeContext acorde() throws RecognitionException {
		AcordeContext _localctx = new AcordeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_acorde);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__1);
			setState(46); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(45);
				match(NOTA);
				}
				}
				setState(48); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NOTA );
			setState(50);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Declaracao_fraseContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(notaParser.IDENT, 0); }
		public FraseContext frase() {
			return getRuleContext(FraseContext.class,0);
		}
		public Declaracao_fraseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao_frase; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterDeclaracao_frase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitDeclaracao_frase(this);
		}
	}

	public final Declaracao_fraseContext declaracao_frase() throws RecognitionException {
		Declaracao_fraseContext _localctx = new Declaracao_fraseContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_declaracao_frase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			match(T__3);
			setState(53);
			match(IDENT);
			setState(54);
			frase();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FraseContext extends ParserRuleContext {
		public List<EventoContext> evento() {
			return getRuleContexts(EventoContext.class);
		}
		public EventoContext evento(int i) {
			return getRuleContext(EventoContext.class,i);
		}
		public FraseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_frase; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterFrase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitFrase(this);
		}
	}

	public final FraseContext frase() throws RecognitionException {
		FraseContext _localctx = new FraseContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_frase);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(T__1);
			setState(58); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(57);
				evento();
				}
				}
				setState(60); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1572L) != 0) );
			setState(62);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EventoContext extends ParserRuleContext {
		public Evento_tempoContext evento_tempo() {
			return getRuleContext(Evento_tempoContext.class,0);
		}
		public Frase_identContext frase_ident() {
			return getRuleContext(Frase_identContext.class,0);
		}
		public EventoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_evento; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterEvento(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitEvento(this);
		}
	}

	public final EventoContext evento() throws RecognitionException {
		EventoContext _localctx = new EventoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_evento);
		try {
			setState(66);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				evento_tempo();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(65);
				frase_ident();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Evento_tempoContext extends ParserRuleContext {
		public DuracaoContext duracao() {
			return getRuleContext(DuracaoContext.class,0);
		}
		public TerminalNode NOTA() { return getToken(notaParser.NOTA, 0); }
		public Acorde_identContext acorde_ident() {
			return getRuleContext(Acorde_identContext.class,0);
		}
		public Evento_tempoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_evento_tempo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterEvento_tempo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitEvento_tempo(this);
		}
	}

	public final Evento_tempoContext evento_tempo() throws RecognitionException {
		Evento_tempoContext _localctx = new Evento_tempoContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_evento_tempo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOTA:
				{
				setState(68);
				match(NOTA);
				}
				break;
			case T__1:
			case IDENT:
				{
				setState(69);
				acorde_ident();
				}
				break;
			case T__4:
				{
				setState(70);
				match(T__4);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(73);
			match(T__5);
			setState(74);
			duracao();
			setState(75);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Acorde_identContext extends ParserRuleContext {
		public AcordeContext acorde() {
			return getRuleContext(AcordeContext.class,0);
		}
		public TerminalNode IDENT() { return getToken(notaParser.IDENT, 0); }
		public Acorde_identContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_acorde_ident; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterAcorde_ident(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitAcorde_ident(this);
		}
	}

	public final Acorde_identContext acorde_ident() throws RecognitionException {
		Acorde_identContext _localctx = new Acorde_identContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_acorde_ident);
		try {
			setState(79);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				acorde();
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				match(IDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Frase_identContext extends ParserRuleContext {
		public FraseContext frase() {
			return getRuleContext(FraseContext.class,0);
		}
		public TerminalNode IDENT() { return getToken(notaParser.IDENT, 0); }
		public Frase_identContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_frase_ident; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterFrase_ident(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitFrase_ident(this);
		}
	}

	public final Frase_identContext frase_ident() throws RecognitionException {
		Frase_identContext _localctx = new Frase_identContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_frase_ident);
		try {
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				frase();
				}
				break;
			case IDENT:
				enterOuterAlt(_localctx, 2);
				{
				setState(82);
				match(IDENT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DuracaoContext extends ParserRuleContext {
		public TerminalNode NUM_INT() { return getToken(notaParser.NUM_INT, 0); }
		public DuracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_duracao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterDuracao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitDuracao(this);
		}
	}

	public final DuracaoContext duracao() throws RecognitionException {
		DuracaoContext _localctx = new DuracaoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_duracao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(NUM_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExecucaoContext extends ParserRuleContext {
		public List<EventoContext> evento() {
			return getRuleContexts(EventoContext.class);
		}
		public EventoContext evento(int i) {
			return getRuleContext(EventoContext.class,i);
		}
		public ExecucaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_execucao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).enterExecucao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof notaListener ) ((notaListener)listener).exitExecucao(this);
		}
	}

	public final ExecucaoContext execucao() throws RecognitionException {
		ExecucaoContext _localctx = new ExecucaoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_execucao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1572L) != 0)) {
				{
				{
				setState(87);
				evento();
				}
				}
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\f^\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0005\u0001 \b\u0001\n\u0001\f\u0001#\t\u0001\u0001\u0002\u0001\u0002"+
		"\u0003\u0002\'\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0004\u0004/\b\u0004\u000b\u0004\f\u00040\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0004\u0006;\b\u0006\u000b\u0006\f\u0006<\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0003\u0007C\b\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0003\bH\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0003\tP\b\t\u0001\n\u0001\n\u0003\nT\b\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0005\fY\b\f\n\f\f\f\\\t\f\u0001\f\u0000\u0000\r\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0000Z\u0000\u001a"+
		"\u0001\u0000\u0000\u0000\u0002!\u0001\u0000\u0000\u0000\u0004&\u0001\u0000"+
		"\u0000\u0000\u0006(\u0001\u0000\u0000\u0000\b,\u0001\u0000\u0000\u0000"+
		"\n4\u0001\u0000\u0000\u0000\f8\u0001\u0000\u0000\u0000\u000eB\u0001\u0000"+
		"\u0000\u0000\u0010G\u0001\u0000\u0000\u0000\u0012O\u0001\u0000\u0000\u0000"+
		"\u0014S\u0001\u0000\u0000\u0000\u0016U\u0001\u0000\u0000\u0000\u0018Z"+
		"\u0001\u0000\u0000\u0000\u001a\u001b\u0003\u0002\u0001\u0000\u001b\u001c"+
		"\u0003\u0018\f\u0000\u001c\u001d\u0005\u0000\u0000\u0001\u001d\u0001\u0001"+
		"\u0000\u0000\u0000\u001e \u0003\u0004\u0002\u0000\u001f\u001e\u0001\u0000"+
		"\u0000\u0000 #\u0001\u0000\u0000\u0000!\u001f\u0001\u0000\u0000\u0000"+
		"!\"\u0001\u0000\u0000\u0000\"\u0003\u0001\u0000\u0000\u0000#!\u0001\u0000"+
		"\u0000\u0000$\'\u0003\u0006\u0003\u0000%\'\u0003\n\u0005\u0000&$\u0001"+
		"\u0000\u0000\u0000&%\u0001\u0000\u0000\u0000\'\u0005\u0001\u0000\u0000"+
		"\u0000()\u0005\u0001\u0000\u0000)*\u0005\n\u0000\u0000*+\u0003\b\u0004"+
		"\u0000+\u0007\u0001\u0000\u0000\u0000,.\u0005\u0002\u0000\u0000-/\u0005"+
		"\t\u0000\u0000.-\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000\u00000.\u0001"+
		"\u0000\u0000\u000001\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u0000"+
		"23\u0005\u0003\u0000\u00003\t\u0001\u0000\u0000\u000045\u0005\u0004\u0000"+
		"\u000056\u0005\n\u0000\u000067\u0003\f\u0006\u00007\u000b\u0001\u0000"+
		"\u0000\u00008:\u0005\u0002\u0000\u00009;\u0003\u000e\u0007\u0000:9\u0001"+
		"\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000"+
		"<=\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000>?\u0005\u0003\u0000"+
		"\u0000?\r\u0001\u0000\u0000\u0000@C\u0003\u0010\b\u0000AC\u0003\u0014"+
		"\n\u0000B@\u0001\u0000\u0000\u0000BA\u0001\u0000\u0000\u0000C\u000f\u0001"+
		"\u0000\u0000\u0000DH\u0005\t\u0000\u0000EH\u0003\u0012\t\u0000FH\u0005"+
		"\u0005\u0000\u0000GD\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000"+
		"GF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IJ\u0005\u0006\u0000"+
		"\u0000JK\u0003\u0016\u000b\u0000KL\u0005\u0007\u0000\u0000L\u0011\u0001"+
		"\u0000\u0000\u0000MP\u0003\b\u0004\u0000NP\u0005\n\u0000\u0000OM\u0001"+
		"\u0000\u0000\u0000ON\u0001\u0000\u0000\u0000P\u0013\u0001\u0000\u0000"+
		"\u0000QT\u0003\f\u0006\u0000RT\u0005\n\u0000\u0000SQ\u0001\u0000\u0000"+
		"\u0000SR\u0001\u0000\u0000\u0000T\u0015\u0001\u0000\u0000\u0000UV\u0005"+
		"\b\u0000\u0000V\u0017\u0001\u0000\u0000\u0000WY\u0003\u000e\u0007\u0000"+
		"XW\u0001\u0000\u0000\u0000Y\\\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000"+
		"\u0000Z[\u0001\u0000\u0000\u0000[\u0019\u0001\u0000\u0000\u0000\\Z\u0001"+
		"\u0000\u0000\u0000\t!&0<BGOSZ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}