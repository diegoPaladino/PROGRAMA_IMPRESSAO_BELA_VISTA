# test_impressão_impressora
# FONTE DE CONHECIMENTO: https://tiforadacaixa.blogspot.com/2018/11/curso-de-tkinter-aula-8-executar-funcao.html
# FONTE DE CONHECIMENTO II: https://www.delftstack.com/pt/tutorial/tkinter-tutorial/tkinter-geometry-managers/



import os
import tkinter
from tkinter import *
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk

# 5Q1
def aoClicar_5Q1A():
    print('eureka! = atividades agrupamento')
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/AG_-_V/KIT7AGRUP.5de12a27.05REV-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do AGRUPAMENTO')

def aoClicar_5Q11():
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do 1º ANO')

def aoClicar_5Q12():
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/2º_ANO/001-2º_ANO_-_1aQUINZENA-MAIO.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do 2º ANO')

def aoClicar_5Q13():
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/3º_ANO/3º_ANO.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do 3º ANO')

def aoClicar_5Q14():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 4º ANO apenas através dos LIVROS')

def aoClicar_5Q15():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 5º ANO apenas através dos LIVROS')

# 5Q2
def aoClicar_5Q2A():
    print('eureka! = atividades agrupamento')
    # os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/AG_-_V/KIT7AGRUP.5de12a27.05REV-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades da 2ª Quinzena de Maio, do AGRUPAMENTO 5, não entregues pelos professores. Não carregadas no programa')

def aoClicar_5Q21():
    # os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades da 2ª Quinzena de Maio, do 1º ANO, não entregues pelos professores. Não carregadas no programa')

def aoClicar_5Q22():
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/IMPRESSAO_B/ATIVIDADES/2ª_QUINZENA/2º_ANO/ATIVIDADE_2ANO_2QUINZENA_MAIO.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do 2º ANO. 2ª Quinzena de Maio')

def aoClicar_5Q23():
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/IMPRESSAO_B/ATIVIDADES/2ª_QUINZENA/3º_ANO/ ATIVIDADE_3ANO_2QUINZENA_MAIO.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do 3º ANO. 2ª Quinzena de Maio')

def aoClicar_5Q24():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 4º ANO apenas através dos LIVROS')

def aoClicar_5Q25():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 5º ANO apenas através dos LIVROS')


# 6Q1
def aoClicar_6Q1A():
    print('eureka! = atividades agrupamento')
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/JUNHO/6Q1/AG_-_V/6Q1A.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do AGRUPAMENTO. 1ª Quinzena de Junho')

def aoClicar_6Q11():
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/JUNHO/6Q1/1º_ANO/6Q11.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do 1º ANO. 1ª Quinzena de Junho')

def aoClicar_6Q12():
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/JUNHO/6Q1/2º_ANO/6Q22.pdf","print")
    tkmsg.showinfo(title='',message='Já está sendo impressa a atividade do 2º ANO. 1ª Quinzena de Junho')

def aoClicar_6Q13():
    # os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/IMPRESSAO_B/ATIVIDADES/2ª_QUINZENA/3º_ANO/ ATIVIDADE_3ANO_2QUINZENA_MAIO.pdf","print")
    tkmsg.showinfo(title='',message='Atividades da 1ª Quinzena de Junho, do 3º ano, não entregues pelos professores. Não carregadas no programa')

def aoClicar_6Q14():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 4º ANO apenas através dos LIVROS')

def aoClicar_6Q15():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 5º ANO apenas através dos LIVROS')


# 6Q2
def aoClicar_6Q2A():
    print('eureka! = atividades agrupamento')
    os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/JUNHO/6Q2/AG_-_V/6Q2A.pdf","print")
    tkmsg.showinfo(title='',message='Atividades da 2ª Quinzena de Junho, do AGRUPAMENTO já estão sendo impressas.')

def aoClicar_6Q21():
    # os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades da 2ª Quinzena de Junho, do 1º ANO, não entregues pelos professores. Não carregadas no programa')

def aoClicar_6Q22():
    # os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/IMPRESSAO_B/ATIVIDADES/2ª_QUINZENA/2º_ANO/ATIVIDADE_2ANO_2QUINZENA_MAIO.pdf","print")
    tkmsg.showinfo(title='',message='Atividades da 2ª Quinzena de Junho, do 2º ANO, não entregues pelos professores. Não carregadas no programa')

def aoClicar_6Q23():
    # os.startfile("C:/Users/Administrador/Documents/DIEGO/ONE/IMPRESSAO_ATIVIDADES/JUNHO/6Q2/AG_-_V/6Q2A.pdf","print")
    tkmsg.showinfo(title='',message='Atividades da 2ª Quinzena de Junho, do 3º ANO, não entregues pelos professores. Não carregadas no programa')

def aoClicar_6Q24():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 4º ANO apenas através dos LIVROS')

def aoClicar_6Q25():
    # os.startfile("C:/Users/Administrador/Desktop/ATIVIDADES_MAIO/1ª_QUINZENA/1º_ANO/001-ATIVIDADESDEMAIO-TUDO-mesclado.pdf","print")
    tkmsg.showinfo(title='',message='Atividades do 5º ANO apenas através dos LIVROS')

# root
window = Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
# window.attributes('-fullscreen', True)
# window.geometry("1600x900+200+100")
window.title("E.M. BELA VISTA - IMPRESSÃO DE ATIVIDADES")

# # MENSAGENS
# MENSAGEM_1-"CLIQUE UMA VEZ..."
mensagem = Label(window, text="CLIQUE 1 VEZ SOB A TURMA:\n", font="calibri 20 bold")
mensagem.pack(side="right")
mensagem.place(x=200,y=10)

# MENSAGEM_LEGENDA
mensagem = Label(window, text="Legenda:", font="calibri 12 bold")
mensagem.pack(side="right")
mensagem.place(x=0,y=790)

# MENSAGEM_2-"MAIO"
mensagem = Label(window, text="MAIO", font="calibri 16 bold")
mensagem.place(x=20,y=100)

# MENSAGEM_5Q1A-"1ª QUINZENA"
mensagem = Label(window, text="1ª QUINZENA", font="calibri 16 bold")
mensagem.place(x=100,y=80)

# MENSAGEM_5Q2B-"2ª QUINZENA"
mensagem = Label(window, text="2ª QUINZENA", font="calibri 16 bold")
mensagem.place(x=100,y=120)


# MENSAGEM_2-"MAIO"
mensagem = Label(window, text="JUNHO", font="calibri 16 bold")
mensagem.place(x=20,y=300)

# MENSAGEM_5Q1A-"1ª QUINZENA"
mensagem = Label(window, text="1ª QUINZENA", font="calibri 16 bold")
mensagem.place(x=100,y=285)

# MENSAGEM_5Q2B-"2ª QUINZENA"
mensagem = Label(window, text="2ª QUINZENA", font="calibri 16 bold")
mensagem.place(x=100,y=325)




# 5Q1
botao_1_5Q1 = Button(window, text="AGRUPAMENTO", command=aoClicar_5Q1A, bg='SeaGreen2')
botao_1_5Q1.place(x=270,y=85)
botao_2_5Q1 = Button(window, text="1º ANO", command=aoClicar_5Q11, bg='SeaGreen2')
botao_2_5Q1.place(x=390,y=85)
botao_3_5Q1 = Button(window, text="2º ANO", command=aoClicar_5Q12, bg='SeaGreen2')
botao_3_5Q1.place(x=450,y=85)
botao_4_5Q1 = Button(window, text="3º ANO", command=aoClicar_5Q13, bg='SeaGreen2')
botao_4_5Q1.place(x=510,y=85)
botao_5_5Q1 = Button(window, text="4º ANO", command=aoClicar_5Q14, bg='dim gray')
botao_5_5Q1.place(x=570,y=85)
botao_6_5Q1 = Button(window, text="5º ANO", command=aoClicar_5Q15, bg='dim gray')
botao_6_5Q1.place(x=630,y=85)

# 5Q2
botao_1_5Q2 = Button(window, text="AGRUPAMENTO", command=aoClicar_5Q2A, bg='SeaGreen2')
botao_1_5Q2.place(x=270,y=125)
botao_2_5Q2 = Button(window, text="1º ANO", command=aoClicar_5Q21, bg='SeaGreen2')
botao_2_5Q2.place(x=390,y=125)
botao_3_5Q2 = Button(window, text="2º ANO", command=aoClicar_5Q22, bg='SeaGreen2')
botao_3_5Q2.place(x=450,y=125)
botao_4_5Q2 = Button(window, text="3º ANO", command=aoClicar_5Q23, bg='SeaGreen2')
botao_4_5Q2.place(x=510,y=125)
botao_5_5Q2 = Button(window, text="4º ANO", command=aoClicar_5Q24, bg='dim gray')
botao_5_5Q2.place(x=570,y=125)
botao_6_5Q2 = Button(window, text="5º ANO", command=aoClicar_5Q25, bg='dim gray')
botao_6_5Q2.place(x=630,y=125)

# 6Q1
botao_1_6Q1 = Button(window, text="AGRUPAMENTO", command=aoClicar_6Q1A, bg='SeaGreen2')
botao_1_6Q1.place(x=270,y=285)
botao_2_6Q1 = Button(window, text="1º ANO", command=aoClicar_6Q11, bg='SeaGreen2')
botao_2_6Q1.place(x=390,y=285)
botao_3_6Q1 = Button(window, text="2º ANO", command=aoClicar_6Q12, bg='SeaGreen2')
botao_3_6Q1.place(x=450,y=285)
botao_4_6Q1 = Button(window, text="3º ANO", command=aoClicar_6Q13, bg='SeaGreen2')
botao_4_6Q1.place(x=510,y=285)
botao_5_6Q1 = Button(window, text="4º ANO", command=aoClicar_6Q14, bg='dim gray')
botao_5_6Q1.place(x=570,y=285)
botao_6_6Q1 = Button(window, text="5º ANO", command=aoClicar_6Q15, bg='dim gray')
botao_6_6Q1.place(x=630,y=285)

# 6Q2
botao_1_6Q2 = Button(window, text="AGRUPAMENTO", command=aoClicar_6Q2A, bg='SeaGreen2')
botao_1_6Q2.place(x=270,y=325)
botao_2_6Q2 = Button(window, text="1º ANO", command=aoClicar_6Q21, bg='OrangeRed2')
botao_2_6Q2.place(x=390,y=325)
botao_3_6Q2 = Button(window, text="2º ANO", command=aoClicar_6Q22, bg='OrangeRed2')
botao_3_6Q2.place(x=450,y=325)
botao_4_6Q2 = Button(window, text="3º ANO", command=aoClicar_6Q23, bg='OrangeRed2')
botao_4_6Q2.place(x=510,y=325)
botao_5_6Q2 = Button(window, text="4º ANO", command=aoClicar_6Q24, bg='dim gray')
botao_5_6Q2.place(x=570,y=325)
botao_6_6Q2 = Button(window, text="5º ANO", command=aoClicar_6Q25, bg='dim gray')
botao_6_6Q2.place(x=630,y=325)


# BOTOES DA LEGENDA
botao_legenda_1 = Button(window, text="DISPONÍVEL", bg='SeaGreen2')
botao_legenda_1.place(x=70,y=790)

botao_legenda_2 = Button(window, text="NÃO DISPONÍVEL", bg='OrangeRed2')
botao_legenda_2.place(x=160,y=790)

botao_legenda_3 = Button(window, text="LIVROS", bg='dim gray')
botao_legenda_3.place(x=280,y=790)

# ABRINDO IMAGEM
logo = Tk()

image1 = Image.open("C:/Users/Administrador/Documents/DIEGO/COMUNICAÇÃO/LOGO_EMBELA_VISTA/logo_bela_vista-png.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=200, y=400)
logo.mainloop()




window.mainloop()
