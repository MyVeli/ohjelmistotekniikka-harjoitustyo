# Velin ohjelmistotekniikan repository

Projektissa tehtävä sovellus toimii erilaisten investointien kannattavuuslaskentaa ja laskelmien visualisointia varten. Tällä hetkellä sovelluksesta on tehty lähinnä rekisteröinti ja sisäänkirjautuminen, sekä tietokannan luominen.

## Dokumentaatio
* [määrittely dokumentti](https://github.com/MyVeli/ohjelmistotekniikka-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/maarittely.md)
* [työaikakirjanpito](https://github.com/MyVeli/ohjelmistotekniikka-harjoitustyo/blob/main/harjoitustyo/tyoaikakirjanpito/tyoaika.md)

## Asennus
1. Riippuvuudet asennetaan komennolla "poetry install"
2. Tämän jälkeen sovelluksen voi käynnistää komennolla "poetry invoke start"

## Komentorivitoiminnot
* Ohjelman voi käynnistää komennolla "poetry run invoke start"
* Testit voi suorittaa komennolla "poetry run invoke test"
* Testikattavuusraportin saa komennolla "poetry run invoke coverage-report" ja raportti muodostuu kansioon htmlcov.

