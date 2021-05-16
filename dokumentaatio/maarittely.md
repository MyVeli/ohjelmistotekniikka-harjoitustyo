# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on investointien kannattavuuslaskenta sovellus. Sen avulla voi pitää kirjaa kuluista, sekä piirtää niiden ja kannattavuuden kehityksestä graafin.

## Käyttäjät
Sovelluksessa on vain yksi käyttäjärooli. Käyttäjät ja käyttäjien tiedot on suojattu salasanalla.

## Perusversion toiminnallisuudet
### Kirjautuminen ja rekisteröinti
* Ennen kirjautumista käyttäjä pystyy luomaan uuden käyttäjätunnuksen tai kirjautumaan sisään vanhalla, mutta ei näe muuta.
* Käyttäjätunnukset ovat uniikkejamerkkijonoja.
* Salasanat ovat vähintään 5 merkkiä pitkiä merkkijonoja, jotka on tallennettu tietokantaan hashina.
* Uuden tunnuksen luomisen yhteydessä järjestelmä ilmoittaa mikäli tunnus on jo varattu
* Kirjautumisen yhteydessä järjestelmä ilmoittaa mikäli tunnus puuttuu

### Kirjautumisen jälkeen
* Käyttäjä näkee listan tehdyistä suunnitelmista
* Käyttäjä voi luoda uuden suunnitelman
* Käyttäjä voi ladata suunnitelman

### Suunnitelman luominen
* Käyttäjä valitsee suunnitelmalle uniikin nimen ja luo suunnitelman
* Suunnitelman luomisen jälkeen käyttäjä siirtyy tyhjään suunnitelmaan

### Suunnitelman muokkaaminen
* Käyttäjä voi lisätä suunnitelman kuluja ja tuloja
* Kuluja ja liikevaihtoa voi olla erilaisista nimetyistä lähteistä ja järjestelmä tallentaa ne erikseen
* Järjestelmä piirtää liikevaihdon, kulujen ja kannattavuuden kehittymisestä graafin
* Suunnitelmasivulta voi poistua ja suunnitelma, sekä kaikki siihen liittyvä tieto tallentuvat tietokantaan

## Jatkokehitysideoita
* Laajemmat mahdollisuudet muokata tai poistaa kuluja, tuloja ja suunnitelmia
* Monipuolisten kannattavuuslukujen laskenta
* Käyttäjätunnuksien jakaminen kahteen luokkaan, joista toisella on vain oikeus tutkia suunnitelmia
* Skenaarioiden luominen suunnitelmille ja niiden vertailu ja piirtäminen graafeihin samassa näkymässä
* Kuva ja taulukko export suunnitelmista
* Kuluerien ja liikevaihdon laskenta käyttäjän antamien kaavojen pohjalta
* Useamman investoinnin yhdistäminen yhteen
* Erilaisten tulo- ja kustannuslähteiden vertailu keskenään graafien avulla
