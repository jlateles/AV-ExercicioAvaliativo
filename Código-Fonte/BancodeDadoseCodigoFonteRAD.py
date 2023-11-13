import tkinter as tk
import psycopg2
#Conectando com o BD e criando (CREATE) a tabela
conn =psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
comando = conn.cursor()
comando.execute(""" CREATE TABLE Livros
(id INT PRIMARY KEY NOT NULL,Autor TEXT NOT NULL,Titulo_livro TEXT NOT NULL,Editora TEXT NOT NULL,Ano CHAR(4),Genero TEXT NOT NULL, Preco CHAR(5) );""")
conn.commit()
print("Tabela criada com sucesso no BD!!!")
conn.close

import psycopg2
conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
comando = conn.cursor()
comando.execute (""" INSERT INTO LIVROS (id,Autor,Titulo_livro,Ano,Editora,Genero,Preco) VALUES ()""")

# função dos botões
def cadastrar_livro(autor,titulo_livro,ano,editora,genero,preco):
 autor = entry_autor.get()
 titulo_livro = entry_titulo_livro.get()
 editora = entry_editora.get()
 ano = entry_ano.get()
 genero = entry_genero.get()
 preco = float(entry_preco.get()) # Converte o preço para float
# Calcula o preço com a taxa de 10%
def acrescimo_dez_por_cento(preco):
    return preco * 1.10
conn.commit()
print("Inserção realizada com sucesso!")
conn.close()

def ler_livro():
 import psycopg2
 conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
 comando = conn.cursor()
 comando.execute (""" SELECT * FROM LIVROS where id = %s""")
 resultado = comando.fetchone()
 print("Livro encontrado ->", resultado)
 conn.commit()
 print("Seleção realizada com sucesso!")
 conn.close()
 
def atualizar_livro():
 import psycopg2
 conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
 comando = conn.cursor()
 comando.execute(""" SELECT * FROM LIVROS where id = %s""")
 resultado = comando.fetchone()
 print("Livro encontrado ->", resultado)
 comando.execute(""" UPDATE LIVROS SET id = %s, Autor = %s, Titulo_livro = %s, Ano = %s,
 Editora = %s, Genero = %s, Preco = %s, where id = %s""")
 print("Atualização realizada com sucesso!")
 comando = conn.cursor()
 print("--- Consulta após atualização ---")
 comando.execute(""" SELECT * FROM LIVROS where id = %s""")
 resultado = comando.fetchone()
 print("Dados atualizados ->", resultado)
 conn.commit()
 print("Livro atualizado com sucesso!")
 conn.close()

def excluir_livro():
 import psycopg2
 conn = psycopg2.connect(database="postgres",user="postgres",password="1234",port="5432")
 comando = conn.cursor()
 comando.execute(""" DELETE FROM LIVROS where id = %s""")
 conn.commit()
 cont = comando.rowcount
 print(cont, '-> Registro(s) excluído(s) com sucesso!')
 conn.close()
 print("Livro excluído com sucesso!")
 
def limpar_campos():
 entry_nome.delete(0, tk.END)
 entry_autor.delete(0, tk.END)
 entry_editora.delete(0, tk.END)
 entry_ano.delete(0, tk.END)
 entry_genero.delete(0, tk.END)
 
# configuração da janela principal
root = tk.Tk()
root.title("Sistema de cadastramento de livros virtuais")
# campos de entrada para as informações do livro
label_nome = tk.Label(root, text="Nome do Livro:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()
label_autor = tk.Label(root, text="Autor:")
label_autor.pack()
entry_autor = tk.Entry(root)
entry_autor.pack()
label_editora = tk.Label(root, text="Editora:")
label_editora.pack()
entry_editora = tk.Entry(root)
entry_editora.pack()
label_ano = tk.Label(root, text="Ano de Publicação:")
label_ano.pack()
entry_ano = tk.Entry(root)
entry_ano.pack()
label_genero = tk.Label(root, text="Gênero:")
label_genero.pack()
entry_genero = tk.Entry(root)
entry_genero.pack()
label_preco = tk.Label(root, text="Preço:")
label_preco.pack()
entry_preco = tk.Entry(root)
entry_preco.pack()
# botões
btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_livro)
btn_cadastrar.pack()
btn_atualizar = tk.Button(root, text="Atualizar", command=atualizar_livro)
btn_atualizar.pack()
btn_excluir = tk.Button(root, text="Excluir", command=excluir_livro)
btn_excluir.pack()
btn_limpar = tk.Button(root, text="Limpar", command=limpar_campos)
btn_limpar.pack()
root.mainloop()

