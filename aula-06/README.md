# Paradigmas de Linguagens de Programação: Atividade Aula 06

[← voltar ao índice do repositório](../README.md)

Exercício sobre **tipos de dados, verificação de tipos e representação numérica**.
Para cada programa, duas perguntas: (A) o que ele imprime e (B) em que momento o
erro é detectado — compilação, execução ou nunca.

A atividade roda o mesmo tipo de armadilha em seis linguagens, o que deixa claro
que o resultado depende menos do código e mais das regras de tipagem de cada uma.

| # | Linguagem | Saída | Erro detectado |
|---|---|---|---|
| 1 | JavaScript | `false` e `9007199254740992` | nunca |
| 2 | Python | `4 6` | não há erro |
| 3 | Go | `0` | nunca |
| 4 | Java | `0` e depois `ArrayIndexOutOfBoundsException` | em execução |
| 5 | Rust | não executa, porque não compila | em compilação |
| 6 | C | `1065353216` | nunca |

O contraste que eu achei mais interessante é entre Rust e C: o mesmo tipo de
problema é barrado pelo compilador em um e passa silenciosamente no outro,
produzindo um número que parece válido.

## Estrutura

```
.
├── README.md
└── exercicio-aula-06.pdf     # enunciados e respostas
```
