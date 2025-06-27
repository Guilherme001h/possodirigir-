import customtkinter as ctk

# Configura o modo e tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Cria janela
app = ctk.CTk()
app.title("Verificação de Habilitação")
app.geometry("400x300")

# Função para verificar habilitação
def verificar_habilitacao():
    nome = entry_nome.get().strip()
    idade_input = entry_idade.get().strip()

    if not nome:
        resultado_label.configure(text="Você precisa informar o nome.", text_color="red")
        return

    if not idade_input:
        resultado_label.configure(text="Você precisa informar a idade.", text_color="red")
        return

    try:
        idade = int(idade_input)
    except ValueError:
        resultado_label.configure(text="A idade precisa ser um número inteiro.", text_color="red")
        return

    if idade >= 18:
        resultado_label.configure(text=f"{nome}, você está apto(a) a dirigir!", text_color="green")
    else:
        resultado_label.configure(text=f"{nome}, você NÃO está apto(a) a dirigir.", text_color="orange")

# Widgets
label_titulo = ctk.CTkLabel(app, text="Verificação de Habilitação", font=("Arial", 20))
label_titulo.pack(pady=10)

label_nome = ctk.CTkLabel(app, text="Nome:")
label_nome.pack(pady=(10, 0))
entry_nome = ctk.CTkEntry(app, width=200)
entry_nome.pack()

label_idade = ctk.CTkLabel(app, text="Idade:")
label_idade.pack(pady=(10, 0))
entry_idade = ctk.CTkEntry(app, width=200)
entry_idade.pack()

botao_verificar = ctk.CTkButton(app, text="Verificar", command=verificar_habilitacao)
botao_verificar.pack(pady=20)

resultado_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
resultado_label.pack()

# Inicia o loop da aplicação
app.mainloop()
