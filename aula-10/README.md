# Paradigmas de Linguagens de Programação: Atividade Aula 10

[← voltar ao índice do repositório](../README.md)

Laboratório de **concorrência**, baseado no capítulo 13 de Sebesta. O relatório é
um HTML que abre no navegador, com as respostas preenchidas e o código de cada
prática disponível para consulta.

| Etapa | Linguagem | Assunto |
|---|---|---|
| Preparação | — | Sincronização de cooperação × de competição |
| Prática 1 | Java | Condição de corrida: duas threads incrementando o mesmo contador |
| Prática 2 | Python | Todas as respostas possíveis para o mesmo programa |
| Prática 3 | Java | Corrigindo a corrida com sincronização |
| Prática 4 | — | Impasse (*deadlock*) |
| Prática 5 | Go | Mensagens em vez de memória compartilhada |
| Prática 6 | Rust | O compilador como guarda |
| Prática 7 | JavaScript | Uma thread só: o laço de eventos |
| Fechamento | — | Quem impede a corrida? |

O que a prática 1 mostra de forma mais direta: duas threads somando 1.000.000 cada
deveriam chegar a 2.000.000, mas as execuções deram 1.129.299, 1.920.411 e
1.898.195. A atualização se perde quando as duas threads leem o mesmo valor,
somam 1 e gravam o mesmo resultado — dois incrementos viram um só.

## Estrutura

```
.
├── README.md
└── laboratorio-concorrencia.html     # relatório do laboratório (abrir no navegador)
```
