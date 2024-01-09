from tkinter import *
from tkinter import messagebox

numero1 = ''
numero2 = ''
somar = FALSE
subtracao = FALSE
multilicacao = FALSE
divisao = FALSE

def btn_click(num):
    entrada.insert(END, num)
    

def btn_soma():
   global numero1
   global somar
   somar = True
   numero1 = entrada.get()
   entrada.delete(0, END)

def btn_subtracao():
   global numero1
   global subtracao
   subtracao = True
   numero1 = entrada.get()
   entrada.delete(0, END)

def btn_multilicacao():
   global numero1
   global multilicacao
   multilicacao = True
   numero1 = entrada.get()
   entrada.delete(0, END) 

def btn_divisao():
   global numero1
   global divisao
   divisao = True
   numero1 = entrada.get()
   entrada.delete(0, END) 

def btn_limpar():
   entrada.delete(0, END) 
   
def btn_igual():
   global somar
   global subtracao
   global multilicacao
   global divisao
   global numero2
   numero2 = entrada.get()
   entrada.delete(0, END)

   try:
      if somar == True:
         entrada.insert(0, int(numero1) + int(numero2))
         somar = FALSE
      elif subtracao == True:
         entrada.insert(0, int(numero1) - int(numero2))
         subtracao = FALSE 
      elif multilicacao == True:
         entrada.insert(0, int(numero1) * int(numero2))
         multilicacao = FALSE 
      elif divisao == True:
         entrada.insert(0, int(numero1) / int(numero2))
         divisao = FALSE      
   except:
      messagebox.showerror(f'', 'ERROR')
   





root = Tk()

root.title('Calculadora')
root.geometry(f'300x230')
root.wm_maxsize(width=300, height=230)
root.wm_minsize(width=300, height=230)
root.config(background='#302c34')

#Entrada dos números
entrada = Entry(root, width=25, font=('Arial', 12))
entrada.grid(column=0, row=0, columnspan=5, pady=5)

#Botões Numéricos
btn_0 = Button(root, text="0", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(0))
btn_0.grid(column=1, row=5, pady=2, padx=3)

btn_1 = Button(root, text="1", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(1))
btn_1.grid(column=0, row=4, pady=3, padx=3)

btn_2 = Button(root, text="2", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(2))
btn_2.grid(column=1, row=4, pady=3, padx=3)

btn_3 = Button(root, text="3", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(3))
btn_3.grid(column=2, row=4, pady=3, padx=3)

btn_4 = Button(root, text="4", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(4))
btn_4.grid(column=0, row=3, pady=3, padx=3)

btn_5 = Button(root, text="5", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(5))
btn_5.grid(column=1, row=3, pady=3, padx=3)

btn_6 = Button(root, text="6", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(6))
btn_6.grid(column=2, row=3, pady=3, padx=3)

btn_7 = Button(root, text="7", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(7))
btn_7.grid(column=0, row=2, pady=3, padx=3)

btn_8 = Button(root, text="8", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(8))
btn_8.grid(column=1, row=2, pady=3, padx=3)

btn_9 = Button(root, text="9", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda: btn_click(9))
btn_9.grid(column=2, row=2, pady=3, padx=3)


#Botões para os Operadores
btn_soma = Button(root, text="+", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=btn_soma)
btn_soma.grid(column=3, row=2, pady=3, padx=3)

btn_sub = Button(root, text="-", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=btn_subtracao)
btn_sub.grid(column=4, row=2, pady=3, padx=3)

btn_mult = Button(root, text="*", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=btn_multilicacao)
btn_mult.grid(column=3, row=3, pady=3, padx=3)

btn_div = Button(root, text="/", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=btn_divisao)
btn_div.grid(column=4, row=3, pady=3, padx=3)

#Botão Limpar
btn_c = Button(root, text="C", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=btn_limpar)
btn_c.grid(column=0, row=5, pady=3, padx=3)

#Caracteres especiais
btn_ponto = Button(root, text=".", width=5, height=2, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=lambda:btn_click('.'))
btn_ponto.grid(column=2, row=5, pady=3, padx=3)

btn_igual= Button(root, text="=", width=15, height=5, bg='#d3c56c', fg='#ffffff', activebackground='#2c38b0', command=btn_igual)
btn_igual.grid(column=3, row=4, columnspan=2, rowspan=4, pady=3, padx=3)


root.mainloop()