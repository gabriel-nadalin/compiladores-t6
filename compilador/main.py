from antlr4 import CommonTokenStream, FileStream
from compilador.antlr.notaLexer import notaLexer
from compilador.antlr.notaParser import notaParser
from compilador.AnalisadorSemantico import AnalisadorSemantico
from compilador.GeradorMIDI import GeradorMIDI
import subprocess

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
    
    va = AnalisadorSemantico()
    va.visitar_no(tree)
    va.mostrar_erros()

    # Gerando o código objeto "midi" usado pelo interpretador midi
    gerador = GeradorMIDI()
    gerador.visitar_no(tree)
    nome = file_name.split('.')[0].split('/')[-1] + '.mid'
    gerador.arquivo.save("midi/" + nome)

    # Rodando o interpretador midi
    subprocess.run(["./compilador/sintetizador", f"midi/{nome}"])