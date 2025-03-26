
import tkinter as tk
from database import conectar, criar_tabelas, criar_usuario_inicial

def tela_principal(profissional):
    janela = tk.Tk()
    janela.title("BarberControl - Tela Principal")
    janela.state('zoomed')  # Janela maximizada

    # Paleta de Cores Terrosas Fortes
    cor_fundo = "#D8C8A7"  # Bege Escuro
    cor_texto_principal = "#FFFFFF"  # Branco
    cor_texto_secundario = "#3E2C1C"  # Marrom Escuro
    cor_botao = "#8E735B"  # Marrom Médio
    cor_botao_destque = "#D75D49"  # Terracota Forte
    cor_verdinho = "#4C6B3C"  # Verde Escuro

    fonte_padrao = ("Arial", 18)

    # Configuração do fundo da janela
    janela.configure(bg=cor_fundo)

    # Frame centralizado
    frame = tk.Frame(janela, bg=cor_fundo)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Saudação com o nome do profissional
    label_profissional = tk.Label(frame, text=f"Bem-vindo, {profissional}!", font=("Arial", 22), bg=cor_fundo, fg=cor_texto_principal)
    label_profissional.pack(pady=30)

    # Botões principais
    botao_orcamento = tk.Button(frame, text="Novo Orçamento", font=fonte_padrao, width=20, height=2, bg=cor_botao, fg=cor_texto_principal)
    botao_orcamento.pack(pady=10)

    botao_clientes = tk.Button(frame, text="Clientes", font=fonte_padrao, width=20, height=2, bg=cor_botao, fg=cor_texto_principal)
    botao_clientes.pack(pady=10)

    botao_relatorios = tk.Button(frame, text="Relatórios", font=fonte_padrao, width=20, height=2, bg=cor_botao, fg=cor_texto_principal)
    botao_relatorios.pack(pady=10)

    botao_sair = tk.Button(frame, text="Sair", font=fonte_padrao, width=20, height=2, bg=cor_botao_destque, fg=cor_texto_principal, command=janela.destroy)
    botao_sair.pack(pady=30)

    print("A tela principal foi aberta!")
    janela.mainloop()
