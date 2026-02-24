from app import db
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Percorso valutato
    route = db.Column(db.String(120), nullable=False)

    # Valutazione del percorso
    rating_percorso_segnaletica = db.Column(db.Integer, nullable=False, default=5)
    rating_percorso_fondo = db.Column(db.Integer, nullable=False, default=5)
    rating_percorso_distanza = db.Column(db.Integer, nullable=False, default=5)

    # Valutazione ristori
    rating_ristori_numero = db.Column(db.Integer, nullable=False, default=5)
    rating_ristori_varieta = db.Column(db.Integer, nullable=False, default=5)
    rating_ristoro_abusivo = db.Column(db.Integer, nullable=False, default=5)
    rating_ristoro_finale = db.Column(db.Integer, nullable=False, default=5)

    # Valutazione extra
    rating_extra_organizzazione = db.Column(db.Integer, nullable=False, default=5)
    
    # Note dell'utente
    content = db.Column(db.Text, nullable=False)



    def __repr__(self):
        return f'<Review by {self.user.username} on {self.race.name}>'
