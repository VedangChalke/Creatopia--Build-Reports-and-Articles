##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
