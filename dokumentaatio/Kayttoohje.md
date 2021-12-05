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


### Opettajan aloitusnäkymä

- Uusi sanalista painikkeella pääsee päänäkymään tekemään uuden sanalistan
- Mahdollisuus valita olemassaolevista listoista muokattavaksi päänäkymään
- Lopetus

### Opettajan päänäkymä

- Uudelle sanalistalle annetaan nimi
- kirjoitetaan sana kenttään Sana ja sen käännös kenttään Käännös.
- Nuolinäppäimillä voi liikkua sanalistassa ja tehdä muutoksia
- Tallenna lisää sanan sanalistaan
- Peru painikkeella pääsee takaisin kirjautumisnäkymään.
- Tallenna lista painikkeella tallennetaan lista tietokantaan
- Listalla pitää olla uniikki nimi ja se ei saa olla tyhjä
- Paluu opettajan aloitusnäkymään

### Oppilaan päänäkymä

- Valitaan harjoitus
- Lopetus

### Harjoitusnäkymä

- Harjoituksessa kirjoitetaan sanan käännös ja tarkistetaan
- kun kaikki sanat on käännetty oikein palataan oppilaan päänäkymään