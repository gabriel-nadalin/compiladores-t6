grammar nota

musica: declaracoes execucao;
declaracoes: (declaracao)*;
declaracao: declaracao_acorde | declaracao_frase;
declaracao_acorde: 'acorde' IDENT acorde;
acorde: '{' (NOTA)+ '}';
declaracao_frase: 'frase' IDENT frase;
frase: '{' (evento)+ '}';
evento: evento_tempo | frase_ident;
evento_tempo: (NOTA | acorde_ident | 'pausa') '(' duracao ')';
acorde_ident: acorde | IDENT;
frase_ident: frase | IDENT;
duracao: NUM_INT;
execucao: (evento)*;
comentario: '//' (~('\n'|'\r')) {skip();};
NUM_INT: [0-9]+;
NOTA: [A-G] [#b]? [0-9];
IDENT: [a-zA-Z]([a-zA-Z]|[0-9]|'_')*;
WS: ( ' '
    | '\t'
    | '\r'
    | '\n'
    ) {skip();}
    ;