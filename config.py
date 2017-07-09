import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	#SECRET_KEY = os.environ['SECRET_KEY'] or 'bonfire'
	SECRET_KEY = 'bonfire'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	#SQLALCHEMY_DATABASE_URI = os.environ['DEV_DATABASE_URI'] or 'sqlite:///' + os.path.join(basedir, 'data_dev.sqlite')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data_dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	#SQLALCHEMY_DATABASE_URI = os.environ['TEST_DATABASE_URI'] or 'sqlite:///' + os.path.join(basedir, 'data_test.sqlite')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data_test.sqlite')

class ProductionConfig(Config):
	#SQLALCHEMY_DATABASE_URI = os.environ['PROD_DATABASE_URI'] or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig,
	'production' : ProductionConfig,
	'default' : DevelopmentConfig
}