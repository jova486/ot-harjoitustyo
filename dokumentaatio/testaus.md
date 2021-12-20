# Testausdokumentti

Ohjelmaa on testattu unittestin yksikkötesteillä ja manuaalisesti [Käyttöohjeen](Kayttoohje.md) kuvaamalla tavalla.


# Sovelluslogiikka

Sovelluslogiikasta vastaavaa `WordListService`-luokkaa testataan `TestServise` luokan metodeilla. `TestServise`-luokan metodissa setUp tyhjennetään tietokanta wordlistdb siten että tietokantahaut ja testit tehdään tyhjälle tietokannalle.
# Tietokanta-luokka

Tietokantaluokkaa `DbServise` testataan luokan `TestDbServise` luokan metodeilla. `TestDbServise`-luokan metodissa setUp tyhjennetään tietokanta wordlistdb siten että  tietokantahaut ja testit tehdään tyhjälle tietokannalle.

# Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 96%

![](./kuvat/testikattavuus.png)


# Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

# Asennus ja konfigurointi

Sovelluksen release-versio on asennettu ja sitä on testattu [Käyttöohjeen](Kayttoohje.md) kuvaamalla tavalla Linux-ympäristössä kannettavalla tietokoneella ja virtuaalityöasemassa.

# Toiminnallisuudet

Sovelluksessa on pyritty välttämään kaikki tilanteet joissa virheellinen syöte voisi aiheuttaa ongelman. Tällä hetkellä ei ole tiedossa että näin voisi käydä. Ongelma syntyy kuitenkin silloin kun sovellus käynnistetään ennen tietokannan alustamista.


