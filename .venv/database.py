import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('pesquisa.db')
c = conn.cursor()

# Criar tabela para armazenar respostas
c.execute('''CREATE TABLE respostas
             (idade TEXT, convenio TEXT, faixa_salarial TEXT, motivo_emprestimo TEXT)''')

# Salvar as alterações
conn.commit()

# Fechar conexão
conn.close()
