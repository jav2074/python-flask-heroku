from flask import Flask
from bd import db_init
from config import config

def create_app(config_name):
	app = Flask(__name__)
	
	current_config = config[config_name]
	app.config.from_object(current_config)

	db_init(current_config)

	return app