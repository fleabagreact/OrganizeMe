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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        Usuario.criar_usuario(nome, email, senha)
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
    return redirect(url_for('login'))

@app.route('/tarefas', methods=['GET', 'POST'])
@login_required
def tarefas():
    tarefas = Tarefa.listar_tarefas(current_user.id)
    return render_template('tarefas.html', tarefas=tarefas)

@app.route('/tarefas/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar_tarefa():
    if request.method == 'POST':
        descricao = request.form['descricao']
        prioridade = request.form['prioridade']
        data_limite = request.form['data_limite']
        Tarefa.adicionar_tarefa(current_user.id, descricao, prioridade, data_limite)
        flash('Tarefa adicionada com sucesso!', 'sucesso')
        return redirect(url_for('tarefas'))
    return render_template('adicionar_tarefa.html')

if __name__ == '__main__':
    app.run(debug=True)