from app import db
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=5)  # Voto da 1 a 5
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relazioni
    race = db.relationship('Race')  # backref definito in Race
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    
    def __repr__(self):
        return f'<Review by {self.user.username} on {self.race.name}>'
