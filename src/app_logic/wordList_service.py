from entity.word_list import WordList
from entity.user import User

from database.db_service import (
    db_servise as dbs
)


class word_list_Service:
    """Sovelluslogiikasta vastaa luokka."""

    def __init__(
        self
    ):
        self._user = None
        
        
        self.dbs = dbs
        
    def check_user(self, username, password):
        

        if self.dbs.check_user(username, password):
            self._user = username
            return True
        else:
            return False



    def add_user(self, username, password):

        if self.dbs.add_user(username, password):
            self._user = username
            return True
        else:
            return False


word_list_Service = word_list_Service()

