#  aqui é um pontuário  médico  gráfico básico  dessenvolvido em python


import tkinter as tk
from tkinter import messagebox

# Função para salvar os dados
def save_data():
    messagebox.showinfo("Informação", "Dados salvos com sucesso!")

# Cria a janela principal
root = tk.Tk()
root.title("PRONTUÁRIO MÉDICO")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Título para o exame clínico-ocupacional
exame_label = tk.Label(frame, text="EXAME CLÍNICO-OCUPACIONAL", font=("Arial", 12, "bold"), fg="green")
exame_label.grid(row=0, column=0, columnspan=2)

# Opções para o tipo de exame
options = ["ADMISSIONAL", "PERIÓDICO", "MUDANÇA DE FUNÇÃO", "RETORNO AO TRABALHO", "DEMISSIONAL"]
exame_option = tk.StringVar()
exame_option.set(options[0])
option_menu = tk.OptionMenu(frame, exame_option, *options)
option_menu.grid(row=1, column=1)

tk.Label(frame, text="Tipo de Exame:").grid(row=1,column=0)

# Campo para a data
tk.Label(frame,text="DATA:").grid(row=2,column=0)
data_entry=tk.Entry(frame)
data_entry.grid(row=2,column=1)

fields_personal=["NOME:", "IDADE:", "RG:", "FUNÇÃO:", "EMPRESA:"]
fields_clinical=["DOENÇAS INFECTOCONTAGIOSAS:",
                 "ALERGIAS:",
                 "CIRURGIAS:",
                 "TRANSFUSÃO SANGUÍNEA:",
                 "MEDICAMENTOS DE USO CONTÍNUO:",
                 "OUTROS:"]

row_count = 3

for field in fields_personal:
    tk.Label(frame,text=f'{field}').grid(row=row_count,column=0)
    entry=tk.Entry(frame)
    entry.grid(row=row_count,column=1)
    row_count += 1

save_button=tk.Button(root,text='Salvar',command=lambda: save_data())
save_button.pack()

root.mainloop()

