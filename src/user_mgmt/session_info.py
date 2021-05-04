class SessionInfo:
    def __init__(self):
        self.__db_connection__ = None
        self.__username__ = None
    
    def get_db_connection(self):
        return self.__db_connection__
    
    def set_db_connection(self,db_connection):
        self.__db_connection__ = db_connection
    
    def get_username(self):
        return self.__username__
    
    def set_username(self,username):
        self.__username__ = username
        