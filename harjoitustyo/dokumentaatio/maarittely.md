# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on investointien kannattavuuslaskenta sovellus. Sen avulla voi laskea takaisinmaksuaikoja ja investoinnin kannattavuutta erilaisille projekteille.

## Käyttäjät
Sovelluksessa on vain yksi käyttäjärooli. Myöhemmin sovellukseen saatetaan lisätä erikseen roolit investointisuunnitelmien tekijälle ja katsojalle, joka voi vain tutkai luotuja suunnitelmia.

## Perusversion toiminnallisuudet
### Kirjautuminen ja rekisteröinti
* Ennen kirjautumista käyttäjä pystyy luomaan uuden käyttäjätunnuksen tai kirjautumaan sisään vanhalla, mutta ei näe muuta.
* Käyttäjätunnukset ovat uniikkeja vähintään 5 merkkiä pitkiä merkkijonoja.
* Uuden tunnuksen luomisen yhteydessä järjestelmä ilmoittaa mikäli tunnus on jo varattu
* Kirjautumisen yhteydessä järjestelmä ilmoittaa mikäli tunnus puuttuu

### Kirjautumisen jälkeen
* Käyttäjä näkee listan tehdyistä suunnitelmista
* Käyttäjä voi luoda uuden suunnitelman
* Käyttäjä voi poistaa suunnitelman
* Käyttäjä voi ladata suunnitelman

### Suunnitelman luominen
* Käyttäjä valitsee suunnitelmalle uniikin nimen ja luo suunnitelman
* Suunnitelman luomisen jälkeen käyttäjä siirtyy tyhjään suunnitelmaan

### Suunnitelman muokkaaminen
* Käyttäjä voi lisätä, poistaa tai muokata suunnitelman kuluja ja tuloja
* Kuluja ja liikevaihtoa voi olla erilaisista nimetyistä lähteistä ja järjestelmä tallentaa ne erikseen
* Järjestelmä piirtää liikevaihdon, kulujen ja kannattavuuden kehittymisestä graafin ja näyttää arvot myös numeerisina
* Suunnitelman voi tallentaa ja siirtyä takaisin valikkoon, jossa on lista suunnitelmista

## Jatkokehitysideoita
* Salasanan lisääminen käyttäjätunnuksiin
* Käyttäjätunnuksien jakaminen kahteen luokkaan, joista toisella on vain oikeus tutkia suunnitelmia
* Skenaarioiden luominen suunnitelmille ja niiden vertailu ja piirtäminen graafeihin samassa näkymässä
* Kuva ja taulukko export suunnitelmista
* Kuluerien ja liikevaihdon laskenta käyttäjän antamien kaavojen pohjalta
* Useamman investoinnin yhdistäminen yhteen
* Erilaisten tulo- ja kustannuslähteiden vertailu keskenään graafien avulla