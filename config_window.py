import tkinter as tk

def change_state(row, col, state):
    buttons[row][col].config(text=str(state))
    vagas[row][col] = state

def button_click(row, col):
    txt = buttons[row][col].cget("text")
    if txt == "0":
        change_state(row, col, 1)
    if txt == "1":
        change_state(row, col, 0)


# Define o número de linhas e colunas
altura: int = 3 # int(input("Altura: "))
largura: int = 3 # int(input("Largura: "))

# Cria a janela principal
root = tk.Tk()
root.title("Matriz de Botões")

# Cria uma lista para armazenar os botões
buttons = []
vagas = []

# Cria a matriz de botões
for i in range(altura):
    row_buttons = []  # Lista para os botões de cada linha
    linhas = []
    for j in range(largura):
        btn = tk.Button(root, text='0', 
                        command=lambda row=i, col=j: button_click(row, col))
        btn.grid(row=i, column=j, padx=10, pady=10)

        row_buttons.append(btn)  # Adiciona o botão à lista da linha
        linhas.append(0)
        
    buttons.append(row_buttons)  # Adiciona a linha à lista principal
    vagas.append(linhas)

# Inicia o loop principal da interface gráfica
root.mainloop()