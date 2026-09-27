# SAPZ - Calculadora de Resistores

Calculadora de resistores desenvolvida em Python com Tkinter.

O projeto permite calcular o valor de uma resistência a partir das
cores das faixas do resistor e também encontrar as cores correspondentes
a partir de um valor de resistência.

## Sobre o projeto

O objetivo do projeto é facilitar a identificação de resistores através
de uma interface gráfica simples e visual.

A aplicação trabalha com:

- Código de cores de resistores
- Valor da resistência
- Multiplicadores
- Tolerância
- Representação visual do resistor
- Valores em Ω, kΩ, MΩ e GΩ

O programa possui dois modos de cálculo:

### Cores → Resistência

O usuário seleciona:

- Banda 1
- Banda 2
- Multiplicador
- Tolerância

A aplicação calcula o valor da resistência e mostra o resultado junto
com uma representação visual do resistor. :contentReference[oaicite:1]{index=1}

### Resistência → Cores

O usuário informa o valor da resistência e escolhe a tolerância.

O programa testa as combinações disponíveis de cores até encontrar uma
combinação correspondente ao valor informado. :contentReference[oaicite:2]{index=2}

## Tecnologias

- Python
- Tkinter
- ttk

## Interface

A interface foi desenvolvida utilizando componentes do Tkinter, como:

- `Frame`
- `Label`
- `Button`
- `Entry`
- `Combobox`
- `Radiobutton`
- `Canvas`

O `Canvas` é utilizado para desenhar o resistor e suas quatro faixas
de cores. :contentReference[oaicite:3]{index=3}

## Estrutura do funcionamento

O projeto utiliza tabelas para armazenar os valores das cores,
multiplicadores e tolerâncias.

```python
valores_cores = {
    "preto": 0,
    "marrom": 1,
    "vermelho": 2,
    "laranja": 3,
    "amarelo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "cinza": 8,
    "branco": 9
}
