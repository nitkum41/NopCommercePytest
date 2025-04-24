import configparser

# create configparser object
config = configparser.RawConfigParser()


# read config.ini file

config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info','admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        username = config.get('admin login info', 'invalid_username')
        return username

