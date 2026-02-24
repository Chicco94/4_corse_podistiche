import os

class Config:
    """Configurazione base"""
    SECRET_KEY = os.environ.get('3d6f45a5fc12445dbac2f59c3b6c7cb1') or 'dev-secret-key'
    DEBUG = False
    # MySQL PythonAnywhere
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Chicco94:Cmhyac_631@Chicco94.mysql.pythonanywhere-services.com/Chicco94$corse_podistiche'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Configurazione di sviluppo"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurazione di produzione"""
    DEBUG = False

class TestingConfig(Config):
    """Configurazione di testing"""
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
