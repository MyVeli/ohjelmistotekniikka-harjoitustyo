# Testausdokumentti
Ohjelma on testattu manuaalisin testein käyttämällä sovellusta, sekä automaattisilla yksikkö- ja integraatiotesteillä. Sovellus on jaettu kolmeen osaan, datapalveluun, sovelluslogiikkaan ja käyttöliittymään. Näistä käyttäliittymä on testattu vain manuaalisesti. Sovelluslogiikka ja datapalvelu on testattu sekä manuaalisesti, että automaattisesti.

## Yksikkö- ja integraatiotestit

### Sovelluslogiikka
Ohelman sovelluslogiikka, eli logic-kansion sisältö on testattu neljällä testitiedostolla, jotka ovat TestYearlyCosts, TestYearlyRevenue, TestInvestmentPlan ja TestSessionInfo. TestInvestmentPlan ja TestSessionInfo vaativat tietokannan, joka luodaan niille in-memory tyyppisenä tietokantana käyttämällä db_mgmt.py palvelun tietokannan luontia ja antamalla parametriksi ":memory:". TestInvestmentPlan ja TestSessionInfo käyttävät molemmat useita luokkia, joten varsinkin TestInvestmentPlan testien osalta suuri osa sovelluksen osista tulee samalla integraatiotestattua.

### Datapalvelu
Ohjelman data_service osuus on testattu kolmella testitiedostolla, jotka ovat TestLogin, TestRegister ja TestPlanService. Kaikki näistä luokista käyttävät tietokantaa, joka luodaan niille in-memory tyyppisenä tietokantana kuten sovelluslogiikalle. Lisäksi db_mgmt.py sisältö on lyhyesti testattu TestCreateDB testiluokassa.

### Testikattavuus
[Test_coverage](./kuvat/coverage.PNG)
Muutamia poikkeuksia jäi testaamatta. Lisäksi plan_mgmt jäi testaamatta, mutta sen toiminnallisuus tulee käytännössä testattua hyvin TestPlanService testien kautta.

## Järjestelmätestaus
Järjestelmätestaus suoritettiin manuaalisesti. Sovellus on asennettu sekä Windows 10, että Linux ympäristöihin [ohjelman käyttöohjeen](./kayttohje.md) kuvaamalla tavalla. Sovellus on testattu python 3.9.2 ja 3.6.8 ympäristöissä. Sovellus on testattu sekä sellaisessa tilanteessa, jossa tietokanta on olemassa, että sellaisessa, jossa se luo käynnistettäessä uuden.

Testatessa kaikki käyttöohjeen mukaiset toiminnallisuudet on testattu läpi toimivilla, tyhjillä ja virheellisillä arvoilla.

## Sovelluksessa olevat laatuongelmat
* Käyttäjä ei tällä hetkellä saa näkyvää virheilmoitusta mikäli yrittää lisätä kulun tai tulon ilman vaadittavia arvoja tai kummallisilla arvoilla. Virhe kyllä käsitellään silti, eikä se kaada ohjelmaa.
* Matplotlib ei toimi hyvin yhteen poetryn ja vanhan pythonin kanssa, joten se pitää asentaa erikseen pip komennolla.
