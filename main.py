from tkinter import *

# ---------- VALIDAÇÃO EM TEMPO REAL ----------
def validar_numero(texto):
    if texto == "":
        return True
    try:
        float(texto)
        return True
    except ValueError:
        return False

# ---------- CÁLCULO IMC ----------
def calcularimc():
    try:
        imcpeso = float(peso_entrada.get())
        imcaltura = float(altura_entrada.get())

        if imcpeso <= 0 or imcaltura <= 0:
            resposta.config(text='')
            subresposta.config(
                text='⚠ Peso e altura devem ser maiores que zero',
                fg='red'
            )
            return

        imc = imcpeso / (imcaltura ** 2)
        resposta.config(text=f'📊 IMC: {imc:.2f}', fg='#2c3e50')

        if imc < 16:
            texto = '🔵 Magreza grave'
            cor = '#2980b9'
        elif imc < 17:
            texto = '🔵 Magreza moderada'
            cor = '#3498db'
        elif imc < 18.5:
            texto = '🔵 Magreza leve'
            cor = '#5dade2'
        elif imc < 25:
            texto = '🟢 Saudável'
            cor = '#27ae60'
        elif imc < 30:
            texto = '🟠 Sobrepeso'
            cor = '#f39c12'
        elif imc < 35:
            texto = '🔴 Obesidade grau 1'
            cor = '#e74c3c'
        elif imc < 40:
            texto = '🔴 Obesidade grau 2'
            cor = '#c0392b'
        else:
            texto = '🔴 Obesidade grau 3'
            cor = '#922b21'

        subresposta.config(text=texto, fg=cor)

    except ValueError:
        resposta.config(text='')
        subresposta.config(
            text='❌ Digite apenas números válidos',
            fg='red'
        )

# ---------- JANELA ----------
janela = Tk()
janela.title('Calculadora de IMC')
janela.geometry('320x430')
janela.resizable(False, False)
janela.configure(bg='#ecf0f1')

# ---------- REGISTRO DA VALIDAÇÃO ----------
validacao = janela.register(validar_numero)

# ---------- CARD ----------
card = Frame(janela, bg='white', padx=20, pady=20)
card.place(relx=0.5, rely=0.5, anchor='center')

# ---------- TÍTULO ----------
titulo = Label(
    card,
    text='🧮 Calculadora de IMC',
    font=('Segoe UI', 16, 'bold'),
    bg='white',
    fg='#2c3e50'
)
titulo.pack(pady=(0, 15))

# ---------- PESO ----------
Label(
    card,
    text='Peso (kg)',
    font=('Segoe UI', 10),
    bg='white'
).pack(anchor='w')

peso_entrada = Entry(
    card,
    font=('Segoe UI', 11),
    width=20,
    relief='solid',
    bd=1,
    validate='key',
    validatecommand=(validacao, '%P')
)
peso_entrada.pack(pady=(0, 10))

# ---------- ALTURA ----------
Label(
    card,
    text='Altura (m)',
    font=('Segoe UI', 10),
    bg='white'
).pack(anchor='w')

altura_entrada = Entry(
    card,
    font=('Segoe UI', 11),
    width=20,
    relief='solid',
    bd=1,
    validate='key',
    validatecommand=(validacao, '%P')
)
altura_entrada.pack(pady=(0, 15))

# ---------- BOTÃO ----------
botao = Button(
    card,
    text='Calcular IMC',
    font=('Segoe UI', 11, 'bold'),
    bg='#3498db',
    fg='white',
    activebackground='#2980b9',
    relief='flat',
    command=calcularimc
)
botao.pack(fill='x', pady=(0, 15))

# ---------- RESULTADOS ----------
resposta = Label(
    card,
    text='',
    font=('Segoe UI', 12, 'bold'),
    bg='white'
)
resposta.pack()

subresposta = Label(
    card,
    text='',
    font=('Segoe UI', 10),
    bg='white'
)
subresposta.pack()

janela.mainloop()