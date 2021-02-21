# Keskustelusovellus

Tässä repositoriossa tehdään Helsingin yliopiston Tietokantasovellus kurssille  harjoitustyö. Harjoitustyön aiheeksi on valittu keskustelusovellus. 


### Sovelluksen testaaminen herokussa
Sovellus löytyy herokusta täältä: https://tsoha-keskustelusovellus-ms.herokuapp.com/

#### Lisätietoja testaukseen
* Tietokannasta löytyy käyttäjä admin, salasana:admin, joka on ns. superuser käyttäjä, joka pystyy poistamaan moderointioikeuksia muilta moderaattoreilta. Muut moderaattorit eivät poistaa moderointioikeutta. Admin ei pysty poistamaan moderointioikeutta itseltään. Käyttäjällä admin voi siis käydä testikäyttäjälle myös antamassa moderointioikeudet, mikäli moderointioikeuksia haluaa testata. 
* Näkymiä on sovelluksessa neljänlaisia: vierailija-käyttäjä, peruskäyttäjä, ylläpitokäyttäjä (moderaattori), sekä admin.

### Sovelluksen tämänhetkinen tilanne
* Keskustelut on jaettu alueisiin, joilla on viestejä sisältäviä viestiketjuja(threads)
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan ja tunnukset tarkistetaan.
* Käyttäjät voivat olla peruskäyttäjiä tai moderaattoreita
    * Ainoastaan moderaattorit voivat lisätä uusia keskustelualueita
    * Moderaattorit voivat antaa moderointioikeudet toiselle käyttäjälle
    * Ainoastaan "superuser" (admin,admin) voi poistaa moderointioikeudet
    * Superuser admin ei pysty poistamaan itseltään käyttöoikeutta
* Samannimistä keskusteluaihetta ei voi luoda.
* Keskusteluaiheille ja viestin pituuksille määritelty maksimipituus.
* Viestiä voi muokata tai viestin voi poistaa käyttäjä joka viestin on luonut.
* Kaikki viestiketjut listattu etusivulla, keskusteluaiheen viestiketjuihin pääsee sivupalkista
* Käyttäjä voi luoda tunnuksen, luoda uusia ketjuja ja lähettää viestejä olemassaoleviin ketjuihin
* Käyttäjät eivät pääse alueille mihin heidän ei kuulu. Esim kirjautumattomat käyttäjät eivät voi luoda ketjuja tai lähettää viestejä. Moderaattorisivun sisältö näkyy vaan moderaattoreille.


### Sovelluksen haluttuja toiminnallisuuksia

* Viestit myös moderaattorien poistettavaksi. Ei kuitenkaan muokkausoikeutta.
* Viestejä voi etsiä hakutoiminnolla
    * Esim lähettäjän, lähetysajan tai sisällön mukaan
* Sovellukseen voi luoda myös salaisia alueita, jolle on pääsy vain tietyillä käyttäjillä

### Muita muutoksia
* Etusivun asettelua missä nyt viimeisimmät viestiketjut niin vielä pohdinnassa. Ehkä niin, että näytetään vaan 10 viimeksi luotua tai viimeksi aktiivisia.

