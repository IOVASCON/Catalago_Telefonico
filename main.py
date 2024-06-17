# main.py

# Importa a classe CatalogoTelefonico do módulo utils.catalogo
from utils.catalogo import CatalogoTelefonico
import tkinter as tk
from tkinter import messagebox

# Função para incluir um contato, chamada ao clicar no botão "Incluir"
def incluir():
    nome = entry_nome.get()  # Obtém o nome do campo de entrada
    telefone = entry_telefone.get()  # Obtém o telefone do campo de entrada
    if nome and telefone:
        msg = catalogo.incluir_contato(nome, telefone)  # Chama o método incluir_contato
        messagebox.showinfo("Info", msg)  # Exibe uma mensagem informativa
    else:
        messagebox.showerror("Erro", "Nome e telefone são obrigatórios.")  # Exibe uma mensagem de erro

# Função para excluir um contato, chamada ao clicar no botão "Excluir"
def excluir():
    nome = entry_nome.get()  # Obtém o nome do campo de entrada
    if nome:
        msg = catalogo.excluir_contato(nome)  # Chama o método excluir_contato
        messagebox.showinfo("Info", msg)  # Exibe uma mensagem informativa
    else:
        messagebox.showerror("Erro", "Nome é obrigatório.")  # Exibe uma mensagem de erro

# Função para pesquisar um contato, chamada ao clicar no botão "Pesquisar"
def pesquisar():
    nome = entry_nome.get()  # Obtém o nome do campo de entrada
    if nome:
        msg = catalogo.pesquisar_contato(nome)  # Chama o método pesquisar_contato
        messagebox.showinfo("Info", msg)  # Exibe uma mensagem informativa
    else:
        messagebox.showerror("Erro", "Nome é obrigatório.")  # Exibe uma mensagem de erro

# Função para imprimir o catálogo, chamada ao clicar no botão "Imprimir"
def imprimir():
    msg = catalogo.imprimir_catalogo()  # Chama o método imprimir_catalogo
    messagebox.showinfo("Catálogo Telefônico", msg)  # Exibe o catálogo em uma mensagem informativa

# Cria uma instância da classe CatalogoTelefonico
catalogo = CatalogoTelefonico()

# Configuração da interface gráfica
root = tk.Tk()  # Cria a janela principal do Tkinter
root.title("Catálogo Telefônico")  # Define o título da janela

frame = tk.Frame(root)  # Cria um frame dentro da janela principal
frame.pack(padx=10, pady=10)  # Adiciona padding ao frame

# Criação e posicionamento dos widgets (rótulos, campos de entrada e botões)
label_nome = tk.Label(frame, text="Nome:")  # Cria um rótulo para o nome
label_nome.grid(row=0, column=0, pady=5)  # Posiciona o rótulo na grade

entry_nome = tk.Entry(frame)  # Cria um campo de entrada para o nome
entry_nome.grid(row=0, column=1, pady=5)  # Posiciona o campo de entrada na grade

label_telefone = tk.Label(frame, text="Telefone:")  # Cria um rótulo para o telefone
label_telefone.grid(row=1, column=0, pady=5)  # Posiciona o rótulo na grade

entry_telefone = tk.Entry(frame)  # Cria um campo de entrada para o telefone
entry_telefone.grid(row=1, column=1, pady=5)  # Posiciona o campo de entrada na grade

button_incluir = tk.Button(frame, text="Incluir", command=incluir)  # Cria um botão para incluir
button_incluir.grid(row=2, column=0, pady=5)  # Posiciona o botão na grade

button_excluir = tk.Button(frame, text="Excluir", command=excluir)  # Cria um botão para excluir
button_excluir.grid(row=2, column=1, pady=5)  # Posiciona o botão na grade

button_pesquisar = tk.Button(frame, text="Pesquisar", command=pesquisar)  # Cria um botão para pesquisar
button_pesquisar.grid(row=3, column=0, pady=5)  # Posiciona o botão na grade

button_imprimir = tk.Button(frame, text="Imprimir", command=imprimir)  # Cria um botão para imprimir
button_imprimir.grid(row=3, column=1, pady=5)  # Posiciona o botão na grade

# Inicia o loop principal do Tkinter
root.mainloop()
