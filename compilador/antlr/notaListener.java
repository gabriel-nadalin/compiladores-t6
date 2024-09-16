// Generated from ./projeto/compilador/antlr/nota.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link notaParser}.
 */
public interface notaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link notaParser#musica}.
	 * @param ctx the parse tree
	 */
	void enterMusica(notaParser.MusicaContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#musica}.
	 * @param ctx the parse tree
	 */
	void exitMusica(notaParser.MusicaContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#declaracoes}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracoes(notaParser.DeclaracoesContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#declaracoes}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracoes(notaParser.DeclaracoesContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao(notaParser.DeclaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao(notaParser.DeclaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#declaracao_acorde}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao_acorde(notaParser.Declaracao_acordeContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#declaracao_acorde}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao_acorde(notaParser.Declaracao_acordeContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#acorde}.
	 * @param ctx the parse tree
	 */
	void enterAcorde(notaParser.AcordeContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#acorde}.
	 * @param ctx the parse tree
	 */
	void exitAcorde(notaParser.AcordeContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#declaracao_frase}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao_frase(notaParser.Declaracao_fraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#declaracao_frase}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao_frase(notaParser.Declaracao_fraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#frase}.
	 * @param ctx the parse tree
	 */
	void enterFrase(notaParser.FraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#frase}.
	 * @param ctx the parse tree
	 */
	void exitFrase(notaParser.FraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#evento}.
	 * @param ctx the parse tree
	 */
	void enterEvento(notaParser.EventoContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#evento}.
	 * @param ctx the parse tree
	 */
	void exitEvento(notaParser.EventoContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#evento_tempo}.
	 * @param ctx the parse tree
	 */
	void enterEvento_tempo(notaParser.Evento_tempoContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#evento_tempo}.
	 * @param ctx the parse tree
	 */
	void exitEvento_tempo(notaParser.Evento_tempoContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#acorde_ident}.
	 * @param ctx the parse tree
	 */
	void enterAcorde_ident(notaParser.Acorde_identContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#acorde_ident}.
	 * @param ctx the parse tree
	 */
	void exitAcorde_ident(notaParser.Acorde_identContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#frase_ident}.
	 * @param ctx the parse tree
	 */
	void enterFrase_ident(notaParser.Frase_identContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#frase_ident}.
	 * @param ctx the parse tree
	 */
	void exitFrase_ident(notaParser.Frase_identContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#duracao}.
	 * @param ctx the parse tree
	 */
	void enterDuracao(notaParser.DuracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#duracao}.
	 * @param ctx the parse tree
	 */
	void exitDuracao(notaParser.DuracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link notaParser#execucao}.
	 * @param ctx the parse tree
	 */
	void enterExecucao(notaParser.ExecucaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link notaParser#execucao}.
	 * @param ctx the parse tree
	 */
	void exitExecucao(notaParser.ExecucaoContext ctx);
}