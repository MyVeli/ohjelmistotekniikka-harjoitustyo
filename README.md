# Velin ohjelmistotekniikan repository

Projektissa tehtävä sovellus toimii erilaisten investointien kannattavuuslaskentaa ja laskelmien visualisointia varten. Tällä hetkellä sovelluksesta on tehty lähinnä rekisteröinti ja sisäänkirjautuminen, sekä tietokannan luominen.

## Release:
[Viikko 6 release](https://github.com/MyVeli/ohjelmistotekniikka-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio
* [määrittely dokumentti](https://github.com/MyVeli/ohjelmistotekniikka-harjoitustyo/blob/main/dokumentaatio/maarittely.md)
* [työaikakirjanpito](https://github.com/MyVeli/ohjelmistotekniikka-harjoitustyo/blob/main/tyoaikakirjanpito/tyoaika.md)
* [arkkitehtuuri](https://github.com/MyVeli/ohjelmistotekniikka-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
* [käyttöohje](https://github.com/MyVeli/ohjelmistotekniikka-harjoitustyo/blob/main/dokumentaatio/kayttohje.md)

## Asennus
1. Riippuvuudet asennetaan komennolla "poetry install"
2. Tämän jälkeen sovelluksen voi käynnistää komennolla "poetry invoke start"

## Komentorivitoiminnot
* Ohjelman voi käynnistää komennolla "poetry run invoke start"
* Testit voi suorittaa komennolla "poetry run invoke test"
* Testikattavuusraportin saa komennolla "poetry run invoke coverage-report" ja raportti muodostuu kansioon htmlcov.

