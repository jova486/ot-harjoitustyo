
class WordList:
    """Luokka, joka kuvaa sanalista oliota

    Attributes:
        name: Sanalistan nimi.
        language: Sanalistan kieli.
        user: Sanalistan tekijän käyttäjätunnus 
    """

    def __init__(self, name, language, user):
        """Luokan konstruktori, joka luo tyhjän sanalistan.

        Args:
            language: Kuvaa sanalistan toista kieltä.
            user: Sanalistan tekijän käyttäjätunnus 
        """

        self.name = name
        self.language = language
        self.user = user
        self.words 

    def addWord(self, fi,translation):
        self.words.append((fi,translation))


        