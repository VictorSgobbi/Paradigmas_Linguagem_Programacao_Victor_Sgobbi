# Paradigmas de Linguagens de Programação: Atividade Aula 05

[← voltar ao índice do repositório](../README.md)

Lista de exercícios: **Nomes, Vinculações e Escopo**, com base no capítulo 5 de
Sebesta (*Conceitos de Linguagens de Programação*) e nos slides da aula.

A lista original traz 27 exercícios. Resolvi **7 deles, não consecutivos**, para
cobrir os blocos principais do capítulo sem repetir o mesmo tipo de questão:
nomes, apelidos, vinculação, tipagem dinâmica, armazenamento, ocultação e a
distinção entre escopo e tempo de vida.

| Exercício | Tema | Tipo de tarefa |
|---|---|---|
| 3 | Case sensitive | construir exemplo mínimo |
| 7 | Apelidos | analisar erro conceitual |
| 10 | Vinculação estática e dinâmica | explicar para um colega |
| 13 | Vinculação de tipos dinâmica | construir exemplo mínimo |
| 16 | Variáveis dinâmicas da pilha | aplicar a exemplo pequeno |
| 21 | Ocultação de nomes | aplicar a exemplo pequeno |
| 25 | Escopo e tempo de vida | explicar para um colega |

## Estrutura do repositório

```
.
└── README.md     # este documento (enunciados + respostas)
```

---

## 3. Case sensitive

**Enunciado:** Construa um exemplo mínimo que demonstre "Case sensitive".
Identifique a situação observada, a aplicação do conceito e a conclusão
esperada.

**Situação observada:** em Java — como em toda linguagem baseada em C — os nomes
são *case sensitive*. O exemplo abaixo compila e executa sem nenhum aviso:

```java
public class Contador {
    public static void main(String[] args) {
        int total = 10;
        int Total = 20;
        int TOTAL = 30;

        System.out.println(total + Total + TOTAL);  // 60
    }
}
```

**Aplicação do conceito:** maiúsculas e minúsculas são caracteres distintos na
formação do nome, então `total`, `Total` e `TOTAL` são **três variáveis
diferentes**, cada uma com seu próprio endereço e valor. Não há redeclaração e
não há erro: para o compilador são três entidades sem relação entre si.

**Conclusão esperada:** a sensibilidade a maiúsculas é uma decisão de projeto
com saldo dividido. Ela **favorece a capacidade de escrita** — amplia o espaço
de nomes e viabiliza convenções úteis, como as classes em *PascalCase* do tipo
`IndexOutOfBoundsException` — e **prejudica a legibilidade**, porque nomes
visualmente quase idênticos designam coisas diferentes e o compilador não tem
como avisar que `Total` era provavelmente um erro de digitação de `total`. Em
uma linguagem não sensível a maiúsculas, a segunda declaração seria recusada
como redeclaração, e o erro apareceria em tempo de compilação.

---

## 7. Apelidos

**Enunciado:** Analise o erro conceitual: alguém tratou "Apelidos" como uma
etapa isolada, sem relação com os objetivos ou com os demais conceitos. Explique
o problema e reescreva a conclusão.

**O erro:** tratar apelido (*alias*) como uma curiosidade da linguagem — "dois
nomes que apontam para a mesma coisa" — e parar aí, como se fosse um detalhe de
sintaxe sem consequência. Quem conclui assim perde a razão pela qual o assunto
aparece no capítulo.

**Por que está errado:** apelido não é um tópico solto, é uma **consequência
direta do atributo endereço**. Duas variáveis são apelidos quando seus nomes
estão vinculados ao **mesmo endereço de memória** — ou seja, o conceito só
existe porque a variável é uma sêxtupla e o endereço é um dos seis atributos.
A partir daí ele se conecta a pelo menos três outros pontos:

- **Com o capítulo 1:** apelidos são um **prejuízo à legibilidade e à
  confiabilidade**. Ler uma atribuição a `x` deixa de ser suficiente para saber
  quais valores mudaram, porque outro nome pode ter sido alterado junto.
- **Com as variáveis dinâmicas do heap:** ponteiros e variáveis de referência
  são o mecanismo que mais produz apelidos, já que o heap só é acessível
  através deles.
- **Com o projeto da linguagem:** restringir apelidos é uma decisão consciente
  de projeto. Java elimina a aritmética de ponteiros justamente para limitar o
  problema.

Exemplo mínimo em C, onde `x` muda sem que o nome `x` apareça na atribuição:

```c
int x = 5;
int *p = &x;   /* p e x passam a referenciar o mesmo endereço */

*p = 99;
printf("%d\n", x);   /* imprime 99 */
```

**Conclusão reescrita:** apelidos são dois ou mais nomes vinculados ao mesmo
endereço de memória. Não são um detalhe isolado, e sim o ponto em que o atributo
**endereço** produz efeito visível sobre os critérios de avaliação da linguagem:
como qualquer um dos nomes pode alterar o valor observado pelos outros, o
programa fica mais difícil de ler e mais difícil de verificar. Por isso o
projeto de uma linguagem trata apelidos como algo a ser **restringido**, e não
como recurso a ser oferecido livremente.

---

## 10. Vinculação estática e dinâmica

**Enunciado:** Explique "Vinculação estática e dinâmica" para um colega usando
uma definição, um exemplo autoral e uma relação com outro conceito da aula.

**Definição:** vinculação é a associação entre um atributo e uma entidade — por
exemplo, entre uma variável e seu tipo. Ela é **estática** quando ocorre
**antes do tempo de execução** e permanece inalterada durante toda a execução;
é **dinâmica** quando ocorre **durante a execução**, ou quando pode mudar ao
longo dela.

**Exemplo:** as duas linhas abaixo fazem a mesma coisa aos olhos de quem lê, mas
vinculam o tipo em momentos diferentes.

```java
// Java — vinculação de tipo ESTÁTICA, feita em tempo de compilação
int medida = 40;
medida = "quarenta";   // erro de compilação: o tipo de medida é int e não muda
```

```javascript
// JavaScript — vinculação de tipo DINÂMICA, refeita a cada atribuição
let medida = 40;       // neste ponto, medida é number
medida = "quarenta";   // agora medida é string, sem erro nenhum
```

Em Java o tipo de `medida` é decidido na compilação e vale para o programa
inteiro; o erro aparece antes de o programa rodar. Em JavaScript o tipo é um
atributo da variável **naquele instante da execução**, redefinido a cada
atribuição, e a troca simplesmente acontece.

**Relação com outro conceito da aula:** isso é o mesmo eixo que organiza os
**tempos de vinculação**. Quanto mais cedo a vinculação acontece — projeto da
linguagem, implementação, compilação, carga — mais estática ela é e mais o
compilador consegue verificar e otimizar; quanto mais tarde — execução —, mais
flexível e mais cara ela fica. O compromisso é sempre o mesmo par:
**eficiência e detecção antecipada de erros** de um lado, **flexibilidade** do
outro. É exatamente o que reaparece nas categorias por tempo de vida, onde a
variável estática é vinculada à memória antes da execução e a dinâmica da pilha
só na elaboração da declaração.

---

## 13. Vinculação de tipos dinâmica

**Enunciado:** Construa um exemplo mínimo que demonstre "Vinculação de Tipos
Dinâmica". Identifique a situação observada, a aplicação do conceito e a
conclusão esperada.

**Situação observada:** em JavaScript, o tipo não é declarado nem fixado — ele é
determinado pela atribuição. A mesma variável muda de tipo entre duas linhas
consecutivas:

```javascript
let lista = [2, 4.33, 6, 8];
console.log(typeof lista, lista.length);   // object 4

lista = 17.3;
console.log(typeof lista, lista.length);   // number undefined
```

**Aplicação do conceito:** a vinculação de tipo é **especificada pela sentença
de atribuição**. Na primeira linha `lista` é vinculada ao tipo array; na
terceira, a mesma variável passa a ser vinculada ao tipo numérico. Nenhuma
declaração precisou ser alterada, e nada é verificado antes da execução. Note
que `lista.length` deixa de fazer sentido e passa a devolver `undefined`, em vez
de provocar um erro — o interpretador aceita a operação e segue.

**Conclusão esperada:** a tipagem dinâmica troca verificação por flexibilidade.
A **vantagem** é permitir código genérico, que opera sobre qualquer tipo sem
sobrecarga de declarações. As **desvantagens** são três e todas relevantes:
o erro de tipo deixa de ser detectado em compilação e só aparece em execução —
ou, pior, **não aparece**, como no `undefined` acima, e se propaga
silenciosamente; a checagem precisa ser feita em tempo de execução, o que
**custa desempenho**; e a linguagem geralmente exige um interpretador, já que o
tipo só é conhecido quando a atribuição acontece. Comparado ao exemplo do
exercício 10, é o mesmo compromisso visto do lado oposto: aqui se ganha
liberdade e se perde a rede de segurança do compilador.

---

## 16. Variáveis dinâmicas da pilha

**Enunciado:** Aplique "Variáveis dinâmicas da pilha" a um exemplo autoral
pequeno. Descreva o contexto, a decisão tomada e a consequência esperada.

**Contexto:** preciso de uma função que calcule o fatorial de um número por
recursão. Cada chamada precisa lembrar qual é o **seu** `n` enquanto espera o
resultado da chamada seguinte.

```c
int fatorial(int n) {
    int resultado;          /* variável dinâmica da pilha */

    if (n <= 1) {
        resultado = 1;
    } else {
        resultado = n * fatorial(n - 1);
    }

    return resultado;
}
```

**Decisão tomada:** declarar `n` e `resultado` como **variáveis locais comuns**,
sem `static`. Com isso elas se tornam variáveis dinâmicas da pilha: o vínculo
com o armazenamento é criado quando a declaração é **elaborada** — isto é,
quando a execução chega nela —, e desfeito no retorno da função. O tipo continua
vinculado estaticamente, em tempo de compilação; o que é dinâmico aqui é apenas
o **armazenamento**.

**Consequência esperada:** em `fatorial(4)` existem quatro ativações vivas ao
mesmo tempo, e cada uma recebe um **registro de ativação próprio** na pilha.
Logo, existem quatro `n` e quatro `resultado` simultâneos, em endereços
diferentes, sem interferência entre si — é isso que torna a recursão possível.
O preço é o **custo de alocação e desalocação a cada chamada** e o fato de a
variável não conservar valor entre ativações. Se eu tivesse declarado
`static int resultado`, a variável passaria à categoria estática: um único
endereço para todas as chamadas, mais eficiente, porém compartilhado entre as
ativações — o que quebraria a recursão.

---

## 21. Ocultação de nomes

**Enunciado:** Aplique "Ocultação de nomes" a um exemplo autoral pequeno.
Descreva o contexto, a decisão tomada e a consequência esperada.

**Contexto:** estou dentro de uma função em C que já usa a variável `count`
para contar registros processados, e preciso de um contador auxiliar dentro de
um laço interno.

```c
void processar(void) {
    int count = 0;              /* conta registros processados */

    while (temRegistro()) {
        int count = 0;          /* OCULTA a variável externa */

        while (temCampo()) {
            count++;            /* incrementa a INTERNA */
        }
        printf("campos: %d\n", count);
    }

    printf("registros: %d\n", count);   /* sempre 0 */
}
```

**Decisão tomada:** declarar o contador auxiliar com o mesmo nome `count` dentro
do bloco do `while`. Como C permite criar escopo estático com blocos aninhados,
a declaração interna é legal e cria uma **nova variável**, que **oculta** a
externa dentro daquele bloco.

**Consequência esperada:** toda referência a `count` dentro do laço se conecta à
declaração **mais próxima** — a interna. A externa continua existindo e viva,
apenas ficou **invisível** ali: ela foi escondida, não substituída nem apagada.
O resultado é o bug silencioso da última linha: `registros` imprime `0`, porque
o `count++` nunca tocou a variável externa. Nenhum erro é emitido, já que o
código é perfeitamente válido.

Vale registrar que essa validade depende da linguagem: o mesmo código é aceito
em **C e C++**, mas **rejeitado em Java e C#**, que proíbem declarar uma local
com o nome de outra local ainda em escopo justamente para evitar esse tipo de
engano. A lição prática é que ocultação é um recurso legítimo do escopo
estático, mas **reusar o nome custa legibilidade** — nomear o contador interno
como `campos` teria eliminado o problema por completo.

---

## 25. Escopo e tempo de vida

**Enunciado:** Explique "Escopo e tempo de vida" para um colega usando uma
definição, um exemplo autoral e uma relação com outro conceito da aula.

**Definição:** são dois atributos parecidos e independentes. **Escopo** é a
faixa de sentenças na qual a variável é **visível**, ou seja, onde o nome dela
pode ser usado. **Tempo de vida** é o intervalo em que a variável está
**vinculada a uma posição de memória**, exista ou não algum lugar de onde se
possa chamá-la pelo nome. Um trata de *visibilidade*, o outro de *existência*.

**Exemplo:** o caso que separa os dois conceitos de forma mais limpa é a local
estática.

```c
void imprimirCabecalho(void) {
    printf("--- relatorio ---\n");
    /* aqui 'chamadas' NÃO é visível: está fora do escopo... */
    /* ...mas continua existindo na memória, com o valor preservado */
}

void gerar(void) {
    static int chamadas = 0;    /* escopo: gerar()  |  vida: o programa inteiro */

    chamadas++;
    imprimirCabecalho();
    printf("geracao numero %d\n", chamadas);
}
```

O **escopo** de `chamadas` é apenas o corpo de `gerar()` — nenhuma outra função
consegue citar esse nome. Já o **tempo de vida** é o do programa inteiro: a
variável é vinculada à memória em tempo de carga e permanece no mesmo endereço
até o fim. Por isso, ao chamar `gerar()` três vezes, ela imprime 1, 2 e 3 em vez
de 1, 1 e 1. Enquanto `imprimirCabecalho()` executa, `chamadas` está **viva e
invisível** ao mesmo tempo — que é exatamente a prova de que os dois conceitos
não coincidem.

**Relação com outro conceito da aula:** a distinção só fica clara quando se
cruza escopo com as **categorias por tempo de vida**. Uma variável dinâmica da
pilha, como no exercício 16, tem escopo e tempo de vida praticamente
sobrepostos — nasce na elaboração da declaração e morre no retorno —, e é
justamente essa coincidência que faz muita gente achar que os termos são
sinônimos. Bastou trocar a categoria para estática, sem mexer no escopo, para os
dois se descolarem. O escopo é decidido pela **estrutura textual** do programa;
o tempo de vida, pela **categoria de armazenamento**. São eixos diferentes, e é
por isso que o capítulo os apresenta como atributos separados da sêxtupla.

---

## Fontes

- SEBESTA, R. W. *Conceitos de Linguagens de Programação*. 11. ed. Capítulo 5:
  nomes, vinculações e escopo (p. 215–243).
- Slides da aula 05 (capítulo 5), disponibilizados pelo professor.
- Lista de exercícios autorais da aula 05 — exercícios 3, 7, 10, 13, 16, 21 e 25.
