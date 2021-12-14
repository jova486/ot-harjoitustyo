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
- Mikäli tunnusta ei ole, sen voi luoda käyttäjätunnuksen-luonti näkymässä klikkaamalla Luo Tunnus.



### Käyttäjätunnuksen-luonti näkymä

- Annetaan käyttäjänimi ja salasana.
- Käyttäjä tunnuksen on oltava uniikki.
- Valitaan halutessa rooliksi opettaja joka antaa mahdollisuuden luoda ja muokata sanalistoja.
- käyttäjätunnus, salasana ja rooli tallennetaan tietokantaan


### Opettajan aloitusnäkymä

- Uusi sanalista painikkeella pääsee päänäkymään tekemään uuden sanalistan
- Mahdollisuus valita olemassaolevista listoista muokattavaksi päänäkymään
- Lopetus

### Opettajan päänäkymä

- Uudelle sanalistalle annetaan nimi
- Uudelle sanalistalle annetaan käännösten kieli
- kirjoitetaan sana kenttään Sana ja sen käännös kenttään Käännös.
- Nuolinäppäimillä voi liikkua sanalistassa ja tehdä muutoksia
- Tallenna lisää näkyvissä olevan sanan sanalistaan
- Peru painikkeella pääsee takaisin kirjautumisnäkymään.
- Tallenna lista painikkeella tallennetaan lista tietokantaan
- Listalla pitää olla uniikki nimi ja se ei saa olla tyhjä

### Oppilaan päänäkymä

- Valitaan harjoitus.
- Vaidaan valita kieli jonka sanalistat halutaan näyttää.
- Lopetus

### Harjoitusnäkymä

- Harjoituksessa kirjoitetaan sanan käännös ja tarkistetaan
- Kun kaikki sanat on käännetty oikein palataan oppilaan päänäkymään
- Tämän jälkeen näytetään edistymistä kuvaava kaavio jossa tehdyn harjoituksen tilastoidut suoritukset
näytetään päivämäärien mukaan. Palkki kuvaa prosentteja ensimmäisellä yrityksellä onnistuneista suhteessa kaikkiin.