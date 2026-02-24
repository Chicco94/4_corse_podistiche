from app import db
from datetime import datetime

class Race(db.Model):
    __tablename__ = 'races'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    place = db.Column(db.String(120), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relazione con le corse create
    reviews = db.relationship('Review', backref='race', foreign_keys='Review.race_id', lazy=True)
    
    def __repr__(self):
        return f'<Race {self.name} - {self.place}>'

    @property
    def reviews_count(self):
        return len(self.reviews or [])

    @property
    def average_rating(self):
        """Restituisce la media aggregata di tutte le recensioni per questa gara (float) o None se nessuna recensione."""
        if not self.reviews:
            return None
        totals = 0.0
        for r in self.reviews:
            # ogni recensione ha 8 valori di rating
            s = (
                (r.rating_percorso_segnaletica or 0)
                + (r.rating_percorso_fondo or 0)
                + (r.rating_percorso_distanza or 0)
                + (r.rating_ristori_numero or 0)
                + (r.rating_ristori_varieta or 0)
                + (r.rating_ristoro_abusivo or 0)
                + (r.rating_ristoro_finale or 0)
                + (r.rating_extra_organizzazione or 0)
            )
            totals += (s / 8.0)
        return totals / len(self.reviews)
