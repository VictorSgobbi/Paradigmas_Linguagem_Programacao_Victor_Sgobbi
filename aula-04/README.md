# Paradigmas de Linguagens de Programação: Atividade Aula 04

[← voltar ao índice do repositório](../README.md)

Aula exploratória prática sobre o **Capítulo 4 de Sebesta** (análise léxica e
análise sintática), executada em Java em 60 minutos, divididos em 5 estações.

A proposta é copiar, executar, alterar e registrar cinco programas curtos que
tornam visíveis etapas normalmente escondidas dentro de um compilador.

| Item | Valor |
|---|---|
| **Aluno** | Victor Hugo Pacchioni Sgobbi |
| **RA** | 24000732-2 |
| **Linguagem** | Java 17 ou superior |
| **Referência** | SEBESTA, R. W. *Conceitos de Linguagens de Programação*, 11. ed., cap. 4 |
| **Entrega** | 6 prints das 5 estações (entregues no portal da disciplina) |

## Estrutura do repositório

```
.
└── README.md                # este documento (enunciado e registro da atividade)
```

> Os cinco `Main.java` foram escritos e executados no laboratório da
> faculdade, e a entrega em si são os prints de cada estação. Por isso nem os
> fontes nem as imagens estão versionados aqui: este README é o registro
> escrito do que foi feito em cada estação.

---

## Enunciado

**Regra principal:** não pesquisar durante a atividade. Seguir cada passo na
ordem, alterar somente o que for solicitado e usar a saída do programa para
observar o conceito.

### Antes de começar

1. Abrir um ambiente com Java 17 ou superior, no computador ou no navegador;
2. Localizar os cinco programas, separados em pastas numeradas de 01 a 05;
3. Substituir os valores de `ALUNO` e `RA` antes da primeira execução;
4. Ao tirar cada print, deixar visíveis ao mesmo tempo uma parte do código e o
   console;
5. Não avançar com erro inesperado. Na Estação 3 os erros são propositais; nas
   demais, conferir se o programa foi copiado por inteiro.

### Distribuição dos 60 minutos

| Etapa | Tempo |
|---|---|
| Preparar | 5 min |
| Léxico (estações 1 e 2) | 17 min |
| Sintaxe (estação 3) | 9 min |
| Parsers (estações 4 e 5) | 23 min |
| Entregar | 6 min |

---

## Estação 1: de caracteres a lexemas e tokens

| Item | Valor |
|---|---|
| **Tempo** | 9 minutos |
| **Arquivo** | `01-lexemas-tokens/Main.java` |
| **Evidência** | `01_tokens.png` |

Objetivo: observar como uma linha de código-fonte é dividida em unidades com
significado.

Passos: executar o programa sem alterar a entrada inicial, ler as colunas
`LEXEMA` e `TOKEN`, localizar um identificador, um operador, um número inteiro
e o ponto e vírgula. Depois, trocar apenas a constante `ENTRADA` por uma
atribuição personalizada e executar de novo.

Entrada personalizada utilizada:

```java
static final String ENTRADA = "resultado = somaAnterior - valor / 1000;";
```

Saída obtida:

```
LEXEMA          TOKEN
------------------------------------
resultado       IDENTIFICADOR
=               ATRIBUICAO
somaAnterior    IDENTIFICADOR
-               SUBTRACAO
valor           IDENTIFICADOR
/               DIVISAO
1000            INTEIRO
;               PONTO_E_VIRGULA
```

O programa mantém a tabela de símbolos em um `LinkedHashMap<Character, String>`,
o que preserva a ordem de inserção dos operadores.

**Conclusão guiada:** `resultado` é o **lexema**, o texto que aparece no
arquivo. `IDENTIFICADOR` é o **token**, a categoria atribuída a esse lexema.
São coisas diferentes: três lexemas distintos aqui compartilham o mesmo token.

---

## Estação 2: o que o analisador léxico reconhece

| Item | Valor |
|---|---|
| **Tempo** | 8 minutos |
| **Arquivo** | `02-classes-reservadas/Main.java` |
| **Evidência** | `02_lexico.png` |

Objetivo: comparar espaços, comentários, palavras reservadas, identificadores e
caracteres inválidos.

Palavras reservadas reconhecidas pelo programa: `int`, `if`, `else`, `while`,
`return`.

Identificador personalizado utilizado:

```java
static final String IDENTIFICADOR_PERSONALIZADO = "nota_lm";
```

### Testes executados

| Teste | Foco | Entrada |
|---|---|---|
| A | entrada compacta | `int total=valor+10;` |
| B | espaços e comentário | `int   total  =  valor + 10;  // este comentario sera ignorado` |
| C | reservadas e identificadores | `int inteiro = 0; while (inteiro < intValor) inteiro = inteiro + 1;` |
| C2 | identificador personalizado | `int nota_lm = 10;` |
| D | caractere inválido | `int valor# = 1;` |

Saída do teste C2:

```
LEXEMA      CLASSE      TOKEN
------------------------------------------------
int         LETRA       PALAVRA_RESERVADA
nota_lm     LETRA       IDENTIFICADOR
=           SIMBOLO     ATRIBUICAO
10          DIGITO      INTEIRO
;           SIMBOLO     PONTO_E_VIRGULA
```

Saída do teste D:

```
LEXEMA      CLASSE          TOKEN
------------------------------------------------
int         LETRA           PALAVRA_RESERVADA
valor       LETRA           IDENTIFICADOR
#           DESCONHECIDO    ERRO_LEXICO
=           SIMBOLO         ATRIBUICAO
1           DIGITO          INTEIRO
;           SIMBOLO         PONTO_E_VIRGULA
```

### Observações

- Espaços adicionais não criaram novos tokens: os testes A e B produzem os
  mesmos tokens essenciais;
- O comentário foi ignorado pelo analisador;
- `int` saiu como `PALAVRA_RESERVADA`, mas `inteiro` e `intValor` saíram como
  `IDENTIFICADOR`, mesmo começando pelas mesmas letras. A decisão vem de
  consulta a uma tabela, não do prefixo;
- O caractere `#` foi rejeitado com `ERRO_LEXICO`, e a análise seguiu nos
  tokens restantes.

**Ligação com os slides:** o programa agrupa letras e dígitos em classes de
caracteres (`LETRA`, `DIGITO`, `SIMBOLO`, `DESCONHECIDO`) e depois consulta uma
tabela para decidir se um nome é palavra reservada.

---

## Estação 3: quando o compilador encontra erros

| Item | Valor |
|---|---|
| **Tempo** | 9 minutos |
| **Arquivo** | `03-diagnosticos/Main.java` |
| **Evidências** | `03_erro_compilador.png` e `04_programa_corrigido.png` |

O arquivo é entregue com erros propositais. Falhar na primeira compilação
significa que o experimento está funcionando.

### Primeira compilação

Diagnósticos do `javac`, sem nenhuma correção:

```
Main.java:8: error: ';' expected
        int total = 10 + 20 // CORRIGIR 1: acrescente o ponto e virgula
                            ^
Main.java:10: error: ')' expected
        if (total > 20 { // CORRIGIR 2: feche corretamente o parenteses
                      ^
Main.java:11: error: unclosed string literal
            System.out.println("Programa corrigido!); // CORRIGIR 3: feche o texto entre aspas
                               ^
3 errors
```

### Reparo mecânico

As três linhas marcadas foram corrigidas na ordem: ponto e vírgula ausente,
parêntese da condição não fechado e texto entre aspas não finalizado.

Saída depois das correções:

```
ALUNO: Victor Hugo Pacchioni Sgobbi | RA: 24000732-2
Programa corrigido!
Resultado: 30
```

### Classificação rápida

| Erro | Natureza |
|---|---|
| Texto entre aspas não finalizado | formação de um elemento **léxico** |
| Ponto e vírgula ausente | estrutura **sintática** incompleta |
| Parêntese não fechado | estrutura **sintática** incompleta |

O compilador aponta a linha e o símbolo esperado, o que basta para o reparo sem
entender a lógica do programa.

---

## Estação 4: parser descendente recursivo

| Item | Valor |
|---|---|
| **Tempo** | 14 minutos |
| **Arquivo** | `04-parser-descendente/Main.java` |
| **Evidência** | `05_descendente.png` |

Objetivo: acompanhar as chamadas de `expr`, `term` e `factor` enquanto o parser
percorre a expressão.

### Execução válida

A entrada original do roteiro é `2 + 3 * 4`, onde a multiplicação é tratada
dentro de `term` antes de `expr` concluir a soma. Em seguida a constante
`ENTRADA` foi trocada pela expressão personalizada:

```java
static final String ENTRADA = "(2 + 3) * 4";
static final boolean DEMONSTRAR_RECURSAO_ESQUERDA = false;
```

Rastreamento (trecho) e resultado:

```
SAINDO de <term>   | lookahead = +
Encontrado operador +
Novo lookahead: 3
  ENTRANDO em <term>   | lookahead = 3
    ENTRANDO em <factor> | lookahead = 3
      Numero reconhecido: 3
      Novo lookahead: )
    SAINDO de <factor>   | lookahead = )
  SAINDO de <term>       | lookahead = )
SAINDO de <expr>         | lookahead = )
Novo lookahead: *
Fechando parenteses
SAINDO de <factor>       | lookahead = *
Encontrado operador *
Novo lookahead: 4
  ENTRANDO em <term>     | lookahead = 4
    Numero reconhecido: 4
    Novo lookahead: $FIM$
  SAINDO de <factor>     | lookahead = $FIM$
SAINDO de <term>         | lookahead = $FIM$
SAINDO de <expr>         | lookahead = $FIM$

ENTRADA ACEITA
RESULTADO DA EXPRESSAO: 20
```

Com os parênteses explícitos o resultado é `20`, e não `14`: a soma passa a ser
reconhecida dentro de `factor`, portanto abaixo da multiplicação.

### Execução inválida e recursão à esquerda

Com a entrada `2 + * 4` o parser falha, e o token no *lookahead* no momento do
erro é o `*`, que aparece onde `factor` esperava um número ou um parêntese de
abertura.

Depois, com uma entrada válida restaurada, `DEMONSTRAR_RECURSAO_ESQUERDA` foi
ligado para uma execução e devolvido a `false`.

**Conclusão guiada:** o parser descendente começa pela regra mais geral e chama
métodos associados aos não terminais. Uma regra que chama a si mesma antes de
consumir entrada repete indefinidamente, e é por isso que a recursão à esquerda
não serve para essa técnica.

---

## Estação 5: parser ascendente, deslocar e reduzir

| Item | Valor |
|---|---|
| **Tempo** | 9 minutos |
| **Arquivo** | `05-parser-ascendente/Main.java` |
| **Evidência** | `06_ascendente.png` |

Objetivo: observar a entrada ser transferida para uma pilha e reduzida até o
símbolo inicial.

Gramática embutida no programa:

```
1) E -> E + T      2) E -> T
3) T -> T * F      4) T -> F
5) F -> id
```

Entradas configuradas:

```java
static final String ENTRADA_VALIDA = "id+id*id";
static final String ENTRADA_INVALIDA = "+id*id";
```

Rastreamento completo da entrada válida:

```
PILHA                       ENTRADA      ACAO
----------------------------------------------------------
$ 0                         id+id*id$    SHIFT id -> estado 5
$ 0 id 5                    +id*id$      REDUCE F -> id
$ 0 F 3                     +id*id$      REDUCE T -> F
$ 0 T 2                     +id*id$      REDUCE E -> T
$ 0 E 1                     +id*id$      SHIFT + -> estado 6
$ 0 E 1 + 6                 id*id$       SHIFT id -> estado 5
$ 0 E 1 + 6 id 5            *id$         REDUCE F -> id
$ 0 E 1 + 6 F 3             *id$         REDUCE T -> F
$ 0 E 1 + 6 T 9             *id$         SHIFT * -> estado 7
$ 0 E 1 + 6 T 9 * 7         id$          SHIFT id -> estado 5
$ 0 E 1 + 6 T 9 * 7 id 5    $            REDUCE F -> id
$ 0 E 1 + 6 T 9 * 7 F 10    $            REDUCE T -> T * F
$ 0 E 1 + 6 T 9             $            REDUCE E -> E + T
$ 0 E 1                     $            ACCEPT
```

Lendo as três ações: `SHIFT` desloca um item da entrada para a pilha, `REDUCE`
substitui uma sequência reconhecida pelo lado esquerdo de uma regra e `ACCEPT`
conclui a análise com apenas o símbolo inicial na pilha.

Trocando para a entrada inválida, o programa chega a uma configuração sem
entrada na tabela `ACTION` e emite `ERROR`.

### Comparação entre as duas direções

| | Descendente (estação 4) | Ascendente (estação 5) |
|---|---|---|
| **Ponto de partida** | símbolo inicial (`expr`) | tokens da entrada |
| **Direção** | do geral para os componentes menores | dos componentes menores para o símbolo inicial |
| **Mecanismo** | chamadas recursivas com *lookahead* | pilha com `SHIFT` e `REDUCE` guiados por tabela |
| **Recursão à esquerda** | inadequada | aceita naturalmente |

**Limite do experimento:** a tabela LR (`ACTION` e `GOTO`) já vem pronta dentro
do programa. A atividade observa o uso da tabela, não a sua construção.

---

## Conferência final

Os seis prints exigidos pelo roteiro:

| Arquivo | Deve mostrar |
|---|---|
| `01_tokens.png` | a entrada personalizada e a lista de tokens |
| `02_lexico.png` | palavra reservada, identificador e erro léxico |
| `03_erro_compilador.png` | a tentativa de compilação que falhou |
| `04_programa_corrigido.png` | a execução depois dos reparos |
| `05_descendente.png` | `expr`, `term` ou `factor` no rastreamento |
| `06_ascendente.png` | `PILHA`, `ENTRADA`, `ACAO` e `ACCEPT` |

Cada print traz a identificação visível, a alteração pedida na estação e o
console legível.

## Síntese

O analisador léxico transforma caracteres em tokens. O parser verifica se a
sequência de tokens obedece à gramática. Os rastreamentos e a pilha mostram que
as abordagens descendente e ascendente percorrem a mesma estrutura em direções
opostas e chegam ao mesmo veredito.

## Referências

- SEBESTA, R. W. *Conceitos de Linguagens de Programação*. 11. ed. Capítulo 4:
  análise léxica e sintática.
- Roteiro de aula exploratória prática, Capítulo 4, fornecido pelo professor.
