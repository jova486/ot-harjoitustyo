# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen käyttötarkoitus on vieraan kielen sanaston harjoittelu. 
Sovelluksen pääkieli on suomi
Harjoitus tehdään kirjottamalla suomesta käännetty sana halutulla kielellä

## Käyttäjät

Käyttäjärooleja on kaksi. Opettaja ja oppilas joilla on eri oikeuksia. 

- Opettaja voi luoda harjoituksia jotka koostuvat sanalistoista ja niiden käännöksistä. 
- oppilas voi valita tehtävän harjoituksen listalta



## Käyttöliittymäluonnos

Sovellus koostuu kahdeksasta kymmeneen eri näkymästä

!["Käyttöliittymäluonnos"](kuvat/luonnos.jpg)

### 1 kirjautumis näkymä

- Sovellus aukeaa kirjautumisnäkymään jossa kysytään käyttäjätunnusta. Mikäli tunnusta ei ole sen voi luoda.
- Mikäli tunnus tai salasana ei ole oikein annetaan siitä ilmoitus 
- mikäli tunnusta ei ole, sen voi luoda käyttäjätunnuksen-luonti näkymässä



### 2 käyttäjätunnuksen-luonti näkymä

- Annetaan näyttäjänimi ja salasana
- voidaan valita rooliksi opettaja tai oppilas
- käyttäjä tunnuksen on oltava uniikki
- käyttäjätunnus ja salasana tallennetaan tietokantaan


### 3 Opettajan päänäkymä

- Opettajan päänäkymässä voi valita joko uuden harjoituksen tai lopetuksen 
- Harjoitukselle annetaan nimi (pakollinen)
- Harjoitukselle annetaan kuvaus
- Määritellään harjoituksen kieli (pakollinen)
- Lopetus
- Harjoitukset tallennetaan tietokantaan



### 4 Uuden harjoituksen luonti näkymä

- annetaan uusi sana ja sille käännös
- nuolinäppäimillä voidaan siirtyä eteen ja taaksepäin
- harjoitus voidaan tallentaa
- muutokset voidaan perua ja palata pää näkymään

### 5 Muokattavan harjoituksen valinta näkymä

- voidaan valita harjoitus nimen ja kielen perusteella vain itse luoduista harjoituksista
- voidaan perua ja siirtyä takaisin päänäkymään
- voidaan siirtyä uuden harjoituksen luonti näkymään muokkaamaan olemassa olevaa harjoitusta

### 6 Oppilaan päänäkymä

- Oppilaan päänäkymässä voi valita tehtävän harjoituksin nimen ja kielen perusteella
- siirrytään harjoitus näkymään
- lopetus.

### 7 Oppilaan päänäkymä

- Oppilaan päänäkymässä voi valita tehtävän harjoituksin nimen ja kielen perusteella
- siirrytään harjoitus näkymään
- lopetus.

### 8 Harjoitus näkymä

- Kysytty sana käännetään ja kirjoitetaan
- tarkistus
- palaute sen mukaan onko oikein vai
- lopetus.


## Jatkokehitysideoita

Mikäli aika sallii lisätään toiminnallisuutta:
- olemassaolevan harjoituksen muokkaus 
- pidetään kirjaa tuloksista 
- statistiikka näkymä sekä opettajalle että oppilaalle



