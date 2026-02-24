from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db
from app.models import User, Race, Review
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

@bp.route('/races/new', methods=['GET', 'POST'])
def create_race():
    # Verifica che l'utente sia loggato
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        date_str = request.form.get('date', '').strip()
        
        # Validazione
        if not name:
            return render_template('create_race.html', error='Inserisci il nome della gara')
        if not date_str:
            return render_template('create_race.html', error='Inserisci la data della gara')
        
        try:
            from datetime import datetime
            race_date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            return render_template('create_race.html', error='Formato data non valido (YYYY-MM-DD)')
        
        # Crea la gara
        race = Race(
            name=name,
            date=race_date,
            creator_id=session['user_id']
        )
        db.session.add(race)
        db.session.commit()
        
        return redirect(url_for('main.race_detail', race_id=race.id))
    
    return render_template('create_race.html')

@bp.route('/races/<int:race_id>')
def race_detail(race_id):
    race = Race.query.get_or_404(race_id)
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    return render_template('race_detail.html', race=race, user=user)

@bp.route('/races/<int:race_id>/reviews', methods=['POST'])
def add_review(race_id):
    # Verifica che l'utente sia loggato
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    
    race = Race.query.get_or_404(race_id)
    content = request.form.get('content', '').strip()
    rating = request.form.get('rating', '5')
    
    # Validazione
    if not content:
        return render_template('race_detail.html', race=race, error='Inserisci un commento')
    
    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            rating = 5
    except ValueError:
        rating = 5
    
    # Crea la recensione
    review = Review(
        content=content,
        rating=rating,
        race_id=race_id,
        user_id=session['user_id']
    )
    db.session.add(review)
    db.session.commit()
    
    return redirect(url_for('main.race_detail', race_id=race_id))
