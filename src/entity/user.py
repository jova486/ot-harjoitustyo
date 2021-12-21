class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.
    Attributes:
        username: Käyttäjätunnus.
        password: Salasana
        teacher: Kokonaislukuarvo 1 = opettaja 0 = oppilas
    """

    def __init__(self, username, password, teacher):
        """Luokan konstruktori.
        Args:
            username: Käyttäjätunnus.
            password: Salasana
            teacher: Kokonaislukuarvo 1 = opettaja 0 = oppilas
        """

        self.username = username
        self.password = password
        self.teacher = teacher
