# Paradigmas de Linguagens de Programação

Aqui eu vou guardando as atividades da disciplina, uma pasta por aula. Cada
`aula-NN/` tem o próprio README com o enunciado, o caminho que eu segui pra
resolver, as respostas e o código, quando a atividade tem código.

👤 **Aluno:** Victor Hugo Pacchioni Sgobbi  
🎓 **RA:** 24000732-2

---

## As atividades

### [`aula-00`](aula-00/README.md) · "Olá, mundo!" e tabuada em Python

Primeira atividade da matéria. A linguagem que caiu pro meu grupo foi
**Python**, então comecei rodando o `hello world` de sempre num compilador
online e depois fui mexendo nele até ler um número do teclado e imprimir a
tabuada desse número. A parte que eu achei mais legal nem foi o código: também
tinha que caçar uma vaga de verdade pedindo Python, ver a faixa salarial que
estavam pagando e descobrir quais paradigmas a linguagem suporta.

📁 Código em [`aula-00/src/`](aula-00/src) — [`ola_mundo.py`](aula-00/src/ola_mundo.py) e [`tabuada.py`](aula-00/src/tabuada.py)

### [`aula-02`](aula-02/README.md) · Evolução das principais linguagens

Lista de exercícios em cima do capítulo 2 do Sebesta, que é o de história das
linguagens. Respondi 10 questões, cada uma com o enunciado e a minha resposta
logo embaixo. Passa por Plankalkül, Fortran, Lisp, ALGOL 60, COBOL, Ada, a
chegada da orientação a objetos e as linguagens de script, e fecha com um estudo
de caso de escolher linguagem de acordo com o domínio. A ideia que mais ficou
comigo foi essa: linguagem nova não mata linguagem velha, elas convivem.

### [`aula-03`](aula-03/README.md) · Derivação de código a partir da gramática

Nessa a gente tinha que pegar a gramática formal de uma linguagem de verdade e
derivar um trecho de código a partir dela. Fiquei com Python e fui atrás da
gramática do CPython, que usa notação **PEG** desde a versão 3.9. Separei só as
produções que eu ia precisar e derivei `total = 2 + 3 * 4` passo a passo, até
sobrar só terminal. Dá um trabalho danado, mas foi o que fez cair a ficha sobre
o que é terminal, não terminal, produção e derivação.

### [`aula-04`](aula-04/README.md) · Análise léxica e sintática em Java

Aula exploratória no laboratório: 60 minutos divididos em 5 estações, tudo em
Java. Em cada estação eu rodava um programa curto que deixa à vista uma etapa
que normalmente fica escondida dentro do compilador — separar lexema de token,
reconhecer palavra reservada, quebrar o código de propósito só pra ver do que o
compilador reclama, e acompanhar o rastro de um parser descendente recursivo e
de um ascendente com tabela `ACTION`/`GOTO`. No README da pasta eu registrei o
que saiu em cada estação.

### [`aula-06`](aula-06/README.md) · Tipos, verificação de tipos e representação numérica

Exercício com seis linguagens — JavaScript, Python, Go, Java, Rust e C — em que
eu tinha que dizer o que cada programa imprime e em que momento o erro aparece:
na compilação, na execução ou nunca. O contraste que mais me chamou atenção foi
entre Rust e C: o mesmo problema é barrado pelo compilador em um e passa batido
no outro, devolvendo um número que parece válido.

### [`aula-07`](aula-07/README.md) · Expressões, atribuições e estruturas de controle

Resumo escrito da aula, passando por precedência e associatividade, sobrecarga
de operadores, conversões implícitas e explícitas, curto-circuito, atribuição
dentro de condição e as estruturas de seleção e repetição. A ideia que sobrou é
que saber a sintaxe não basta: é o jeito como cada linguagem avalia a expressão
que gera a maior parte dos erros.

### [`aula-08`](aula-08/README.md) · Subprogramas: passagem de parâmetros e escopo

Seis programas em Python, Java, C e Rust, cada um para eu dizer a saída e
identificar o conceito por trás: parâmetro padrão mutável, passagem por valor,
fechamento, variável local estática, passagem por posse e ambiente de
referenciamento. Todos caem no mesmo ponto — o que vale é a que o nome está
vinculado, e não o que o código aparenta fazer.

### [`aula-10`](aula-10/README.md) · Laboratório de concorrência

Laboratório em cima do capítulo 13, com sete práticas em Java, Python, Go, Rust
e JavaScript: condição de corrida, correção por sincronização, impasse, troca de
mensagens no lugar de memória compartilhada e o laço de eventos. Na prática 1,
duas threads que deveriam somar 2.000.000 fecharam em 1.129.299, 1.920.411 e
1.898.195 — a corrida aparecendo na prática.

---

## Material do professor

🔗 **Munif** — <https://drive.google.com/drive/folders/1Inoq29Xxfmu5fDI6JOY9EFvjdDZxQtwt?usp=sharing>

📝 **Dontpad da aula** — <https://dontpad.com/munifaula>

---

## Como este repositório é organizado

```
.
├── README.md          ← você está aqui: índice geral
├── aula-00/
│   ├── README.md      ← enunciado, respostas da pesquisa e instruções
│   └── src/           ← código-fonte da atividade
├── aula-02/README.md
├── aula-03/README.md
├── aula-04/README.md
├── aula-06/
├── aula-07/
├── aula-08/
├── aula-10/
├── conteudo-das-aulas/    ← slides, roteiros e exercícios do professor
└── revisao-para-prova/    ← material da Prova 01 + meu guia de estudo
```
