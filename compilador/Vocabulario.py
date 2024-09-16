from antlr4 import *
from antlr.notaLexer import notaLexer
import os
import sys

class Vocabulario:
    def __init__(self, tokens_file_name : str) -> None:
        self.dicionario = {}
        with open(tokens_file_name) as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace('\'', '')
                token, key = line.split('=')
                self.dicionario[int(key)] = token

    def get_str_tipo(self, tipo : int)->str | None:
        if tipo in self.dicionario.keys():
            return self.dicionario[tipo]
        return None
    
    def is_token(self, token) -> bool:
        return token in self.dicionario
    
if __name__ == '__main__':
    v = Vocabulario(sys.argv[1])
    print(v.dicionario)