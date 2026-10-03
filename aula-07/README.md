# Paradigmas de Linguagens de Programação: Atividade Aula 07

[← voltar ao índice do repositório](../README.md)

Resumo escrito sobre **expressões, atribuições e estruturas de controle**.

Pontos cobertos:

- **Precedência e associatividade** — a mesma expressão pode dar resultados
  diferentes dependendo da linguagem; em Python a exponenciação tem prioridade
  maior que o sinal negativo e associa da direita para a esquerda;
- **Sobrecarga de operadores** — em Java o `+` soma ou concatena, conforme os
  tipos envolvidos;
- **Conversões de tipo** — implícitas, feitas pela linguagem, ou explícitas, via
  cast; mesmo uma conversão para um tipo maior pode perder precisão;
- **Coerção em JavaScript** — `"5" - 2` dá `3`, mas `"5" + 2` dá `"52"`; por isso
  o `===` é mais seguro nas comparações;
- **Expressões relacionais e booleanas** — em C, `3 > 2 > 1` não se comporta como
  em Python, onde as comparações podem ser encadeadas;
- **Curto-circuito** — com `&&`, a segunda condição nem chega a ser avaliada se a
  primeira já for falsa, o que evita erros como acessar um método de um `null`;
- **Atribuição dentro de condição** — em C, trocar `==` por `=` compila e atribui
  em vez de comparar;
- **Estruturas de controle** — sequência, seleção (`if`, `switch`) e repetição
  (`for`, `while`); o *fall-through* do `switch` em C sem `break`; a diferença
  entre alterar a variável de controle do `for` em C e em Python com `range`; e
  `for...in` contra `for...of` em JavaScript.

A conclusão que ficou é que conhecer a sintaxe não basta: é preciso saber como a
linguagem trata precedência, conversões, comparações e avaliação, porque é daí
que vem boa parte dos erros.

## Estrutura

```
.
├── README.md
└── resumo-aula-07.pdf     # resumo completo da aula
```
