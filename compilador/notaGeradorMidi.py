from antlr4 import *
from antlr.notaVisitor import notaVisitor
from antlr.notaLexer import notaLexer
from antlr.notaParser import notaParser

import sys

def visitPrograma(self):
    for i in range(self.ctx.getChildCount()):
        for j in range(self.ctx.getChild(i).getChildCount()):
            
            text, text2 = self.visitToken(self.ctx.getChild(i).getChild(j))
            line_split = []

            for k in text.split():
                line_split.append(k.split('|'))
            line, line2 = map(list, zip(*line_split))
        
            self.analyzeLine(line, line2, text2.split())

    return 

def print_tree(tree, level=0):
    indent = "  " * level
    if level != 0:
        print(indent + tree.getText())
    for child in tree.getChildren():
        if not isinstance(child,  TerminalNode):
            print_tree(child, level + 1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Nome do arquivo de entrada faltando!')
        print('Uso: <path/arquivo>')
        exit(1)
    file_name = sys.argv[1]

    input_stream = FileStream(file_name, 'utf-8')
    # print(input_stream)
    lexer = notaLexer(input_stream)
    # while True:
    #     token = lexer.nextToken()
    #     if token.type == Token.EOF:
    #         break
    #     print(token.text)



    token_stream = CommonTokenStream(lexer)
    parser = notaParser(token_stream)

    tree = parser.musica()
    print_tree(tree)

    # # print(list(tree.getChildren()))
    # # for token in tree.getChildren():
    # #     if isinstance(token, TerminalNode):
    # #         pass
    # #     print(token.symbol.type)