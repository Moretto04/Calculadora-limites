from tkinter import *

# Função que realiza a integração
def calcular_integral():
    # Obtém a função a ser integrada e os limites de integração
    func = entrada_funcao.get()
    limite_inferior = float(entrada_limite_inferior.get())
    limite_superior = float(entrada_limite_superior.get())
    n_retangulos = int(entrada_n_retangulos.get())
    
    # Define o tamanho dos subintervalos
    delta_x = (limite_superior - limite_inferior) / n_retangulos
    
    # Aproxima o valor da integral por retângulos
    soma_areas = 0
    for i in range(n_retangulos):
        x_i = limite_inferior + i * delta_x
        area_retangulo = delta_x * eval(func.replace('x', str(x_i)))
        soma_areas += area_retangulo
    
    # Atualiza o resultado na interface
    resultado.configure(text="Resultado: " + str(soma_areas))

# Cria a interface gráfica
janela = Tk()
janela.title("Calculadora de Integrais")

# Cria os widgets
texto_funcao = Label(janela, text="Função:")
entrada_funcao = Entry(janela)
texto_limite_inferior = Label(janela, text="Limite Inferior:")
entrada_limite_inferior = Entry(janela)
texto_limite_superior = Label(janela, text="Limite Superior:")
entrada_limite_superior = Entry(janela)
texto_n_retangulos = Label(janela, text="Número de Retângulos:")
entrada_n_retangulos = Entry(janela)
botao_calcular = Button(janela, text="Calcular", command=calcular_integral)
resultado = Label(janela, text="Resultado: ")

# Define a posição dos widgets na janela
texto_funcao.grid(row=0, column=0)
entrada_funcao.grid(row=0, column=1)
texto_limite_inferior.grid(row=1, column=0)
entrada_limite_inferior.grid(row=1, column=1)
texto_limite_superior.grid(row=2, column=0)
entrada_limite_superior.grid(row=2, column=1)
texto_n_retangulos.grid(row=3, column=0)
entrada_n_retangulos.grid(row=3, column=1)
botao_calcular.grid(row=4, column=0)
resultado.grid(row=4, column=1)

# Inicia a interface
janela.mainloop()