class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@localhost:3306/hzmc"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO =True

