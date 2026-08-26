# Paradigmas de Linguagens de Programação: Atividade Aula 03

[← voltar ao índice do repositório](../README.md)

Atividade: **Derivação de um código a partir da gramática de uma linguagem de
programação**.

O objetivo é pesquisar a gramática formal de uma linguagem real, selecionar as
regras de produção necessárias e usá-las para derivar, passo a passo, um trecho
de código válido — relacionando na prática os conceitos de símbolo terminal,
símbolo não terminal, produção e derivação.

## Estrutura do repositório

```
.
└── README.md     # este documento (atividade completa)
```

---

## 1. Fonte da gramática

| Item | Valor |
|---|---|
| **Linguagem escolhida** | Python (CPython 3) |
| **Fonte da gramática sintática** | <https://docs.python.org/3/reference/grammar.html> — *10. Full Grammar specification* |
| **Fonte da gramática léxica** | <https://docs.python.org/3/reference/lexical_analysis.html> — *2. Lexical analysis* |
| **Fonte sobre a notação** | <https://docs.python.org/pt-br/3.13/reference/introduction.html> — *1.2. Notação* e [PEP 617](https://peps.python.org/pep-0617/) |
| **Notação da gramática sintática** | **PEG** (*Parsing Expression Grammar*), adotada pelo CPython a partir da versão 3.9 |
| **Notação da gramática léxica** | **BNF modificada / EBNF**, conforme a própria documentação |

### 1.1. Por que duas gramáticas?

Python é descrito em **dois níveis**, e a atividade toca nos dois:

- A **gramática léxica** descreve como os caracteres do arquivo-fonte são
  agrupados em *tokens* (`NAME`, `NUMBER`, `NEWLINE`, operadores). É escrita
  em BNF modificada, com `::=` nas versões da documentação que usam esse
  operador.
- A **gramática sintática** descreve como a *sequência de tokens* forma um
  programa. É escrita em PEG e é a que aparece em `grammar.html`.

Ou seja: `NAME` e `NUMBER` são **não terminais** para o analisador léxico, mas
chegam ao analisador sintático já como **terminais**. Essa distinção é
explicitada na seção 7.

### 1.2. Notação PEG — símbolos usados

Reproduzido do cabeçalho da própria gramática do CPython:

```
# rule_name: expression   define uma regra
# e1 e2                   casa e1, depois casa e2 (sequência)
# e1 | e2                 casa e1 ou e2 (escolha ORDENADA)
# ( e )                   agrupamento
# [ e ] ou e?             casa e opcionalmente
# e*                      zero ou mais ocorrências de e
# e+                      uma ou mais ocorrências de e
# s.e+                    uma ou mais ocorrências de e separadas por s
# &e                      sucesso se e casa, SEM consumir entrada (lookahead positivo)
# !e                      falha se e casa, SEM consumir entrada (lookahead negativo)
# ~                       compromete-se com a alternativa atual
```

Três pontos importantes dessa notação, que aparecem na derivação:

1. **`|` é escolha ordenada, não alternativa livre.** A primeira alternativa
   que casar é a escolhida, e o analisador não volta atrás. É por isso que a
   gramática traz o comentário *"assignment MUST precede expression"*: se
   `star_expressions` viesse antes de `assignment` em `simple_stmt`, o
   analisador consumiria `total` como expressão e o `=` seguinte viraria erro
   de sintaxe.
2. **`!e` e `&e` não consomem entrada.** Aparecem na derivação como passos que
   *verificam* algo sem produzir nenhum símbolo, e por isso não alteram a
   forma sentencial.
3. **PEG admite recursão à esquerda** (PEP 617). Regras como
   `sum: sum '+' term` são legais e são exatamente o que codifica a
   **associatividade à esquerda** dos operadores.

---

## 2. Produções selecionadas

Apenas as regras necessárias para o código escolhido, copiadas literalmente da
fonte.

### 2.1. Regra inicial e estrutura do arquivo

```
file: [statements] ENDMARKER

statements: statement+

statement:
    | compound_stmt
    | simple_stmts

simple_stmts:
    | simple_stmt !';' NEWLINE  # Not needed, there for speedup
    | ';'.simple_stmt+ [';'] NEWLINE
```

- **`file`** é o **símbolo inicial** da gramática para um arquivo-fonte. Diz
  que um arquivo é uma lista opcional de comandos seguida do token
  `ENDMARKER` (o fim de arquivo produzido pelo analisador léxico).
- **`statements`** é um ou mais comandos.
- **`statement`** separa comandos compostos (`if`, `for`, `def`, que abrem
  bloco) dos comandos simples.
- **`simple_stmts`** trata a linha física: um comando simples que **não** seja
  seguido de `;` termina em `NEWLINE`.

### 2.2. Comando simples e atribuição

```
# NOTE: assignment MUST precede expression, else parsing a simple assignment
# will throw a SyntaxError.
simple_stmt:
    | assignment
    | type_alias
    | star_expressions
    | return_stmt
    | ...

assignment:
    | NAME ':' expression ['=' annotated_rhs ]
    | ('(' single_target ')'
         | single_subscript_attribute_target) ':' expression ['=' annotated_rhs ]
    | (star_targets '=' )+ annotated_rhs !'=' [TYPE_COMMENT]
    | single_target augassign ~ annotated_rhs

annotated_rhs: yield_expr | star_expressions
```

- **`assignment`** tem quatro alternativas: atribuição com anotação de tipo
  (`x: int = 1`), anotação em alvo mais complexo, **atribuição simples** e
  atribuição composta (`x += 1`).
- A terceira alternativa, `(star_targets '=' )+ annotated_rhs`, é a usada aqui:
  um ou mais alvos separados por `=` (o que permite `a = b = 0`), seguidos do
  lado direito. O `!'='` final garante que não sobrou outro `=`.
- **`annotated_rhs`** é o lado direito da atribuição.

### 2.3. Alvo da atribuição (lado esquerdo)

```
star_targets:
    | star_target !','
    | star_target (',' star_target )* [',']

star_target:
    | '*' (!'*' star_target)
    | target_with_star_atom

target_with_star_atom:
    | t_primary '.' NAME !t_lookahead
    | t_primary '[' slices ']' !t_lookahead
    | star_atom

star_atom:
    | NAME
    | '(' target_with_star_atom ')'
    | '(' [star_targets_tuple_seq] ')'
    | '[' [star_targets_list_seq] ']'
```

Essa cadeia existe porque o lado esquerdo de uma atribuição em Python pode ser
muito mais que um nome: `a.b = 1`, `a[0] = 1`, `a, b = 1, 2`, `*resto = ...`.
Para um alvo que é um nome simples, a cadeia colapsa em quatro passos até
`NAME`.

### 2.4. Cascata de expressões (lado direito)

```
star_expressions:
    | star_expression (',' star_expression )+ [',']
    | star_expression ','
    | star_expression

star_expression:
    | '*' bitwise_or
    | expression

expression:
    | disjunction 'if' disjunction 'else' expression
    | disjunction
    | lambdef

disjunction:  | conjunction ('or' conjunction )+   | conjunction
conjunction:  | inversion ('and' inversion )+      | inversion
inversion:    | 'not' inversion                    | comparison
comparison:   | bitwise_or compare_op_bitwise_or_pair+   | bitwise_or
bitwise_or:   | bitwise_or '|' bitwise_xor         | bitwise_xor
bitwise_xor:  | bitwise_xor '^' bitwise_and        | bitwise_and
bitwise_and:  | bitwise_and '&' shift_expr         | shift_expr
shift_expr:   | shift_expr '<<' sum   | shift_expr '>>' sum   | sum

sum:
    | sum '+' term
    | sum '-' term
    | term

term:
    | term '*' factor
    | term '/' factor
    | term '//' factor
    | term '%' factor
    | term '@' factor
    | factor

factor:
    | '+' factor
    | '-' factor
    | '~' factor
    | power

power:
    | await_primary '**' factor
    | await_primary

await_primary:
    | 'await' primary
    | primary

primary:
    | primary '.' NAME
    | primary genexp
    | primary '(' [arguments] ')'
    | primary '[' slices ']'
    | atom

atom:
    | NAME
    | 'True'
    | 'False'
    | 'None'
    | strings
    | NUMBER
    | (tuple | group | genexp)
    | (list | listcomp)
    | (dict | set | dictcomp | setcomp)
    | '...'
```

Esta é a parte conceitualmente mais importante da atividade. A cascata
`star_expressions → ... → sum → term → factor → power → await_primary →
primary → atom` **não é redundância**: cada nível corresponde a um nível de
**precedência de operadores**, do menos ligado (vírgula, `if/else` ternário,
`or`) ao mais ligado (chamada, indexação, átomo).

Duas consequências que a derivação vai exibir:

- **Precedência.** Como `sum` só pode alcançar `*` descendo até `term`, a
  multiplicação fica obrigatoriamente *abaixo* da soma na árvore. A gramática
  torna `2 + 3 * 4` igual a `2 + (3 * 4)` — não há regra de precedência
  externa, ela está embutida na forma das produções.
- **Associatividade.** `sum: sum '+' term` recorre à esquerda, então
  `a - b - c` se agrupa como `(a - b) - c`. Já `power: await_primary '**'
  factor` recorre à direita, e por isso `2 ** 3 ** 2` é `2 ** (3 ** 2)`.

### 2.5. Regras léxicas dos tokens usados

Da gramática léxica (notação BNF modificada):

```
NAME          ::= name_start name_continue*
name_start    ::= "a"..."z" | "A"..."Z" | "_" | <caractere não-ASCII>
name_continue ::= name_start | "0"..."9"
identifier    ::= <NAME, exceto palavras reservadas>

integer       ::= decinteger | bininteger | octinteger | hexinteger | zerointeger
decinteger    ::= nonzerodigit (["_"] digit)*
nonzerodigit  ::= "1"..."9"
digit         ::= "0"..."9"
```

---

## 3. Código a ser derivado

```python
total = 2 + 3 * 4
```

Escolhido por ser uma **atribuição com expressão aritmética**: é curto o
suficiente para uma derivação completa e, ao mesmo tempo, exercita o alvo da
atribuição, a cascata inteira de expressões e a precedência entre `+` e `*`.

Ao final da execução, `total` vale `14` — e não `20` —, o que a árvore de
derivação explica sem precisar de nenhuma regra extra.

### 3.1. Sequência de tokens correspondente

O analisador léxico produz, a partir desse texto:

```
NAME('total')  OP('=')  NUMBER('2')  OP('+')  NUMBER('3')  OP('*')  NUMBER('4')  NEWLINE  ENDMARKER
```

É essa sequência que a gramática sintática precisa gerar.

---

## 4. Derivação passo a passo

Derivação **mais à esquerda**, partindo do símbolo inicial `file`. Símbolos não
terminais aparecem em texto simples; terminais aparecem entre aspas.

```
file

⇒  statements ENDMARKER
       [file: [statements] ENDMARKER — parte opcional presente]

⇒  statement ENDMARKER
       [statements: statement+ — uma única ocorrência]

⇒  simple_stmts ENDMARKER
       [statement: 2ª alternativa (não é comando composto)]

⇒  simple_stmt NEWLINE ENDMARKER
       [simple_stmts: 1ª alternativa; o !';' é lookahead negativo e não
        consome nem produz símbolo]

⇒  assignment NEWLINE ENDMARKER
       [simple_stmt: 1ª alternativa]

⇒  star_targets "=" annotated_rhs NEWLINE ENDMARKER
       [assignment: 3ª alternativa, com (star_targets '=')+ repetido uma vez;
        !'=' e [TYPE_COMMENT] não produzem símbolo]

⇒  star_target "=" annotated_rhs NEWLINE ENDMARKER
       [star_targets: 1ª alternativa; o !',' é lookahead]

⇒  target_with_star_atom "=" annotated_rhs NEWLINE ENDMARKER
       [star_target: 2ª alternativa]

⇒  star_atom "=" annotated_rhs NEWLINE ENDMARKER
       [target_with_star_atom: 3ª alternativa]

⇒  NAME "=" annotated_rhs NEWLINE ENDMARKER
       [star_atom: 1ª alternativa]

⇒  "total" "=" annotated_rhs NEWLINE ENDMARKER
       [NAME ::= name_start name_continue* — ver sub-derivação léxica em 4.1]

⇒  "total" "=" star_expressions NEWLINE ENDMARKER
       [annotated_rhs: 2ª alternativa]

⇒  "total" "=" star_expression NEWLINE ENDMARKER
       [star_expressions: 3ª alternativa — um só elemento, sem vírgula]

⇒  "total" "=" expression NEWLINE ENDMARKER
       [star_expression: 2ª alternativa]

⇒  "total" "=" disjunction NEWLINE ENDMARKER      [expression: 2ª alt.]
⇒  "total" "=" conjunction NEWLINE ENDMARKER      [disjunction: 2ª alt.]
⇒  "total" "=" inversion NEWLINE ENDMARKER        [conjunction: 2ª alt.]
⇒  "total" "=" comparison NEWLINE ENDMARKER       [inversion: 2ª alt.]
⇒  "total" "=" bitwise_or NEWLINE ENDMARKER       [comparison: 2ª alt.]
⇒  "total" "=" bitwise_xor NEWLINE ENDMARKER      [bitwise_or: 2ª alt.]
⇒  "total" "=" bitwise_and NEWLINE ENDMARKER      [bitwise_xor: 2ª alt.]
⇒  "total" "=" shift_expr NEWLINE ENDMARKER       [bitwise_and: 2ª alt.]
⇒  "total" "=" sum NEWLINE ENDMARKER              [shift_expr: 3ª alt.]

       ↑ estes nove passos atravessam a cascata de precedência sem aplicar
         nenhum operador: o código não usa vírgula, ternário, or, and, not,
         comparação, |, ^, & nem deslocamento.

⇒  "total" "=" sum "+" term NEWLINE ENDMARKER
       [sum: 1ª alternativa — AQUI a soma é introduzida]

⇒  "total" "=" term "+" term NEWLINE ENDMARKER
       [sum: 3ª alternativa, aplicada ao sum mais à esquerda]

⇒  "total" "=" factor "+" term NEWLINE ENDMARKER          [term: 6ª alt.]
⇒  "total" "=" power "+" term NEWLINE ENDMARKER           [factor: 4ª alt.]
⇒  "total" "=" await_primary "+" term NEWLINE ENDMARKER   [power: 2ª alt.]
⇒  "total" "=" primary "+" term NEWLINE ENDMARKER         [await_primary: 2ª alt.]
⇒  "total" "=" atom "+" term NEWLINE ENDMARKER            [primary: 5ª alt.]
⇒  "total" "=" NUMBER "+" term NEWLINE ENDMARKER          [atom: 6ª alt.]
⇒  "total" "=" "2" "+" term NEWLINE ENDMARKER             [NUMBER → "2"]

⇒  "total" "=" "2" "+" term "*" factor NEWLINE ENDMARKER
       [term: 1ª alternativa — AQUI a multiplicação é introduzida, já DENTRO
        do operando direito da soma]

⇒  "total" "=" "2" "+" factor "*" factor NEWLINE ENDMARKER   [term: 6ª alt.]
⇒  "total" "=" "2" "+" power "*" factor NEWLINE ENDMARKER    [factor: 4ª alt.]
⇒  "total" "=" "2" "+" await_primary "*" factor NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" primary "*" factor NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" atom "*" factor NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" NUMBER "*" factor NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" "3" "*" factor NEWLINE ENDMARKER      [NUMBER → "3"]

⇒  "total" "=" "2" "+" "3" "*" power NEWLINE ENDMARKER       [factor: 4ª alt.]
⇒  "total" "=" "2" "+" "3" "*" await_primary NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" "3" "*" primary NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" "3" "*" atom NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" "3" "*" NUMBER NEWLINE ENDMARKER
⇒  "total" "=" "2" "+" "3" "*" "4" NEWLINE ENDMARKER         [NUMBER → "4"]
```

Forma sentencial final (só terminais):

```
"total" "=" "2" "+" "3" "*" "4" NEWLINE ENDMARKER
```

### 4.1. Sub-derivações léxicas

Os terminais `NAME` e `NUMBER` do parser são, por sua vez, gerados pela
gramática léxica:

```
NAME
⇒ name_start name_continue*
⇒ name_start name_continue name_continue name_continue name_continue
⇒ "t" "o" "t" "a" "l"
⇒ "total"
```

```
NUMBER  (via integer)
⇒ decinteger
⇒ nonzerodigit (["_"] digit)*      [zero repetições]
⇒ nonzerodigit
⇒ "2"
```

O mesmo vale para `"3"` e `"4"`.

---

## 5. Árvore de derivação

A mesma derivação, vista como árvore. As cadeias de regra única foram
comprimidas com `→` para caber na página.

```
file
├── statements → statement → simple_stmts
│   ├── simple_stmt → assignment
│   │   ├── star_targets → star_target → target_with_star_atom → star_atom
│   │   │   └── NAME .................................... "total"
│   │   ├── "="
│   │   └── annotated_rhs → star_expressions → star_expression
│   │       → expression → disjunction → conjunction → inversion
│   │       → comparison → bitwise_or → bitwise_xor → bitwise_and
│   │       → shift_expr → sum
│   │       ├── sum → term → factor → power → await_primary → primary → atom
│   │       │   └── NUMBER ............................... "2"
│   │       ├── "+"
│   │       └── term
│   │           ├── term → factor → power → await_primary → primary → atom
│   │           │   └── NUMBER ........................... "3"
│   │           ├── "*"
│   │           └── factor → power → await_primary → primary → atom
│   │               └── NUMBER ........................... "4"
│   └── NEWLINE
└── ENDMARKER
```

O nó `"*"` está **abaixo** do nó `"+"`: a multiplicação é filha do operando
direito da soma. É essa forma da árvore que faz `total` valer `14`.

---

## 6. Resultado

```python
total = 2 + 3 * 4   # total == 14
```

### 6.1. Como as regras chegaram até o código, em palavras

Partindo de `file`, o único caminho que leva a uma linha de código é
`statements → statement → simple_stmts`, que exige um comando simples seguido
de `NEWLINE`. Entre as alternativas de `simple_stmt`, `assignment` vem
primeiro justamente para que uma linha começando com um nome seguido de `=`
seja reconhecida como atribuição, e não como expressão solta.

Dentro de `assignment`, as duas primeiras alternativas exigem `:` (anotação de
tipo) e falham; a terceira, `(star_targets '=')+ annotated_rhs`, é a que casa.
Ela divide o problema em dois: o alvo à esquerda e a expressão à direita.

O alvo desce por `star_targets → star_target → target_with_star_atom →
star_atom` até `NAME`. Essa cadeia parece longa para um nome simples, mas ela
existe porque o mesmo ponto da gramática precisa aceitar `a.b`, `a[0]`,
`(a, b)` e `*resto`.

A expressão à direita atravessa toda a cascata de precedência. Nos nove
primeiros passos nada acontece — o código não usa nenhum dos operadores de
baixa precedência —, e a cascata só "acorda" em `sum`, onde a produção
recursiva `sum '+' term` introduz o `+`. O operando esquerdo desce direto até
o número `2`. O operando direito é um `term`, e é exatamente por ser um `term`
que ele pode aplicar `term '*' factor` e produzir `3 * 4`.

O ponto central: a **precedência não é uma regra à parte, é a forma da
gramática**. Como o `*` só pode nascer em `term`, e `term` está abaixo de
`sum`, é impossível derivar uma árvore em que `2 + 3` seja operando de `*`.
A gramática não gera `(2 + 3) * 4` para esse texto — para obter isso seria
preciso escrever os parênteses, que entram por outra alternativa de `atom`.

---

## 7. Terminais e não terminais

### 7.1. Não terminais utilizados

Todos são nomes de regra em minúsculas na gramática do CPython:

| Não terminal | Papel na derivação |
|---|---|
| `file` | símbolo inicial |
| `statements`, `statement`, `simple_stmts`, `simple_stmt` | estrutura do arquivo e da linha |
| `assignment`, `annotated_rhs` | a atribuição e seu lado direito |
| `star_targets`, `star_target`, `target_with_star_atom`, `star_atom` | alvo da atribuição |
| `star_expressions`, `star_expression`, `expression` | topo da cascata de expressões |
| `disjunction`, `conjunction`, `inversion`, `comparison` | níveis lógicos e de comparação (atravessados sem uso) |
| `bitwise_or`, `bitwise_xor`, `bitwise_and`, `shift_expr` | níveis bit a bit (atravessados sem uso) |
| `sum` | nível da adição/subtração — **usado** |
| `term` | nível da multiplicação/divisão — **usado** |
| `factor`, `power`, `await_primary`, `primary` | unário, potência, `await`, sufixos |
| `atom` | folha da cascata |
| `name_start`, `name_continue`, `integer`, `decinteger`, `nonzerodigit`, `digit` | não terminais da gramática **léxica** |

### 7.2. Terminais utilizados

Na gramática sintática há dois tipos de terminal:

**a) Literais**, escritos entre aspas na gramática:

| Terminal | Onde aparece |
|---|---|
| `'='` | `assignment` |
| `'+'` | `sum` |
| `'*'` | `term` |

**b) Tokens**, escritos em MAIÚSCULAS e produzidos pelo analisador léxico:

| Token | Valor no código | Observação |
|---|---|---|
| `NAME` | `total` | não terminal na gramática léxica, terminal na sintática |
| `NUMBER` | `2`, `3`, `4` | idem |
| `NEWLINE` | fim da linha lógica | token sem texto visível |
| `ENDMARKER` | fim do arquivo | token sem texto visível |

Na gramática **léxica**, por sua vez, os terminais são os próprios caracteres:
`"t"`, `"o"`, `"a"`, `"l"`, `"2"`, `"3"`, `"4"` — descritos por faixas como
`"a"..."z"` e `"1"..."9"`.

### 7.3. Símbolos que não produzem saída

Aparecem na gramática e foram citados na derivação, mas **não são terminais
nem não terminais** — são operadores da metanotação PEG:

| Símbolo | Significado |
|---|---|
| `!';'` em `simple_stmts` | lookahead negativo: falha se o próximo token for `;` |
| `!','` em `star_targets` | lookahead negativo: garante alvo único |
| `!'='` em `assignment` | lookahead negativo: garante fim da cadeia de `=` |
| `[TYPE_COMMENT]` | parte opcional, ausente aqui |

---

## 8. Observação metodológica: PEG não é uma gramática gerativa

Vale registrar uma diferença conceitual, já que a atividade pede uma
*derivação*:

- Uma gramática **livre de contexto** em BNF é um dispositivo **gerativo**:
  parte-se do símbolo inicial e *produzem-se* sentenças. `⇒` significa
  literalmente "produz".
- Uma **PEG** é um dispositivo **reconhecedor**: descreve um analisador
  descendente com retrocesso limitado, que consome uma entrada e decide se ela
  casa. O `|` é escolha ordenada, e por construção não existe ambiguidade — uma
  entrada válida tem exatamente uma árvore.

Na prática, para o subconjunto de regras usado aqui, as duas leituras coincidem
e a derivação acima é válida nos dois sentidos: pode ser lida de cima para
baixo como geração do código, ou de baixo para cima como o caminho que o
analisador do CPython percorre para reconhecê-lo. A escolha ordenada só
importaria se houvesse ambiguidade — e é exatamente o que o comentário
*"assignment MUST precede expression"* na gramática oficial documenta.

---

## 9. Verificação

A derivação foi conferida contra o próprio analisador do CPython.

**Tokens** (`tokenize`) — coincidem com a forma sentencial final da seção 4:

```
NAME 'total'   OP '='   NUMBER '2'   OP '+'   NUMBER '3'   OP '*'   NUMBER '4'   NEWLINE   ENDMARKER
```

**Árvore sintática** (`ast.parse`) — coincide com a árvore da seção 5:

```python
Module(body=[
  Assign(
    targets=[Name(id='total', ctx=Store())],
    value=BinOp(
      left=Constant(value=2),
      op=Add(),
      right=BinOp(
        left=Constant(value=3),
        op=Mult(),
        right=Constant(value=4))))])
```

O `BinOp(Mult)` aparece como filho **direito** do `BinOp(Add)`, confirmando o
agrupamento `2 + (3 * 4)` previsto pela cascata `sum → term`. E
`eval("2 + 3 * 4")` retorna `14`.

---

## 10. Referências

- Python Software Foundation. *10. Full Grammar specification*. Disponível em:
  <https://docs.python.org/3/reference/grammar.html>
- Python Software Foundation. *2. Lexical analysis*. Disponível em:
  <https://docs.python.org/3/reference/lexical_analysis.html>
- Python Software Foundation. *1. Introdução — Notação*. Disponível em:
  <https://docs.python.org/pt-br/3.13/reference/introduction.html>
- PEP 617 — *New PEG parser for CPython*. Disponível em:
  <https://peps.python.org/pep-0617/>
- SEBESTA, R. W. *Concepts of Programming Languages*, cap. 3 — Describing
  Syntax and Semantics.
