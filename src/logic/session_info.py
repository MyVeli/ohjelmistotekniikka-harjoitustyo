from data_service.login import user_login
from data_service.register import register_user

class SessionInfo:
    """Holds login information and database connection.
    """
    def __init__(self):
        self.__db_connection__ = None
        self.__username__ = None

    def login(self, username, password):
        """used for logging in

        Args:
            username (string): username for logging in
            password (string): password for logging in

        Raises:
            e: passes on exception from login service. Can raise CredentialError or ConnectionError
        """

        try:
            self.__username__ = user_login(username, password, self.__db_connection__)
        except Exception as _e:
            raise _e

    def register(self, username, password):
        """used for registering new user and logging them in

        Args:
            username (string): username for registration
            password (string): password for registration

        Raises:
            e: passes on exception from registration service. Can raise UsernameError, PasswordError
            or ConnectionError
        """
        try:
            self.__username__ = register_user(username, password, self.__db_connection__)
        except Exception as _e:
            raise _e

    def get_db_connection(self):
        """returns sqlite3 database connection.

        Returns:
            sqlite3 connection: database connection
        """
        return self.__db_connection__

    def set_db_connection(self,db_connection):
        """Used for setting the database connection.

        Args:
            db_connection (sqlite3 connection): connection for the db used in the system
        """
        self.__db_connection__ = db_connection

    def get_username(self):
        """returns usename of the logged user

        Returns:
            string: username
        """
        return self.__username__
