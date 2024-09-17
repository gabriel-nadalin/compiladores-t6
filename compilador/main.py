from antlr4 import CommonTokenStream, FileStream
from antlr.notaLexer import notaLexer
from antlr.notaParser import notaParser
from VisitadorArvore import VisitadorArvore

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Nome do arquivo de entrada faltando!')
        print('Uso: <path/arquivo>')
        exit(1)
    file_name = sys.argv[1]

    input_stream = FileStream(file_name, 'utf-8')
    lexer = notaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = notaParser(token_stream)
    tree = parser.musica()

    # print(tree.toStringTree(recog=parser))
    
    va = VisitadorArvore()
    va.visitar_no(tree)
    va.mostrar_erros()