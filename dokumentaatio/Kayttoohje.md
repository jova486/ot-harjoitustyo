### Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita tietokannan alustus komennolla:

```bash
poetry run invoke build
```

3. Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```


### Kirjautumis näkymä

- Sovellus aukeaa kirjautumisnäkymään jossa kysytään käyttäjätunnusta.
- Mikäli tunnus tai salasana ei ole sovellus ilmoittaa siitä.
- Mikäli tunnusta ei ole, sen voi luoda käyttäjätunnuksen-luonti näkymässä klikkaamalla Luo Tunnus.

!["Kirjautumis näkymä"](kuvat/login.png)

### Käyttäjätunnuksen-luonti näkymä

- Annetaan käyttäjänimi ja salasana.
- Käyttäjä tunnuksen on oltava uniikki.
- Valitaan halutessa rooliksi opettaja joka antaa mahdollisuuden luoda ja muokata sanalistoja.

!["Käyttäjätunnuksen-luonti"](kuvat/newuser.png)

### Opettajan aloitusnäkymä

- Uusi sanalista painikkeella pääsee päänäkymään tekemään uuden sanalistan
- Muokkaa painikkeella voi valita olemassaolevista listoista muokattavaksi päänäkymään
- Lopeta painikkeella suljetaan sovellus

!["Opettajan aloitusnäkymä"](kuvat/opettaja1.png)

### Opettajan päänäkymä

- Uudelle sanalistalle annetaan nimi
- Listalla pitää olla uniikki nimi ja se ei saa olla tyhjä
- Uudelle sanalistalle annetaan käännösten kieli
- kirjoitetaan sana kenttään Sana ja sen käännös kenttään Käännös.

!["Opettajan päänäkymä"](kuvat/opettaja2.png)

- Nuolinäppäimillä voi liikkua sanalistassa ja tehdä muutoksia
- Tallenna lisää näkyvissä olevan sanan sanalistaan
- Peru painikkeella pääsee takaisin kirjautumisnäkymään.
- Tallenna lista painikkeella tallennetaan lista tietokantaan

!["painikkeet"](kuvat/painikkeet.png)

### Oppilaan päänäkymä

- Valitaan harjoitus.
- Vaidaan valita kieli jonka sanalistat halutaan näyttää.
- Lopeta painikkeella suljetaan sovellus

!["Oppilaan päänäkymä"](kuvat/oppilas1.png)

### Harjoitusnäkymä

- Harjoituksessa kirjoitetaan sanan käännös ja tarkistetaan Tarkista painikkeella

!["Harjoitusnäkymä"](kuvat/oppilas2.png)

- sana oikein

!["Oikein"](kuvat/oikein.png)

-mikäli sana on kirjoitettu väärin annetaan vihjeenä kirjaimia kunnes joko sana on oikein tai kaikki kirjaimet on annettu.

!["vihje"](kuvat/vihje.png)

- Kun kaikki sanat on käännetty oikein näytetään edistymistä kuvaava kaavio jossa tehdyn harjoituksen tilastoidut suoritukset näytetään päivämäärien mukaan. Palkki kuvaa prosentteja ensimmäisellä yrityksellä onnistuneista suhteessa kaikkiin.
- Tämän jälkeen voi palata päänäkymään ja tehdä harjoituksen uudelleen tai valita toisen.

!["stat"](kuvat/oppilas3.png)
