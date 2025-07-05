import tkinter as tk
from tkinter import messagebox

# Variáveis globais para armazenar as credenciais
email_registrado = ""
senha_registrada = ""

def abrir_janela_cadastro():
    """Abre a janela de cadastro de novas credenciais"""
    def confirmar_cadastro():
        global email_registrado, senha_registrada
        
        email = entrada_email.get()
        senha = entrada_senha.get()
        confirmacao = entrada_confirmacao.get()
        
        if not email or not senha:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
            
        if senha != confirmacao:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return
            
        email_registrado = email
        senha_registrada = senha
        messagebox.showinfo("Sucesso", "Credenciais cadastradas com sucesso!")
        janela_cadastro.destroy()
    
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("300x200")
    
    tk.Label(janela_cadastro, text="Cadastre suas credenciais").pack(pady=10)
    
    tk.Label(janela_cadastro, text="Email:").pack()
    entrada_email = tk.Entry(janela_cadastro)
    entrada_email.pack()
    
    tk.Label(janela_cadastro, text="Senha:").pack(pady=(5, 0))
    entrada_senha = tk.Entry(janela_cadastro, show="*")
    entrada_senha.pack()
    
    tk.Label(janela_cadastro, text="Confirmar Senha:").pack(pady=(5, 0))
    entrada_confirmacao = tk.Entry(janela_cadastro, show="*")
    entrada_confirmacao.pack()
    
    tk.Button(janela_cadastro, text="Confirmar", command=confirmar_cadastro).pack(pady=10)

def abrir_janela_login():
    """Abre a janela de login com as credenciais cadastradas"""
    def validar_login():
        email = entrada_email.get()
        senha = entrada_senha.get()
        
        if email == email_registrado and senha == senha_registrada:
            messagebox.showinfo("Login", "Bem-vindo!")
        else:
            messagebox.showerror("Erro", "Algo está errado, tente novamente!")
    
    janela_login = tk.Toplevel()
    janela_login.title("Login")
    janela_login.geometry("300x200")
    
    tk.Label(janela_login, text="Faça login").pack(pady=10)
    
    tk.Label(janela_login, text="Email:").pack()
    entrada_email = tk.Entry(janela_login)
    entrada_email.pack()
    
    tk.Label(janela_login, text="Senha:").pack(pady=(5, 0))
    entrada_senha = tk.Entry(janela_login, show="*")
    entrada_senha.pack()
    
    tk.Button(janela_login, text="Entrar", command=validar_login).pack(pady=10)

# Janela principal
root = tk.Tk()
root.title("Sistema de Autenticação")
root.geometry("400x150")

tk.Label(root, text="Selecione uma opção:").pack(pady=10)

tk.Button(root, text="Cadastrar Credenciais", 
          command=abrir_janela_cadastro).pack(pady=5)
tk.Button(root, text="Fazer Login", 
          command=abrir_janela_login).pack(pady=5)

root.mainloop()
