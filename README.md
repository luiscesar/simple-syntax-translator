# simple-syntax-translator
INTRODUCCTION
This example shows a software development that translates representative programming language statements
into three-address code, an intermediate representation.

EXAMPLE
This syntax-directed translator maps code fragments as Fig 1. into three-address code of the form of  Fig. 2

{
int i; int j; float[100] a; float v; float x;
while ( true ) {
do i = i+1; while ( a[i] < v );
do j = j-1; while ( a[j] > v );
if ( i >= j ) break;
x = a[i]; a[i] = a[j]; a[j] = x;
}
}
Fig 1.

1: i = i + 1
2: t1 = a [ i ]
3: if t1 < v goto 1
4: j = j - 1
5: t2 = a [ j ]
6: if t2 > v goto 4
7: ifFalse i >= j goto 9
8: goto 14
9: x = a [ i ]
10: t3 = a [ j ]
11: a [ i ] = t3
12: a [ j ] = x
13: goto 1
14:
Fig 2.


THE SOURCE LANGUAGE

For specifying syntax, we present a widely used notation, called context-free grammars or BNF (for Backus-Naur Form)

program --> block
block --> { decls stmts }
decls --> decls decl | ϵ
decl --> type id ;
type --> type [ num ] | basic
stmts --> stmts stmt | ϵ
stmt --> loc = bool ;
             | if ( bool ) stmt
             | if ( bool ) stmt else stmt
             | while ( bool ) stmt
             | do stmt while ( bool ) ;
             | break ;
             |block
loc --> loc [ bool ] | id
bool --> bool || join | join
join --> join && equality | equality
equality --> equality == rel | equality != rel | rel
rel --> expr < expr | expr <= expr | expr >= expr | expr > expr | expr
expr --> expr + term | expr - term | term
term --> term * unary | term / unary | unary
unary -->! unary |- unary | factor
factor --> ( bool ) | loc | num | real | true | false

THREE-ADDRESS INSTRUCTIONS

Three-address code is a sequence of instructions of the form
		x = y op z.

Arrays will be handled by using the following two variants of instructions:
		x [ y ] = z
		x = y [ z ]

Three-address instructions are executed in numerical sequence unless forced
to do otherwise by a conditional or unconditional jump. We choose the following
instructions for control flow:
	ifFalse x goto L if x is false, next execute the instruction labeled L
	ifTrue x goto L if x is true, next execute the instruction labeled L
	goto L next execute the instruction labeled L

A label L can be attached to any instruction by prepending a prefix L:. An
instruction can have more than one label.

Finally, we need instructions that copy a value. The following three-address
instruction copies the value of y into x:
		x = y

EXECUTION
1) Update system variable path with python location
    Example:
     set path=%userprofile%\software\python\Python37

2) Edit a file with a source language program.
   Example: 
    Edit %userprofile%\<download_directory>\simple-syntax-translator\tests\resources\TestSource.txt

3) Set PYTHONPATH
   Example:
     PYTHONPATH=%userprofile%\<download_directory>\simple-syntax-translator

4) Run Translator
     Example:
        python compiler\main\Compiler.py tests\resources\TestSource.txt
 
