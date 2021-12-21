class User:
    """Käyttäjää kuvaava luokka.

    Attributes:
        username: Käyttäjänimi
        password: Salasana
        teacher: Kokonaislukuarvo: 1 = opettaja, 0 = oppilas
    """

    def __init__(self, username, password, teacher):
        """Luokan konstruktori.

        Args:
            username: Käyttäjänimi
            password: Salasana
            teacher: Kokonaislukuarvo: 1 = opettaja, 0 = oppilas
        """

        self.username = username
        self.password = password
        self.teacher = teacher


    def __init__(self, username, password):
