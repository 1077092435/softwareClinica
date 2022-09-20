class Config:
    SECRET_KEY = '12345'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'software_clinica'

config = {
    'development': DevelopmentConfig
}