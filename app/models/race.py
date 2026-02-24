from app import db
from datetime import datetime

class Race(db.Model):
    __tablename__ = 'races'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relazione con le recensioni
    reviews = db.relationship('Review', backref='race', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Race {self.name} - {self.date.strftime("%d/%m/%Y")}>'
