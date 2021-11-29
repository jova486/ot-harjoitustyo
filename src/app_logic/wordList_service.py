from entity.user import User

from database.db_service import db_servise as dbs


class word_list_Service:
    """Sovelluslogiikasta vastaa luokka."""

    def __init__(self):
        self.user = None
        self.dbs = dbs
        self.wordlist_info = None
        self.new_wordlist = None
        self.active_wordlist = None

    def check_user(self, username, password):
        row = self.dbs.check_user(username, password)
        if row:
            self.user = User(row[0], row[1], row[2])
            return True
        else:
            return False

    def add_user(self, username, password, is_teacher):

        if self.dbs.add_user(username, password, is_teacher):
            self.user = User(username, password, is_teacher)
            return True
        else:
            return False

    def get_teacher(self):

        return self.user.teacher

    def get_wordlist(self):
        self.new_wordlist = []

        return self.new_wordlist

    def open_active_wordlist(self, name, language):

        self.active_wordlist = dbs.get_word_list(name, language)

    def get_active_wordlist(self):

        return self.active_wordlist

    def save_to_wordlist(self, word, translation, index):

        if index >= len(self.new_wordlist):
            self.new_wordlist.append((word, translation))

        else:
            self.new_wordlist[index] = (word, translation)

    def save_wordlist(self, name):
        language = "Englanti"
        creator = self.user.username
        return dbs.add_word_list(name, language, creator, self.new_wordlist)

    def get_wordlist_info(self):

        self.wordlist_info = dbs.get_word_list_names()
        return self.wordlist_info

    def check_word_list_name(self, name):
        return dbs.check_word_list_name(name)


word_list_Service = word_list_Service()
