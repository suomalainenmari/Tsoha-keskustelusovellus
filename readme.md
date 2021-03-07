# Keskustelusovellus

Tässä repositoriossa tehdään Helsingin yliopiston Tietokantasovellus kurssille  harjoitustyö. Harjoitustyön aiheeksi on valittu keskustelusovellus. 


### Sovelluksen testaaminen herokussa
Sovellus löytyy herokusta täältä: https://tsoha-keskustelusovellus-ms.herokuapp.com/

#### Lisätietoja testaukseen
* Tietokannasta löytyy käyttäjä admin, salasana:admin, joka on ns. superuser käyttäjä, joka pystyy poistamaan moderointioikeuksia muilta moderaattoreilta. Muut moderaattorit eivät voi poistaa moderointioikeutta. Admin ei pysty poistamaan moderointioikeutta itseltään. Käyttäjällä admin voi siis käydä testikäyttäjälle myös antamassa moderointioikeudet, mikäli moderointioikeuksia haluaa testata. 
* Näkymiä on sovelluksessa neljänlaisia: vierailija-käyttäjä, peruskäyttäjä, ylläpitokäyttäjä (moderaattori), sekä admin.

### Sovelluksen toiminnallisuudet
* Keskustelut on jaettu alueisiin, joilla on viestejä sisältäviä viestiketjuja(threads)
* Käyttäjä voi luoda tunnuksen, luoda uusia ketjuja ja lähettää viestejä olemassaoleviin ketjuihin
* Käyttäjän tunnukset tarkistetaan.
* Kirjautuneet käyttäjät voivat olla peruskäyttäjiä tai moderaattoreita
    * Ainoastaan moderaattorit voivat lisätä uusia keskustelualueita(aiheita)
    * Moderaattorit voivat antaa moderointioikeudet toiselle käyttäjälle
    * Ainoastaan superuser admin (admin,admin) voi poistaa moderointioikeudet
    * Superuser admin ei pysty poistamaan itseltään moderointioikeutta
* Samannimistä keskusteluaihetta ei voi luoda.
* Keskusteluaiheille ja viestin pituuksille määritelty maksimipituus, jotka tarkistetaan.
* Viestiketjun voi poistaa sen luonut henkilö, sekä moderaattorit
* Viestin voi poistaa sen luonut henkilö, sekä moderaattorit
* Viestiketjun aloitusviestiä voi muokata ainoastaan sen luonut henkilö
* Viestiä voi muokata ainoastaan sen luonut henkilö
* Viisi tuoreinta (viimeiseksi luotua) viestiketjua on listattu etusivulla, keskusteluaiheen viestiketjuihin pääsee sivupalkista
* Käyttäjät eivät pääse alueille mihin heidän ei kuulu. Esim kirjautumattomat käyttäjät eivät voi luoda ketjuja tai lähettää viestejä. Moderaattorisivun sisältö näkyy vaan moderaattoreille.
* Hakutoiminnallisuudella voi hakea viestiketjua tai viestiketjussa olevaa viestiä.

