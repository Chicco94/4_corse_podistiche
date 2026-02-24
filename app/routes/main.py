from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db
from app.models import User
import git

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    return render_template('index.html', user=user)


@bp.route('/update_server', methods=['POST'])
def webhook():
	if request.method == 'POST':
		repo = git.Repo('/home/Chicco94/4_corse_podistiche/')
		origin = repo.remotes.origin
		origin.pull('main')
		return 'Updated PythonAnywhere successfully', 200
	else:
		return 'Wrong event type', 400


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        
        if not username:
            return render_template('login.html', error='Inserisci un nome utente')
        
        # Cerca l'utente nel DB
        user = User.query.filter_by(username=username).first()
        
        # Se non esiste, lo crea
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
        
        # Salva l'utente nella sessione
        session['user_id'] = user.id
        session['username'] = user.username
        
        return redirect(url_for('main.index'))
    
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))
