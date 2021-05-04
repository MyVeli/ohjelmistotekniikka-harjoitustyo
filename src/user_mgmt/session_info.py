class SessionInfo:
    """Holds login information and database connection.
    """
    def __init__(self):
        self.__db_connection__ = None
        self.__username__ = None
    
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
    
    def set_username(self,username):
        """Used for setting the logged in users username.

        Args:
            username (string): username
        """
        self.__username__ = username
        