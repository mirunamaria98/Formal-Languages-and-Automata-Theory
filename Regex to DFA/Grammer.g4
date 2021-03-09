grammar Grammer;

REUNIUNE : '|' ;
OPEN : '(' ;
CLOSED : ')' ;
STAR : '*' ;

WHITESPACE : [ \t\r\n]+ -> skip;

VAR : ([a-z]);

expr : m_expr REUNIUNE expr | m_expr ;//OR
m_expr : a_expr m_expr | a_expr ;//AND
a_expr: a_expr STAR | b_expr ;//STAR
b_expr : inner_expr | variabila ;
variabila : VAR ;
inner_expr : OPEN expr CLOSED ;

