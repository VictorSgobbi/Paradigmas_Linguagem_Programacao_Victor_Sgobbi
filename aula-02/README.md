# Paradigmas de Linguagens de Programação: Atividade Aula 02

[← voltar ao índice do repositório](../README.md)

Lista de exercícios: **Evolução das Principais Linguagens de Programação**, com
base no capítulo 2 de Sebesta (*Concepts of Programming Languages*).

10 questões autorais baseadas no capítulo 2; não reproduzem exercícios da
bibliografia.

## Estrutura do repositório

```
.
└── README.md     # este documento (enunciado + respostas)
```

---

## 1. Genealogia das linguagens

**Enunciado:** A genealogia das linguagens não é uma escada de progresso.
Explique essa afirmação e apresente dois fatores históricos que fazem uma
linguagem influenciar outra sem necessariamente substituí-la.

**Resposta:** A história das linguagens é uma árvore, não uma fila: ideias se
espalham, se combinam e coexistem. Fortran segue em uso na computação
científica e COBOL ainda roda sistemas bancários críticos, décadas depois de
surgirem alternativas. "Mais recente" não significa "substitui".

Dois fatores:

1. **Especialização por domínio.** Cada linguagem nasce resolvendo um problema
   específico (Fortran para cálculo numérico, COBOL para processamento
   comercial, Lisp para manipulação simbólica). Uma linguagem nova pode ser
   superior em geral e ainda assim não ser melhor *naquele* domínio.
2. **Custo de troca e base instalada.** Milhões de linhas de código, times
   treinados e ferramentas em torno de uma linguagem tornam a reescrita mais
   cara do que manter o sistema antigo.

*Objetivos: obj01, obj05 · Referência: Sebesta, cap. 2, páginas PDF 50, 51.*

---

## 2. Plankalkül

**Enunciado:** Plankalkül não foi implementada em sua época. Ainda assim, por
que ela é relevante para a história das linguagens? Cite três recursos
antecipados por seu projeto e explique o valor de um deles.

**Resposta:** Zuse projetou Plankalkül entre 1943 e 1945, mas ela só foi
implementada nos anos 2000. Sua relevância está em mostrar que o projeto de
linguagem é um problema conceitual, independente do hardware e da teoria de
compiladores disponíveis na época.

Três recursos antecipados:

- estruturas de dados em formato de **matriz/array**;
- estruturas de dados **hierárquicas** (registros aninhados, próximos do que
  hoje chamamos de `struct`);
- **invariantes/asserções** sobre os valores manipulados.

O valor das estruturas hierárquicas está em reconhecer, ainda nos anos 1940,
que dados reais têm partes relacionadas entre si. A ideia só reapareceu de
forma prática em COBOL (registros) e, depois, em C e nas linguagens orientadas
a objetos.

*Objetivos: obj01, obj02 · Referência: Sebesta, cap. 2, páginas PDF 52, 53.*

---

## 3. Fortran e a competição com código de máquina

**Enunciado:** Explique por que o projeto Fortran precisou convencer
programadores de que código traduzido podia competir com código de máquina
escrito à mão. Relacione desempenho, custo de programação e adoção.

**Resposta:** Nos anos 1950, tempo de computador era caro e escasso, enquanto
tempo de programador era comparativamente barato. Qualquer ineficiência gerada
por um tradutor automático era vista como economicamente inaceitável, e havia
desconfiança de que um compilador igualasse um programador experiente.

A equipe de Backus investiu pesado em otimizações no compilador (alocação de
registradores, otimização de laços) para chegar a poucos pontos percentuais do
código manual. Com isso, a comparação deixou de ser só velocidade de execução
e passou a ser **custo total**: tempo de máquina somado ao tempo de
programação e depuração. Fortran reduzia drasticamente o segundo sem sacrificar
o primeiro, e foi essa combinação que viabilizou a adoção de linguagens de
alto nível.

*Objetivos: obj01, obj02, obj04 · Referência: Sebesta, cap. 2, páginas PDF 56, 60.*

---

## 4. Lisp e Fortran: contextos diferentes

**Enunciado:** Lisp surgiu em um contexto diferente de Fortran. Compare os
domínios, a representação de dados e o estilo de computação favorecido pelas
duas linguagens.

**Resposta:**

| Aspecto | Fortran (1957) | Lisp (1958) |
|---|---|---|
| **Domínio** | Cálculo científico e de engenharia | Inteligência artificial, manipulação simbólica |
| **Representação de dados** | Vetores/matrizes numéricas, escalares com tipo fixo | Listas encadeadas (células *cons*) como estrutura universal, incluindo o próprio código |
| **Estilo favorecido** | Imperativo/iterativo, laços sobre arranjos numéricos | Funcional/recursivo, funções como valores |

Fortran nasceu para calcular fórmulas com eficiência sobre grandes volumes de
números. Lisp nasceu para representar e manipular símbolos, tratando programas
como dados (homoiconicidade), ideia essencial para pesquisa em IA e sem sentido
no domínio numérico do Fortran.

*Objetivos: obj02, obj03 · Referência: Sebesta, cap. 2, páginas PDF 61, 65.*

---

## 5. Contribuições de ALGOL 60

**Enunciado:** Avalie três contribuições de ALGOL 60 que ultrapassaram sua
adoção comercial. Por que uma linguagem pode ser muito influente sem dominar
o mercado?

**Resposta:** ALGOL 60 nunca teve adoção comercial ampla, mas deixou três
legados centrais:

1. **BNF (Backus-Naur Form)**, notação formal criada para descrever sua
   própria gramática e que virou o padrão para especificar sintaxe.
2. **Estrutura de blocos com escopo léxico**, base de praticamente toda
   linguagem imperativa posterior (Pascal, C e herdeiras).
3. **Estruturas de controle bem definidas** (`if`/`then`/`else`, laços) no
   lugar do `goto` indiscriminado, antecipando a programação estruturada.

A influência não depende do número de sistemas em produção, e sim de suas
ideias serem absorvidas pelas linguagens seguintes e de sua notação virar
vocabulário comum da área.

*Objetivos: obj02, obj04 · Referência: Sebesta, cap. 2, páginas PDF 66, 71.*

---

## 6. COBOL: domínio, público e FLOW-MATIC

**Enunciado:** COBOL foi desenhada para processamento comercial. Mostre como
domínio e público influenciaram sua legibilidade, seus registros e sua
relação com FLOW-MATIC.

**Resposta:** O comitê CODASYL projetou COBOL para ser lida também por
gestores e analistas de negócio. Daí a sintaxe verbosa e próxima do inglês
(`ADD A TO B GIVING C`), as divisões fixas e nomeadas (`IDENTIFICATION
DIVISION`, `DATA DIVISION`, `PROCEDURE DIVISION`) e os **registros
hierárquicos**, que espelham a forma como a empresa já organiza a informação
(um cadastro de cliente com campos e subcampos).

FLOW-MATIC, de Grace Hopper, já usava sintaxe baseada em inglês e era
orientada a arquivos comerciais. COBOL herdou essa filosofia e foi além ao ser
projetada por comitê para ser **padronizada entre fornecedores diferentes**,
algo que FLOW-MATIC, restrita à UNIVAC, não oferecia.

*Objetivos: obj01, obj02, obj04 · Referência: Sebesta, cap. 2, páginas PDF 72, 76.*

---

## 7. Ada: requisitos, confiabilidade e domínio crítico

**Enunciado:** Ada resultou de requisitos e projeto em grande escala. Analise
como confiabilidade, tipos, pacotes e concorrência se relacionam ao domínio
de sistemas críticos.

**Resposta:** Ada foi encomendada pelo Departamento de Defesa dos EUA para
unificar as linguagens usadas em sistemas embarcados e de missão crítica
(aviônica, armamentos, controle industrial). Cada decisão reflete esse domínio:

- **Confiabilidade**: verificações extensivas em compilação e tratamento de
  exceções nativo, porque falhas ali custam vidas, não reinicializações.
- **Tipos**: sistema estrito, com subtipos e faixas explícitas, impede que
  valores inválidos cheguem às variáveis em execução.
- **Pacotes**: encapsulamento e interfaces claras permitem que equipes grandes,
  muitas vezes de contratantes diferentes, integrem com previsibilidade.
- **Concorrência**: um modelo de tarefas (*rendezvous*) embutido na linguagem
  atende sensores, atuadores e temporizadores sem depender de soluções ad hoc
  de cada sistema operacional.

*Objetivos: obj02, obj04 · Referência: Sebesta, cap. 2, páginas PDF 94, 98.*

---

## 8. Objetos em Smalltalk, C++ e Java

**Enunciado:** Compare o papel dos objetos em Smalltalk, C++ e Java. Inclua
na resposta o compromisso de C++ com C e a estratégia de portabilidade de
Java.

**Resposta:**

- **Smalltalk**: objetos são o único conceito. Até inteiros e classes são
  objetos, toda comunicação é por passagem de mensagens e a tipagem é dinâmica.
  Mais que uma linguagem, é uma proposta de ambiente computacional (Alan Kay).
- **C++**: objetos são uma camada **opcional** sobre C, e código puramente
  procedural continua válido. É consequência do compromisso de Stroustrup com a
  compatibilidade com C, que atraiu a base existente ao preço de herdar a
  gestão manual de memória e a complexidade de C.
- **Java**: disciplina de objetos próxima de Smalltalk (herança simples,
  interfaces, nada fora de uma classe) com tipagem estática como C++. A
  diferença central é a **portabilidade**: compila para bytecode executado pela
  JVM, viabilizando "escreva uma vez, execute em qualquer lugar", problema que
  C++, compilado nativamente por plataforma, não endereça.

*Objetivos: obj02, obj03 · Referência: Sebesta, cap. 2, páginas PDF 98, 103.*

---

## 9. Perl, JavaScript, PHP, Python, Ruby e Lua

**Enunciado:** Compare Perl, JavaScript, PHP, Python, Ruby e Lua usando três
eixos: domínio inicial, estruturas de dados e estratégia de implementação.
Evite concluir que todas são iguais por serem chamadas de scripting.

**Resposta:**

| Linguagem | Domínio inicial | Estruturas de dados centrais | Estratégia de implementação |
|---|---|---|---|
| **Perl** | Texto e administração de sistemas Unix, scripts CGI | Escalares, arrays e hashes distinguidos por sigilos (`$`, `@`, `%`) | Interpretada, por muito tempo sem especificação formal |
| **JavaScript** | Scripts de cliente no navegador, manipulação do DOM | Objetos baseados em prototype e arrays dinâmicos | Interpretada na origem; motores modernos (V8) usam compilação *just-in-time* |
| **PHP** | Geração dinâmica de HTML no servidor | Um único tipo de array que serve como lista e mapa associativo ordenado | Interpretada por requisição no servidor Web, depois otimizada com cache de opcode e JIT |
| **Python** | Uso geral e ensino, hoje forte em ciência de dados | Listas, dicionários, tuplas e conjuntos embutidos | CPython interpreta bytecode em máquina virtual, com GIL |
| **Ruby** | Uso geral, popularizada na Web via Rails | Tudo é objeto, com arrays e hashes de métodos ricos | Interpretador MRI, com bytecode (YARV) desde a versão 1.9 |
| **Lua** | Scripting embutido em aplicações hospedeiras (jogos, software extensível) | Um único tipo *table*, que serve como array, mapa e objeto | Máquina virtual compacta, feita para inicialização rápida e pouca memória |

"Linguagem de scripting" é uma etiqueta ampla demais para significar algo
sozinha: os domínios de origem divergem, as estruturas de dados centrais também,
e as implementações vão de interpretadores simples a JITs de alta performance.

*Objetivos: obj01, obj03 · Referência: Sebesta, cap. 2, páginas PDF 107, 113.*

---

## 10. Estudo de caso: escolha de linguagens por domínio

**Enunciado:** Estudo de caso: uma equipe precisa escolher tecnologias para
cálculo científico, regras declarativas, aplicação Web interativa e firmware
restrito. Proponha famílias de linguagens, justifique historicamente cada
escolha e explicite dois trade-offs.

**Resposta:**

- **Cálculo científico** → família **Fortran**, incluindo seu ecossistema atual
  (Python com NumPy sobre LAPACK e BLAS). Desde 1957 essa família é otimizada
  para operações numéricas em larga escala, com décadas de bibliotecas já
  validadas.
- **Regras declarativas** → família **Prolog** e motores lógicos (Datalog). É a
  linhagem que desde os anos 1970 formaliza expressar "o que" é verdadeiro em
  vez de "como" calcular.
- **Aplicação Web interativa** → **JavaScript** no cliente com uma linguagem de
  servidor madura (Java ou Python). Desde os anos 1990, JavaScript é a única
  linguagem executada nativamente em todos os navegadores.
- **Firmware restrito** → **C**, ou **Ada** quando o sistema for crítico à
  segurança. C foi desenhada nos anos 1970 para controle fino de memória com
  baixíssimo overhead; Ada, nos anos 1980, para embarcados críticos com
  exigência de confiabilidade.

Dois trade-offs:

1. **Desempenho versus segurança.** C dá controle total de memória sem proteção
   automática; Ada troca parte dessa liberdade por garantias em compilação.
2. **Maturidade de ecossistema versus elegância.** Escolher Fortran ou C
   prioriza bibliotecas testadas em produção sobre a ergonomia de linguagens
   mais novas.

*Objetivos: obj01, obj02, obj03, obj04, obj05 · Referência: Sebesta, cap. 2, páginas PDF 49, 118.*

---

## Fontes

- Sebesta, Robert W. *Concepts of Programming Languages*, capítulo 2
  ("Evolution of the Major Programming Languages").
