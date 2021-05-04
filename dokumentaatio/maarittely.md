# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on investointien kannattavuuslaskenta sovellus. Sen avulla voi laskea takaisinmaksuaikoja ja investoinnin kannattavuutta erilaisille projekteille.

## Käyttäjät
Sovelluksessa on vain yksi käyttäjärooli. Myöhemmin sovellukseen saatetaan lisätä erikseen roolit investointisuunnitelmien tekijälle ja katsojalle, joka voi vain tutkai luotuja suunnitelmia.

## Perusversion toiminnallisuudet
### Kirjautuminen ja rekisteröinti
* Ennen kirjautumista käyttäjä pystyy luomaan uuden käyttäjätunnuksen tai kirjautumaan sisään vanhalla, mutta ei näe muuta.
* Käyttäjätunnukset ovat uniikkejamerkkijonoja.
* Salasanat ovat vähintään 5 merkkiä pitkiä merkkijonoja, jotka on tallennettu tietokantaan hashina.
* Uuden tunnuksen luomisen yhteydessä järjestelmä ilmoittaa mikäli tunnus on jo varattu
* Kirjautumisen yhteydessä järjestelmä ilmoittaa mikäli tunnus puuttuu

### Kirjautumisen jälkeen
* tehty v5: Käyttäjä näkee listan tehdyistä suunnitelmista
* tehty v5: Käyttäjä voi luoda uuden suunnitelman
* Käyttäjä voi poistaa suunnitelman
* tehty v5: Käyttäjä voi ladata suunnitelman

### Suunnitelman luominen
* tehty v5: Käyttäjä valitsee suunnitelmalle uniikin nimen ja luo suunnitelman
* tehty v5: Suunnitelman luomisen jälkeen käyttäjä siirtyy tyhjään suunnitelmaan

### Suunnitelman muokkaaminen
* osittain tehty v6: Käyttäjä voi lisätä, poistaa tai muokata suunnitelman kuluja ja tuloja
* osittain tehty v6: Kuluja ja liikevaihtoa voi olla erilaisista nimetyistä lähteistä ja järjestelmä tallentaa ne erikseen
* osittain tehty v6: Järjestelmä piirtää liikevaihdon, kulujen ja kannattavuuden kehittymisestä graafin ja näyttää arvot myös numeerisina
* osittain tehty v6: Suunnitelman voi tallentaa ja siirtyä takaisin valikkoon, jossa on lista suunnitelmista

## Jatkokehitysideoita
* Käyttäjätunnuksien jakaminen kahteen luokkaan, joista toisella on vain oikeus tutkia suunnitelmia
* Skenaarioiden luominen suunnitelmille ja niiden vertailu ja piirtäminen graafeihin samassa näkymässä
* Kuva ja taulukko export suunnitelmista
* Kuluerien ja liikevaihdon laskenta käyttäjän antamien kaavojen pohjalta
* Useamman investoinnin yhdistäminen yhteen
* Erilaisten tulo- ja kustannuslähteiden vertailu keskenään graafien avulla