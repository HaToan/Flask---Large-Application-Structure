import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY 						= os.environ.get('SECRET_KEY') or 'secret_key'
	SQLALCHEMY_COMMIT_ON_TEARDOWN 	= True
	SQLALCHEMY_TRACK_MODIFICATIONS	= True
	FLASKY_MAIL_SUBJECT_PREFIX 		= '[Flasky]'
	FLASky_MAIL_SENDER 				= 'Flasky Admin <flasky@example.com>'
	FLASKY_ADMIN 					= os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG			=	True
	MAIL_SERVER		=	'smtp.viettel.com.vn'
	MAIL_PORT		=	465
	MAIL_USE_SSL	= 	True
	MAIL_USERNAME	=	os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD	= 	os.environ.get('MAIL_PASSWROD')
	SQLALCHEMY_DATABASE_URI	= os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///'	+	os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING 		= 	True
	SQLALCHEMY_DATABASE_URI	= os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///'	+	os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI	= os.environ.get('DATABASE_URL')	or \
		'sqlite:///'	+	os.path.join(basedir, 'data.sqlite')

config = {
	'development' 	:	DevelopmentConfig,
	'testing'		:	TestingConfig,
	'production'	:	ProductionConfig,
	'default'		:	DevelopmentConfig,
}