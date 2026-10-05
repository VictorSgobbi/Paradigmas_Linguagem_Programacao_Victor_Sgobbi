# Paradigmas de Linguagens de Programação: Atividade Aula 08

[← voltar ao índice do repositório](../README.md)

Atividade sobre **subprogramas: passagem de parâmetros, escopo e tempo de vida**.
Para cada programa, duas perguntas: (A) qual a saída e (B) qual conceito explica
o comportamento.

| # | Linguagem | Conceito identificado |
|---|---|---|
| 1 | Python | Parâmetro padrão mutável — a lista padrão é criada uma vez e reutilizada nas chamadas seguintes; envolve também passagem por atribuição |
| 2 | Java | Passagem por valor — o array é um objeto, então dá para alterar o conteúdo pela cópia da referência, enquanto o `int` é apenas copiado |
| 3 | Python | Fechamento (*closure*) — as lambdas capturam a variável `i`, não uma cópia do valor de cada repetição |
| 4 | C | Variável local estática — o `static` mantém o valor entre as chamadas da função |
| 5 | Rust | Passagem por posse (*move*) — o vetor é movido para a função, então não pode ser usado de novo depois da chamada |
| 6 | Python | Ambiente de referenciamento e escopo — como `total` recebe atribuição dentro da função, o Python o trata como variável local |

O fio que liga os seis casos é o mesmo: o resultado depende de **quando** e **a
que** o nome está vinculado, e não do que o código aparenta fazer na leitura.

## Estrutura

```
.
├── README.md
└── atividade-aula-08.pdf     # enunciados e respostas
```
