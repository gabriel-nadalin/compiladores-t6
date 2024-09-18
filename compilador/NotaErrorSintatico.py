from antlr4.error.ErrorListener import ErrorListener

class NotaErroSintatico(ErrorListener):
    def __init__(self, output_archive) -> None:
        self.output_archive = output_archive
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        #Vendo se é colchete ou aspas duplas o primeiro caractere do token 
        print(f'Erro semântico na linha {line}: {str(msg)}')
        exit()