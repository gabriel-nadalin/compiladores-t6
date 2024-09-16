// Generated from ./projeto/compilador/antlr/nota.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class notaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, NUM_INT=8, NOTA=9, 
		IDENT=10, Comentario=11, Whitespace=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "NUM_INT", "NOTA", 
			"IDENT", "Comentario", "Whitespace"
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


	public notaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "nota.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\f]\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0004\u0007"+
		"6\b\u0007\u000b\u0007\f\u00077\u0001\b\u0001\b\u0003\b<\b\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0005\tB\b\t\n\t\f\tE\t\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0005\nK\b\n\n\n\f\nN\t\n\u0001\n\u0003\nQ\b\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0004\u000bX\b\u000b\u000b\u000b\f\u000bY\u0001"+
		"\u000b\u0001\u000b\u0000\u0000\f\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0001\u0000\u0007\u0001\u000009\u0001\u0000AG\u0002\u0000##b"+
		"b\u0002\u0000AZaz\u0004\u000009AZ__az\u0002\u0000\n\n\r\r\u0003\u0000"+
		"\t\n\r\r  b\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0001\u0019\u0001\u0000\u0000\u0000\u0003 \u0001\u0000\u0000\u0000\u0005"+
		"\"\u0001\u0000\u0000\u0000\u0007$\u0001\u0000\u0000\u0000\t*\u0001\u0000"+
		"\u0000\u0000\u000b0\u0001\u0000\u0000\u0000\r2\u0001\u0000\u0000\u0000"+
		"\u000f5\u0001\u0000\u0000\u0000\u00119\u0001\u0000\u0000\u0000\u0013?"+
		"\u0001\u0000\u0000\u0000\u0015F\u0001\u0000\u0000\u0000\u0017W\u0001\u0000"+
		"\u0000\u0000\u0019\u001a\u0005a\u0000\u0000\u001a\u001b\u0005c\u0000\u0000"+
		"\u001b\u001c\u0005o\u0000\u0000\u001c\u001d\u0005r\u0000\u0000\u001d\u001e"+
		"\u0005d\u0000\u0000\u001e\u001f\u0005e\u0000\u0000\u001f\u0002\u0001\u0000"+
		"\u0000\u0000 !\u0005{\u0000\u0000!\u0004\u0001\u0000\u0000\u0000\"#\u0005"+
		"}\u0000\u0000#\u0006\u0001\u0000\u0000\u0000$%\u0005f\u0000\u0000%&\u0005"+
		"r\u0000\u0000&\'\u0005a\u0000\u0000\'(\u0005s\u0000\u0000()\u0005e\u0000"+
		"\u0000)\b\u0001\u0000\u0000\u0000*+\u0005p\u0000\u0000+,\u0005a\u0000"+
		"\u0000,-\u0005u\u0000\u0000-.\u0005s\u0000\u0000./\u0005a\u0000\u0000"+
		"/\n\u0001\u0000\u0000\u000001\u0005(\u0000\u00001\f\u0001\u0000\u0000"+
		"\u000023\u0005)\u0000\u00003\u000e\u0001\u0000\u0000\u000046\u0007\u0000"+
		"\u0000\u000054\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000075\u0001"+
		"\u0000\u0000\u000078\u0001\u0000\u0000\u00008\u0010\u0001\u0000\u0000"+
		"\u00009;\u0007\u0001\u0000\u0000:<\u0007\u0002\u0000\u0000;:\u0001\u0000"+
		"\u0000\u0000;<\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=>\u0007"+
		"\u0000\u0000\u0000>\u0012\u0001\u0000\u0000\u0000?C\u0007\u0003\u0000"+
		"\u0000@B\u0007\u0004\u0000\u0000A@\u0001\u0000\u0000\u0000BE\u0001\u0000"+
		"\u0000\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000D\u0014"+
		"\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000FG\u0005/\u0000\u0000"+
		"GH\u0005/\u0000\u0000HL\u0001\u0000\u0000\u0000IK\b\u0005\u0000\u0000"+
		"JI\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001\u0000"+
		"\u0000\u0000OQ\u0005\r\u0000\u0000PO\u0001\u0000\u0000\u0000PQ\u0001\u0000"+
		"\u0000\u0000QR\u0001\u0000\u0000\u0000RS\u0005\n\u0000\u0000ST\u0001\u0000"+
		"\u0000\u0000TU\u0006\n\u0000\u0000U\u0016\u0001\u0000\u0000\u0000VX\u0007"+
		"\u0006\u0000\u0000WV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000"+
		"YW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000"+
		"\u0000[\\\u0006\u000b\u0000\u0000\\\u0018\u0001\u0000\u0000\u0000\u0007"+
		"\u00007;CLPY\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}