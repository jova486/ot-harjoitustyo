# Ohjelmistotekniikka, harjoitustyö


# Sanalista

Sovelluksen avulla voi harjoitella toisen kielen sanastoa.
Sovelluksessa luodaan sanalistoja käännöksineen joita voi harjoitella kääntämään halutulle kielelle.

## Python-versio

Sovelluksen toiminta on testattu Python-versioilla 3.8.12 ja 3.8.8



## Dokumentaatio

- [Käyttöohje](./dokumentaatio/Kayttoohje.md)


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

### Testaus

Testit voi suorittaa komennoilla:

```bash
poetry run invoke test
```

```bash
poetry run invoke coverage-report
```

```bash
poetry run invoke lint
```


## Tuntikirjanpito

- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Vaatimusmäärittely

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

## Arkkitehtuurikuvaus

- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)


## Release

- [Release](https://github.com/jova486/ot-harjoitustyo/releases/tag/viikko5_1)




