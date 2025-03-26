from database import criar_tabelas, criar_usuario_inicial
from login import tela_login

if __name__ == "__main__":
    criar_tabelas()
    criar_usuario_inicial()
    tela_login()
