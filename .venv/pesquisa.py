from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Rota para o formulário de pesquisa
@app.route('/')
def form():
    return render_template('form.html')

# Rota para processar os dados do formulário
@app.route('/submit', methods=['POST'])
def submit():
    # Obter dados do formulário
    idade = request.form['idade']
    convenio = request.form['convenio']
    faixa_salarial = request.form['faixa_salarial']
    motivo_emprestimo = request.form['motivo_emprestimo']

    # Conectar ao banco de dados
    conn = sqlite3.connect('pesquisa.db')
    c = conn.cursor()

    # Inserir os dados na tabela
    c.execute("INSERT INTO respostas VALUES (?, ?, ?, ?)", (idade, convenio, faixa_salarial, motivo_emprestimo))

    # Salvar as alterações e fechar conexão
    conn.commit()
    conn.close()

    # Redirecionar para uma página de agradecimento
    return redirect(url_for('thanks'))

# Rota para agradecimento após envio do formulário
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
