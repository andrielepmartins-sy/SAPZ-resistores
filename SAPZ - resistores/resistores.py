from tkinter import *
from tkinter import ttk


# Tabelas das cores
# Valores usados nos calculos

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


multiplicadores = {
    "preto": 1,
    "marrom": 10,
    "vermelho": 100,
    "laranja": 1000,
    "amarelo": 10000,
    "verde": 100000,
    "azul": 1000000,
    "violeta": 10000000,
    "cinza": 100000000,
    "branco": 1000000000,
    "ouro": 0.1,
    "prata": 0.01
}


tolerancias = {
    "marrom": 1,
    "vermelho": 2,
    "verde": 0.5,
    "azul": 0.25,
    "violeta": 0.1,
    "cinza": 0.05,
    "ouro": 5,
    "prata": 10
}


# Cores usadas no desenho
cores_visuais = {
    "preto": "black",
    "marrom": "#8B4513",
    "vermelho": "#E53935",
    "laranja": "#FF8C00",
    "amarelo": "#FFD700",
    "verde": "#2E8B57",
    "azul": "#1976D2",
    "violeta": "#8E44AD",
    "cinza": "#808080",
    "branco": "white",
    "ouro": "#D4AF37",
    "prata": "#C0C0C0"
}


# Formata o resultado
# Mostra o valor em Ω, kΩ, MΩ ou GΩ

def formatar_resistencia(valor):

    if valor >= 1000000000:
        return f"{valor / 1000000000:g} GΩ"

    elif valor >= 1000000:
        return f"{valor / 1000000:g} MΩ"

    elif valor >= 1000:
        return f"{valor / 1000:g} kΩ"

    else:
        return f"{valor:g} Ω"


# Desenha o resistor
# Desenho feito com o Canvas

def desenhar_resistor(cor1, cor2, cor3, cor4):

    canvas.delete("all")


    # Fios do resistor
    canvas.create_line(30, 70, 120, 70, width=5, fill="#777777")
    canvas.create_line(400, 70, 490, 70, width=5, fill="#777777")


    # Corpo do resistor
    canvas.create_rectangle(
        120, 35, 400, 105,
        fill="#F0DFA6",
        outline="#555555",
        width=2
    )


    # Faixas de cores
    canvas.create_rectangle(
        165, 35, 185, 105,
        fill=cor1,
        outline=""
    )

    canvas.create_rectangle(
        210, 35, 230, 105,
        fill=cor2,
        outline=""
    )

    canvas.create_rectangle(
        255, 35, 275, 105,
        fill=cor3,
        outline=""
    )

    canvas.create_rectangle(
        335, 35, 355, 105,
        fill=cor4,
        outline=""
    )


# --------------------------------------------------------------  CALCULAR PELAS CORES

# Transforma as cores em resistencia

def calcular_por_cores():

    cor1 = banda1.get()
    cor2 = banda2.get()
    multiplicador = banda3.get()
    tolerancia = banda4.get()


    # As duas primeiras cores formam o numero
    # Exemplo: 2 e 5 viram 25
    numero = valores_cores[cor1] * 10 + valores_cores[cor2]


    # Aplica o multiplicador
    resistencia = numero * multiplicadores[multiplicador]


    # Pega a tolerancia
    tolerancia_valor = tolerancias[tolerancia]


    # Mostra o resultado
    resultado = formatar_resistencia(resistencia)

    resultado_label.config(
        text=f"Resistência: {resultado} ±{tolerancia_valor}%"
    )


    # Atualiza o desenho
    desenhar_resistor(
        cores_visuais[cor1],
        cores_visuais[cor2],
        cores_visuais[multiplicador],
        cores_visuais[tolerancia]
    )


# Calculo pelo valor
# Aqui e o caminho inverso
# O usuario digita o valor e o programa procura as cores

def calcular_por_valor():

    # Aceita virgula ou ponto
    entrada = valor_entrada.get().replace(",", ".")

    # Tenta transformar em numero
    try:
        valor = float(entrada)

        if valor <= 0:
            raise ValueError


    except ValueError:

        resultado_label.config(
            text="Digite um valor válido.",
            fg="red"
        )

        canvas.delete("all")
        return


# Testa as combinacoes de cores
    for cor1, valor1 in valores_cores.items():

        for cor2, valor2 in valores_cores.items():

            numero = valor1 * 10 + valor2

            for cor3, multiplicador in multiplicadores.items():

                resultado = numero * multiplicador


                if resultado == valor:

                    tolerancia = tolerancia_entrada.get()


                    resultado_label.config(
                        text=f"Resistência: "
                             f"{formatar_resistencia(valor)} "
                             f"±{tolerancias[tolerancia]}%",
                        fg="#222222"
                    )

# Coloca as cores encontradas nos campos
  
                    banda1.set(cor1)
                    banda2.set(cor2)
                    banda3.set(cor3)
                    banda4.set(tolerancia)


    # Atualiza o resistor
                    desenhar_resistor(
                        cores_visuais[cor1],
                        cores_visuais[cor2],
                        cores_visuais[cor3],
                        cores_visuais[tolerancia]
                    )

                    return


    resultado_label.config(
        text="Não foi encontrada uma combinação.",
        fg="red"
    )

    canvas.delete("all")


# Escolha do calculo


# Decide qual calculo usar

def calcular():

# Guarda o modo escolhido
    if modo.get() == "cores":
        calcular_por_cores()

    else:
        calcular_por_valor()


# Limpar
# Volta para o estado inicial

def limpar():

    valor_entrada.delete(0, END)

    banda1.set("vermelho")
    banda2.set("vermelho")
    banda3.set("laranja")
    banda4.set("ouro")

    tolerancia_entrada.set("ouro")


    resultado_label.config(
        text="Selecione as cores ou informe um valor.",
        fg="#666666"
    )

    canvas.delete("all")


# Trocar o modo
# Alterna entre os dois modos

def mudar_modo():

    if modo.get() == "cores":

        frame_valor.pack_forget()
        frame_cores.pack(fill="x")

        botao_calcular.config(
            text="Calcular resistência"
        )

    else:

        frame_cores.pack_forget()
        frame_valor.pack(fill="x")

        botao_calcular.config(
            text="Calcular cores"
        )


    valor_entrada.delete(0, END)


    resultado_label.config(
        text="Selecione as cores ou informe um valor.",
        fg="#666666"
    )

    canvas.delete("all")


# Janela
# Monta a interface

janela = Tk()

janela.title("Calculadora de Resistor")
janela.geometry("570x480")
janela.resizable(False, False)
janela.configure(bg="#eef2f5")

# Titulo
# Titulo da janela

Label(
    janela,
    text="Calculadora de Resistor",
    font=("Arial", 18, "bold"),
    bg="#eef2f5",
    fg="#263238"
).pack(
    anchor="w",
    padx=20,
    pady=(15, 7)
)


# Painel
# Organiza os componentes

painel = Frame(janela, bg="white")

painel.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)


# Escolha do modo
# Escolhe entre cores ou valor

Label(
    painel,
    text="Como deseja informar o resistor?",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(
    anchor="w",
    padx=15,
    pady=(12, 2)
)


modo = StringVar(value="cores")


frame_opcoes = Frame(painel, bg="white")
frame_opcoes.pack(anchor="w", padx=10)


Radiobutton(
    frame_opcoes,
    text="Cores do resistor",
    variable=modo,
    value="cores",
    command=mudar_modo,
    bg="white"
).pack(side=LEFT)


Radiobutton(
    frame_opcoes,
    text="Valor da resistência",
    variable=modo,
    value="valor",
    command=mudar_modo,
    bg="white"
).pack(
    side=LEFT,
    padx=15
)


# Area dos campos
# Area que muda conforme o modo

frame_conteudo = Frame(
    painel,
    bg="white",
    height=55
)

frame_conteudo.pack(
    fill="x",
    padx=15,
    pady=7
)

frame_conteudo.pack_propagate(False)


# Campos das cores
# Escolha das quatro faixas

frame_cores = Frame(
    frame_conteudo,
    bg="white"
)

frame_cores.pack(fill="x")


Label(
    frame_cores,
    text="Banda 1:",
    bg="white"
).grid(row=0, column=0)


banda1 = ttk.Combobox(
    frame_cores,
    values=list(valores_cores.keys()),
    width=11,
    state="readonly"
)

banda1.set("vermelho")
banda1.grid(row=1, column=0, padx=(0, 7))


Label(
    frame_cores,
    text="Banda 2:",
    bg="white"
).grid(row=0, column=1)


banda2 = ttk.Combobox(
    frame_cores,
    values=list(valores_cores.keys()),
    width=11,
    state="readonly"
)

banda2.set("vermelho")
banda2.grid(row=1, column=1, padx=7)


Label(
    frame_cores,
    text="Multiplicador:",
    bg="white"
).grid(row=0, column=2)


banda3 = ttk.Combobox(
    frame_cores,
    values=list(multiplicadores.keys()),
    width=11,
    state="readonly"
)

banda3.set("laranja")
banda3.grid(row=1, column=2, padx=7)


Label(
    frame_cores,
    text="Tolerância:",
    bg="white"
).grid(row=0, column=3)


banda4 = ttk.Combobox(
    frame_cores,
    values=list(tolerancias.keys()),
    width=11,
    state="readonly"
)

banda4.set("ouro")
banda4.grid(row=1, column=3, padx=(7, 0))


# Campo do valor
# Nesse modo o usuario digita o valor

frame_valor = Frame(
    frame_conteudo,
    bg="white"
)


Label(
    frame_valor,
    text="Valor (Ω):",
    bg="white"
).pack(side=LEFT)


valor_entrada = Entry(
    frame_valor,
    width=18
)

valor_entrada.pack(
    side=LEFT,
    padx=6
)


Label(
    frame_valor,
    text="Tolerância:",
    bg="white"
).pack(
    side=LEFT,
    padx=5
)


tolerancia_entrada = ttk.Combobox(
    frame_valor,
    values=list(tolerancias.keys()),
    width=10,
    state="readonly"
)

tolerancia_entrada.set("ouro")
tolerancia_entrada.pack(side=LEFT)


# Botoes
# Botoes principais

frame_botoes = Frame(
    painel,
    bg="white"
)

frame_botoes.pack(
    anchor="w",
    padx=15,
    pady=5
)


botao_calcular = Button(
    frame_botoes,
    text="Calcular resistência",
    command=calcular,
    bg="#4FAEA4",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat"
)

botao_calcular.pack(side=LEFT)


Button(
    frame_botoes,
    text="Limpar",
    command=limpar,
    bg="#dddddd",
    relief="flat"
).pack(
    side=LEFT,
    padx=7
)


# Resultado
# Mostra o resultado

Label(
    painel,
    text="Resultado",
    font=("Arial", 10, "bold"),
    bg="white"
).pack(
    anchor="w",
    padx=15
)


resultado_label = Label(
    painel,
    text="Selecione as cores ou informe um valor.",
    bg="#f5f7f9",
    fg="#666666",
    anchor="w",
    padx=8
)

resultado_label.pack(
    fill="x",
    padx=15,
    ipady=6
)


canvas = Canvas(
    painel,
    width=525,
    height=145,
    bg="#f8fafc",
    highlightthickness=1
)

canvas.pack(
    padx=15,
    pady=7
)


janela.mainloop()
