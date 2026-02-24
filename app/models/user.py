from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relazione con le corse create
    races_created = db.relationship('Race', backref='creator', lazy=True, foreign_keys='Race.creator_id')
    
    def __repr__(self):
        return f'<User {self.username}>'
