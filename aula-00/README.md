# Paradigmas de Linguagens de Programação: Atividade — Aula 00

[← voltar ao índice do repositório](../README.md)

Atividade prática da disciplina de **Paradigmas de Linguagens de Programação**.
Linguagem sorteada para o grupo: **Python**.

## Enunciado

1. Rodar o "Olá, mundo!" num compilador online (ex.: [onecompiler.com](https://onecompiler.com/python));
2. Alterar o programa para receber um número e mostrar a tabuada desse número;
3. Descobrir: 1 vaga real + faixa salarial + paradigma(s) da linguagem;
4. Publicar no GitHub da disciplina.

## Estrutura do repositório

```
.
├── README.md            # este documento (respostas da pesquisa)
└── src/
    ├── ola_mundo.py     # passo 1 — "Olá, mundo!"
    └── tabuada.py       # passo 2 — lê um número e imprime a tabuada
```

## Como executar

### No compilador online (onecompiler)

1. Acesse <https://onecompiler.com/python>;
2. Cole o conteúdo de [src/tabuada.py](src/tabuada.py) no editor;
3. Abra a aba **STDIN** e digite o número desejado (ex.: `7`);
4. Clique em **Run**.

> A aba STDIN é necessária porque o programa usa `input()`. Se ela ficar vazia,
> o `input()` não tem o que ler e a execução termina com erro.

### Localmente

```bash
python3 src/ola_mundo.py
python3 src/tabuada.py
```

Não há dependências externas, apenas Python 3 (testado no Python 3.12.3).

---

## Passo 1 - "Olá, mundo!"

```python
print("Olá, mundo!")
```

Saída:

```
Olá, mundo!
```

Em Python o "Olá, mundo!" é uma única linha: não existe classe obrigatória,
função `main` obrigatória, nem declaração de tipos.

## Passo 2 - Tabuada

Código completo de [src/tabuada.py](src/tabuada.py):

```python
numero = int(input("Digite um número inteiro: "))

print(f"\nTabuada do {numero}:")
for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
```

São três instruções: ler a entrada, anunciar a tabuada e repetir a multiplicação
de 1 a 10. O `range(1, 11)` vai até 10 porque o limite superior em Python é
exclusivo.

Exemplo de execução com a entrada `7`:

```
Digite um número inteiro: 7

Tabuada do 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

> O programa assume que a entrada é um número inteiro. Se for digitado texto
> (`abc`), o `int()` levanta `ValueError` e a execução para, comportamento
> esperado para o escopo desta atividade.

---

## Passo 3 - Pesquisa

### 3.1 Vaga real

| Campo | Informação |
|---|---|
| **Cargo** | Workload Automation (WLA) Senior Analyst — vaga nº 35082 |
| **Empresa** | Bosch Group (Robert Bosch Ltda.) |
| **Local** | Campinas — SP (Av. Robert Bosch, Parque Via Norte) |
| **Modelo** | Híbrido (3 dias por semana presencial) |
| **Situação** | Aberta na data da consulta (04/08/2026) |
| **Link** | [jobs.smartrecruiters.com/BoschGroup/...wla-senior-analyst-35082](https://jobs.smartrecruiters.com/BoschGroup/744000139335779-workload-automation-wla-senior-analyst-35082) |

**Onde Python entra:** entre os requisitos técnicos está explicitamente
*"Scripting and automation (Shell Script, PowerShell, and **Python**)"*. A vaga
usa Python como linguagem de automação e integração, um dos usos mais comuns
da linguagem no mercado corporativo, ao lado de dados e web.

**Outros requisitos da vaga:** ensino superior completo, inglês fluente,
plataformas Automic (UC4) e Redwood, administração de bancos de dados (Oracle,
SQL Server, PostgreSQL), administração de Linux/Unix e Windows, fundamentos de
redes (TCP/IP, firewalls) e disponibilidade para escala de plantão.

**Benefícios citados:** plano de saúde, horário flexível, participação nos
lucros, previdência privada, seguro de vida, clube da empresa, licença
maternidade estendida (180 dias), subsídio para estudos e bônus anual.

### 3.2 Faixa salarial

A vaga da Bosch **não divulga o salário**, o que é a regra, e não a exceção,
no mercado brasileiro de TI. Por isso a faixa abaixo vem de dados agregados de
mercado (Glassdoor, Indeed e Python Brasil), consultados em 04/08/2026:

| Senioridade | Faixa mensal (CLT) | Referência |
|---|---|---|
| Júnior (até ~2 anos) | R$ 3.000 – R$ 6.000 | mediana ≈ R$ 3.665 |
| Pleno | R$ 6.000 – R$ 10.000 | média ≈ R$ 9.723; 90º percentil ≈ R$ 15.000 |
| **Sênior** (nível da vaga acima) | **R$ 10.000 – R$ 16.000** | mediana ≈ R$ 10.679 |

Média geral para "Desenvolvedor Python" no Brasil: **R$ 4.583/mês**, com faixa
típica de R$ 2.908 (25º percentil) a R$ 8.717 (75º percentil).

Observações que explicam a variação:

- **Região:** São Paulo e Florianópolis pagam de 15% a 30% acima da média nacional;
- **Nicho:** IA, dados e fintechs pagam acima da faixa; vagas remotas
  internacionais podem passar de R$ 20.000/mês ou serem pagas em dólar;
- **Regime:** valores PJ tendem a ser mais altos que CLT em termos brutos,
  porque não incluem os encargos e benefícios.

### 3.3 Paradigmas do Python

Python é uma linguagem **multiparadigma**: ela não obriga o programador a
escolher um único estilo e permite misturá-los no mesmo arquivo.

| Paradigma | Suporte | Como aparece na linguagem |
|---|---|---|
| **Imperativo / Procedural** | Nativo e principal | Sequência de comandos, atribuição, `if`/`for`/`while`, funções com `def` |
| **Orientado a objetos** | Nativo e completo | `class`, herança (inclusive múltipla), encapsulamento por convenção, polimorfismo, *duck typing*; **tudo em Python é objeto** — até funções e classes |
| **Funcional** | Parcial | Funções de primeira classe e de alta ordem, `lambda`, `map`/`filter`, `functools` (`reduce`, `partial`), *closures*, compreensões de lista, decoradores |
| **Reflexivo / Metaprogramação** | Nativo | `getattr`, `setattr`, `type()` dinâmico, metaclasses, decoradores |

Características de implementação que também classificam a linguagem:

- **Interpretada** (bytecode executado pela CPython) e de **alto nível**;
- **Tipagem dinâmica e forte**, o tipo é verificado em tempo de execução, mas
  não há coerção silenciosa entre tipos incompatíveis (`1 + "1"` é erro);
- **Gerenciamento automático de memória** (contagem de referências + coletor de ciclos);
- **Anotações de tipo opcionais** (`def f(x: int) -> str`), usadas por
  ferramentas externas como o *mypy*, não são verificadas em tempo de execução.

**Por que Python não é puramente funcional:** ele permite efeitos colaterais e
estado mutável livremente, não garante funções puras, não tem otimização de
recursão de cauda e limita a recursão (~1000 níveis por padrão). Ou seja: dá
para *programar em estilo* funcional, mas a linguagem não *impõe* isso.

#### Qual paradigma usamos no exercício

A tabuada deste repositório é **imperativa**: uma sequência de comandos com um
laço `for` que descreve *como* chegar ao resultado, passo a passo. É o estilo
mais direto em Python e o mais comum para programas pequenos.

O mesmo problema poderia ser resolvido em estilo funcional (`map` sobre um
`range`, sem laço nem variável de controle) ou orientado a objetos (uma classe
`Tabuada` guardando o número e um método para gerar as linhas). O resultado
seria idêntico, e é justamente esse o ponto do multiparadigma: a escolha entre
os estilos é de legibilidade e manutenção, não de possibilidade.

---

## Fontes

Vaga:

- [Bosch Group — Workload Automation (WLA) Senior Analyst, Campinas/SP](https://jobs.smartrecruiters.com/BoschGroup/744000139335779-workload-automation-wla-senior-analyst-35082)
- [Vagas de Python no Brasil — Python Brasil](https://python.dev.br/vagas/)

Faixa salarial:

- [Glassdoor — Salário: Desenvolvedor Python (Brasil)](https://www.glassdoor.com.br/Sal%C3%A1rios/desenvolvedor-python-sal%C3%A1rio-SRCH_KO0,20.htm)
- [Glassdoor — Salário: Desenvolvedor Python Sênior](https://www.glassdoor.com.br/Sal%C3%A1rios/desenvolvedor-python-s%C3%AAnior-sal%C3%A1rio-SRCH_KO0,27.htm)
- [Indeed — Salário de Python no Brasil](https://br.indeed.com/career/python/salaries)
- [Python Brasil — Salário Desenvolvedor Python 2026: Júnior, Pleno e Sênior](https://python.dev.br/carreira/salarios-python-brasil/)

Linguagem e paradigmas:

- [Python.org — What is Python? Executive Summary](https://www.python.org/doc/essays/blurb/)
- [Python Docs — Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)

> Dados de vaga e salário consultados em **04/08/2026**. Anúncios de emprego
> expiram: o link acima pode sair do ar depois dessa data.
