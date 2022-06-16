import os
import socket
import pdb


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        api_a = os.environ.get('API_A')
        api_b = os.environ.get('API_B')
        api_c = os.environ.get('API_C')

        if not api_a or not api_b or not api_c:
            raise Exception("The API credentials 'API_A', 'API_B' and 'API_C' must be in env variable")
        else:
            return {'api_a': api_a, 'api_b': api_b, 'api_c': api_c}

    @staticmethod
    def get_db_credentials():
        db_ip = os.environ.get('DB_IP')
        db_port = os.environ.get('DB_PORT')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_database = os.environ.get('DB_DATABASE')
        db_charset = os.environ.get('DB_CHARSET')

        if not db_user or not db_password:
            raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in env variable")
        else:
            return {'db_ip': db_ip, 'db_port': db_port, 'db_user': db_user, 'db_password': db_password,
                    'db_database': db_database, 'db_charset': db_charset}

    @staticmethod
    def get_local_ip():
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        return local_ip

    @staticmethod
    def get_user_credentials(ip = None, port = 1433, user = 'sa', password = 'Aspen100', dbName = None, charSet = 'utf8'):
        db_ip = ip
        db_port = port
        db_user = user
        db_password = password
        db_database = dbName
        db_charset = charSet

        if not db_user or not db_password or not db_database:
            raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in env variable")
        else:
            return {'db_ip': db_ip, 'db_port': db_port, 'db_user': db_user, 'db_password': db_password,
                    'db_database': db_database, 'db_charset': db_charset}


