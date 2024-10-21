from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import Usuario, Tarefa

app = Flask(__name__)
app.secret_key = 'chave_secreta'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    usuario = Usuario.buscar_por_id(user_id)
    if usuario:
        return User(usuario['id'], usuario['nome'], usuario['email'])
    return None

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        Usuario.criar_usuario(nome, email, senha)
        usuario = Usuario.buscar_por_email(email)
        if usuario:
            user = User(usuario['id'], usuario['nome'], usuario['email'])
            login_user(user)
            flash('Registro realizado com sucesso!', 'sucesso')
            return redirect(url_for('tarefas'))
    return render_template('registrar.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.buscar_por_email(email)
        if usuario and Usuario.verificar_senha(usuario['senha'], senha):
            user = User(usuario['id'], usuario['nome'], usuario['email'])
            login_user(user)
            return redirect(url_for('tarefas'))
        else:
            flash('Credenciais inválidas', 'erro')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('index'))

@app.route('/tarefas', methods=['GET', 'POST'])
@login_required
def tarefas():
    tarefas = Tarefa.listar_tarefas(current_user.id)
    return render_template('tarefas.html', tarefas=tarefas)

@app.route('/tarefas/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        data_limite = request.form['data_limite']
        id_status = request.form['id_status']
        id_prioridade = request.form['id_prioridade']
        id_categoria = request.form['id_categoria']
        Tarefa.adicionar_tarefa(current_user.id, titulo, descricao, data_limite, id_status, id_prioridade, id_categoria)
        flash('Tarefa adicionada com sucesso!', 'sucesso')
        return redirect(url_for('tarefas'))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM status_tarefa')
    status_tarefas = cursor.fetchall()
    
    cursor.execute('SELECT * FROM prioridade_tarefa')
    prioridade_tarefas = cursor.fetchall()
    
    cursor.execute('SELECT * FROM categoria_tarefa')
    categoria_tarefas = cursor.fetchall()
    
    cursor.close()
    connection.close()

    return render_template('adicionar_tarefa.html', status_tarefas=status_tarefas, prioridade_tarefas=prioridade_tarefas, categoria_tarefas=categoria_tarefas)

if __name__ == '__main__':
    app.run(debug=True)