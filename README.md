# Ohjelmistotekniikka, harjoitustyö


# Sanalista

Sovelluksen avulla voi harjoitella toisen kielen sanastoa.
Sovelluksella voi luoda erikielisiä sanalistoja käännöksineen. Sanalistojen muistamista ja oikeinkirjoitusta voi harjoitella.

## Python-versio

Sovelluksen toiminta on testattu Python-versioilla 3.8.12 ja 3.8.8



## Dokumentaatio

- [Käyttöohje](./dokumentaatio/Kayttoohje.md)

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](./dokumentaatio/testaus.md)

- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)



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

### Testaus

Testit voi suorittaa komennoilla:

```bash
poetry run invoke test
```

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Pylint tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```


## Release

- [Release](https://github.com/jova486/ot-harjoitustyo/releases/tag/Final)




