import os

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')

class Development(Config):
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or '¡?¡asdfghjklñ[}{_.;.876543nbvc+´*¨¿?¡oiuytr¿¡ñlkjhg{}lkjhgf[]nbvcx;:_kjhg-.,qwerty'
	DB_DIR = os.path.abspath(os.getcwd()) + "/h_database.db"

class Testing(Config):
	TESTING = True

class Production(Config):
	pass	

config = {
	'development': Development,
	'testing': Testing,
	'production': Production,

	'default': Development
}