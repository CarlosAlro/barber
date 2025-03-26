import tkinter as tk
from tkinter import messagebox
from database import conectar, criar_tabelas, criar_usuario_inicial

def verificar_login(usuario, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def tela_login():
    def tentar_login():
        user = entry_usuario.get()
        pwd = entry_senha.get()

        if verificar_login(user, pwd):
            janela.destroy()
            # Chamar a tela principal
            import home
            home.tela_principal(user)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    janela = tk.Tk()
    janela.title("Login - BarberControl")


    # Ajustar a janela para preencher a tela (sem fullscreen)
    largura = janela.winfo_screenwidth()  # Largura da tela
    altura = janela.winfo_screenheight()  # Altura da tela
    janela.geometry(f"{largura}x{altura}")  # Ajusta a janela para o tamanho da tela

    cor_fundo = "#D8C8A7"


    janela.configure(bg=cor_fundo)

    # Frame centralizado
    frame = tk.Frame(janela,bg=cor_fundo)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Estilização e tamanho
    fonte_label = ("Arial", 18)
    fonte_entry = ("Arial", 16)
    fonte_botao = ("Arial", 16)

    tk.Label(frame, text="Usuário:", font=fonte_label, fg="brown", bg="cor_fundo").pack(pady=10)
    entry_usuario = tk.Entry(frame, font=fonte_entry, width=30)
    entry_usuario.pack()

    tk.Label(frame, text="Senha:", font=fonte_label).pack(pady=10)
    entry_senha = tk.Entry(frame, show="*", font=fonte_entry, width=30)
    entry_senha.pack()

    tk.Button(frame, text="Entrar", font=fonte_botao, command=tentar_login, width=20, height=2).pack(pady=30)

    janela.mainloop()
