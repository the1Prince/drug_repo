import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:@localhost:3306/drug_repo'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SERCRET_KEY = 'f23e372d-d86c-478b-9735-b1265370675f'
