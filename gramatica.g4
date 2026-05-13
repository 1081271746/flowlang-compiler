grammar gramatica;

program
    : INICIO PUNTOYCOMA statement* FIN PUNTOYCOMA EOF
    ;

statement
    : processStmt
    | ifStmt
    | showStmt
    ;

processStmt
    : PROCESO ID DOSPUNTOS expr PUNTOYCOMA
    ;

ifStmt
    : SI condition DOSPUNTOS ifBlock SINO DOSPUNTOS elseBlock FINSI PUNTOYCOMA
    ;

ifBlock
    : statement*
    ;

elseBlock
    : statement*
    ;

showStmt
    : MOSTRAR expr PUNTOYCOMA
    ;

condition
    : expr comparator expr
    ;

expr
    : expr op=(MULT | DIV) expr
    | expr op=(SUMA | RESTA) expr
    | NUMBER
    | ID
    | LPAREN expr RPAREN
    ;

comparator
    : MAYORIGUAL
    | MENORIGUAL
    | IGUAL
    | DIFERENTE
    | MAYOR
    | MENOR
    ;

// Palabras reservadas
INICIO : 'Inicio';
FINSI : 'FinSi';
FIN : 'Fin';
PROCESO : 'Proceso';
SI : 'Si';
SINO : 'Sino';
MOSTRAR : 'Mostrar';

// Operadores relacionales
MAYORIGUAL : '>=';
MENORIGUAL : '<=';
IGUAL : '==';
DIFERENTE : '!=';
MAYOR : '>';
MENOR : '<';

// Operadores aritméticos
SUMA : '+';
RESTA : '-';
MULT : '*';
DIV : '/';

// Símbolos
DOSPUNTOS : ':';
PUNTOYCOMA : ';';
LPAREN : '(';
RPAREN : ')';

// Valores
ID : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER : [0-9]+;

// Ignorar espacios, saltos de línea y comentarios
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;