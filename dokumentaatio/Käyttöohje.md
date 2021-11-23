### Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita tietokannan alustus komennolla:

```bash
poetry run invoke initdb
```

3. Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```


### Kirjautumis näkymä

- Sovellus aukeaa kirjautumisnäkymään jossa kysytään käyttäjätunnusta.
- Mikäli tunnus tai salasana ei ole sovellus ilmoittaa siitä. 
- mikäli tunnusta ei ole, sen voi luoda käyttäjätunnuksen-luonti näkymässä klikkaamalla Luo Tunnus.



### Käyttäjätunnuksen-luonti näkymä

- Annetaan käyttäjänimi ja salasana
- käyttäjä tunnuksen on oltava uniikki
- käyttäjätunnus ja salasana tallennetaan tietokantaan


### Opettajan päänäkymä

- Uudelle sanalistalle annetaan nimi 
- kirjoitetaan sana kenttään Sana ja sen käännös kenttään Käännös.
- Nuolinäppäimillä voi liikkua sanalistassa ja tehdä muutoksia (Työn alla. Ei toimiva)
- Tallenna lisää sanan sanalistaan (Ainoastaan muistiin. Tietokantatallennusta ei vielä ole)
- Peru painikkeella pääsee takaisin kirjautumisnäkymään.
