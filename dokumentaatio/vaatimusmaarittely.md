# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen käyttötarkoitus on vieraan kielen sanaston harjoittelu.
Sovelluksella voi luoda sanalistoja ja luotuja sanalistoja voi harjoitella. Listat muodostuvat sanoista ja niiden käännöksistä. Harjoittelu tapahtuu kirjoittamalla annetun sanan käännös.

## Käyttäjät

Käyttäjärooleja on kaksi. Opettaja ja oppilas joilla on eri oikeuksia.

- Opettaja voi luoda sanalistoja.
- Oppilas voi valita harjoiteltavaksi sanalistan ja tehdä harjoituksen.



## Käyttöliittymäluonnos

Sovellus koostuu kuudesta eri näkymästä

!["Käyttöliittymäluonnos"](kuvat/luonnos.png)

### 1 kirjautumis näkymä

- Sovellus aukeaa kirjautumisnäkymään jossa kysytään käyttäjätunnusta ja salasanaa.
- Mikäli tunnus tai salasana ei ole oikein annetaan siitä ilmoitus.
- Mikäli tunnusta ei ole, sen voi luoda käyttäjätunnuksen-luonti näkymässä.



### 2 käyttäjätunnuksen-luonti näkymä

- Annetaan näyttäjänimi ja salasana.
- Voidaan valita rooliksi opettaja tai oppilas.
- Käyttäjä tunnuksen on oltava uniikki.
- Käyttäjätunnus ja salasana tallennetaan tietokantaan.

### 3 Opettajan aloitusnäkymä

- Opettajan aloitusnäkymässä voi valita joko uuden sanalista tai olemassa olevan sanalistan muokkauksen.
- Muokattavissa olevat sanalistat voidaan jaotella kielen mukaan.


### 4 Opettajan päänäkymä

- Annetaan harjoitukselle nimi ja kieli.
- Annetaan uusi sana ja sille käännös.
- Sanat ja käännökset tallennetaan Tallenna sana painikkeella.
- Sekä sana että sen käännös on kirjoitettava jotta sana voidaan tallentaa.
- Nuolinäppäimillä voidaan siirtyä eteen ja taaksepäin.
- Sanaoja tai käännöksiä voi myös muuttaa.
- Muutokset voidaan perua ja palata pää näkymään.
- Tallenna sanalista painike tallentaa sanalistan.
- Sanalista ei voi olla tyhjä ja sillä on oltava sekä nimi että kieli.


### 5 Oppilaan päänäkymä

- Oppilaan päänäkymässä voi valita tehtävän harjoituksin nimen ja kielen perusteella.
- Siirrytään harjoitus näkymään.
- Ellei sanalistoja ole siitä informoidaan.


### 6 Harjoitus näkymä

- Kysytty sana käännetään ja kirjoitetaan.
- Sana tarkistetaan.
- Palaute sen mukaan onko oikein vai väärin.
- Mikäli tehdään virhe näytetään vihjeenä kirjaimia kunnes sana on oikein tai kaikki kirjaimet on näytetty.
- Kun kaikki sanat on käyty läpi näytetään kyseisen harjoituksen tilasto pylväsgrafiikkana jossa prosentteina oikeiden vastausten osuus.

### Ulkoiset kirjastot

- Sovelluksessa on käytetty numpy ja matplotlib kirjastoja.



## Jatkokehitysideoita

- Sovellukseen voisi lisätä toiminnon joka laatisi opeteltavia sanalistoja automaattisesti annetun tekstin sanastosta tai niin että tietty teksti käytäisiin läpi manuaalisesti ja siitä tallennettaisiin halutut sanat.
- Voisi myös tehdä toiminnon jolla käyttäjä voi halutessaan lisätä itselleen listan sanoista jotka ovat tuottaneet virheitä.
- Listoille voisi luoda automaattiset käännökset eri kielille.
- Käyttöliittymää olisi syytä sujuvoittaa. Tämänhetkinen viestiruuduille perustuva toiminnallisuus on kömpelö oikeaan harjoitteluun. Viestit voisi printata esim. ikkunan yläreunaan tai erilliseen viestipalkkiin.



