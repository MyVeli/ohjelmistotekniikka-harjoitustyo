# Arkkitehtuurikuvaus

## Rakenne
![Rakenne](./kuvat/pakkausrakenne.png)

## Käyttöliittymä
Näkymiä on tällä hetkellä kaksi, joista toinen on kirjautumista ja rekisteröintiä varten ja toinen on pohja pääsivulle, jossa suunnitelmat näkyvät listana, niitä voi luoda lisää ja valita muokattavaksi. Käyttöliittymiä tulee vielä ainakin yksi, joka on suunnitelmien editoimista varten.
<br>
Näkymien näyttämisestä vastaa ui luokka.


## Tietokanta
Järjestelmä käyttää sqlite-tietokantaa. Tällä hetkellä tietokannassa on yksi taulu, jossa on tallennettuna käyttäjät ja salasanojen hashit. Tauluja tulee vielä lisää suunnitelmia ja niissä käytettävää dataa varten.
