# Ohjelmistotekniikka, harjoitustyö


# Sanalista

Sovelluksen avulla voi harjoitella toisen kielen sanastoa. 
Sovelluksessa luodaan sanalistoja käännöksineen joita voi harjoitella kääntämään halutulle kielelle.

## Python-versio

Sovelluksen toiminta on testattu Python-versioilla 3.6.9 ja 3.8.8



## Dokumentaatio

[Käyttöohje.md].(https://github.com/jova486/ot-harjoitustyo/blob/main/dokumentaatio/K%C3%A4ytt%C3%B6ohje.md)


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

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```



