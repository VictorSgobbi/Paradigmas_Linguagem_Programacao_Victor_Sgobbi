# Paradigmas de Linguagens de Programação

Caderno de atividades da disciplina, mantido aula a aula. Cada entrega vive em
uma pasta própria (`aula-NN/`) com um README autocontido: enunciado, raciocínio,
respostas e, quando existe, o código-fonte.

| | |
|---|---|
| **Aluno** | Victor Hugo Pacchioni Sgobbi |
| **RA** | 24000732-2 |
| **Bibliografia base** | SEBESTA, R. W. *Conceitos de Linguagens de Programação*, 11. ed. |
| **Linguagens usadas até aqui** | Python, Java |

---

## Progresso

- [x] **Aula 00** — Primeiro programa e pesquisa de mercado
- [x] **Aula 02** — Evolução das linguagens (cap. 2)
- [x] **Aula 03** — Derivação a partir da gramática
- [x] **Aula 04** — Análise léxica e sintática (cap. 4)

---

## As atividades

### [`aula-00`](aula-00/README.md) · "Olá, mundo!" e tabuada em Python

Primeiro contato com a linguagem sorteada para o grupo (**Python**): rodar um
`hello world` em compilador online, evoluí-lo para imprimir a tabuada de um
número lido do teclado e pesquisar uma vaga real, a faixa salarial praticada e
os paradigmas que a linguagem suporta.

📁 Código em [`aula-00/src/`](aula-00/src) — [`ola_mundo.py`](aula-00/src/ola_mundo.py) e [`tabuada.py`](aula-00/src/tabuada.py)

### [`aula-02`](aula-02/README.md) · Evolução das principais linguagens

10 questões autorais sobre o capítulo 2 de Sebesta, com enunciado e resposta
lado a lado: genealogia das linguagens, Plankalkül, Fortran, Lisp, ALGOL 60,
COBOL, Ada, a chegada dos objetos, as linguagens de script e um estudo de caso
sobre escolha de linguagem por domínio.

### [`aula-03`](aula-03/README.md) · Derivação de código a partir da gramática

Estudo da gramática formal do CPython (notação **PEG**, adotada a partir do
Python 3.9): seleção das regras de produção relevantes e derivação passo a passo
da instrução `total = 2 + 3 * 4`, amarrando os conceitos de terminal, não
terminal, produção e derivação.

### [`aula-04`](aula-04/README.md) · Análise léxica e sintática em Java

Aula exploratória de 60 minutos dividida em 5 estações, em Java: separar lexemas
de tokens, reconhecer palavras reservadas, ler os diagnósticos do compilador
diante de erros propositais e acompanhar o rastreamento de um parser descendente
recursivo e de um parser ascendente com tabela `ACTION`/`GOTO`.

---

## Rodando o código

Só a aula 00 tem código executável versionado. Com Python 3 instalado:

```bash
python aula-00/src/ola_mundo.py
python aula-00/src/tabuada.py
```

Sem instalar nada, cole o conteúdo dos arquivos em <https://onecompiler.com/python>.

Os programas da aula 04 foram escritos e executados no laboratório da faculdade;
o registro escrito de cada estação está no README daquela pasta.

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
└── aula-04/README.md
```

Convenções adotadas:

- uma pasta por aula, nomeada `aula-NN` com dois dígitos;
- todo README de atividade começa com um link de volta para este índice;
- código-fonte sempre em `src/` dentro da pasta da aula;
- um commit por atividade, prefixado pela aula a que se refere.
