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
        place = request.form.get('place', '').strip()
        
        # Validazione
        if not name:
            return render_template('create_race.html', error='Inserisci il nome della gara')
        if not place:
            return render_template('create_race.html', error='Inserisci il luogo della gara')
        
        # Crea la gara
        race = Race(
            name=name,
            place=place,
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
    
    # Estrai i dati dal form
    route = request.form.get('route', '').strip()
    content = request.form.get('content', '').strip()
    
    # Validazione
    if not route:
        return render_template('race_detail.html', race=race, error='Inserisci il percorso valutato')
    if not content:
        return render_template('race_detail.html', race=race, error='Inserisci le note')
    
    # Estrai i rating
    try:
        rating_percorso_segnaletica = int(request.form.get('rating_percorso_segnaletica', 5))
        rating_percorso_fondo = int(request.form.get('rating_percorso_fondo', 5))
        rating_percorso_distanza = int(request.form.get('rating_percorso_distanza', 5))
        rating_ristori_numero = int(request.form.get('rating_ristori_numero', 5))
        rating_ristori_varieta = int(request.form.get('rating_ristori_varieta', 5))
        rating_ristoro_abusivo = int(request.form.get('rating_ristoro_abusivo', 5))
        rating_ristoro_finale = int(request.form.get('rating_ristoro_finale', 5))
        rating_extra_organizzazione = int(request.form.get('rating_extra_organizzazione', 5))
        
        # Valida i rating (1-5)
        for rating in [rating_percorso_segnaletica, rating_percorso_fondo, rating_percorso_distanza,
                       rating_ristori_numero, rating_ristori_varieta, rating_ristoro_abusivo,
                       rating_ristoro_finale, rating_extra_organizzazione]:
            if rating < 1 or rating > 5:
                rating = 5
    except ValueError:
        return render_template('race_detail.html', race=race, error='Valori rating non validi')
    
    # Crea la recensione
    review = Review(
        route=route,
        content=content,
        rating_percorso_segnaletica=rating_percorso_segnaletica,
        rating_percorso_fondo=rating_percorso_fondo,
        rating_percorso_distanza=rating_percorso_distanza,
        rating_ristori_numero=rating_ristori_numero,
        rating_ristori_varieta=rating_ristori_varieta,
        rating_ristoro_abusivo=rating_ristoro_abusivo,
        rating_ristoro_finale=rating_ristoro_finale,
        rating_extra_organizzazione=rating_extra_organizzazione,
        race_id=race_id,
        user_id=session['user_id']
    )
    db.session.add(review)
    db.session.commit()
    
    return redirect(url_for('main.race_detail', race_id=race_id))
