Tässä repositoriossa tehdään Helsingin yliopiston Tietokantasovellus kurssille  harjoitustyö. Harjoitustyön aiheeksi on valittu keskustelusovellus. 

Sovelluksen testaaminen herokussa: 
https://tsoha-keskustelusovellus-ms.herokuapp.com/

Sovelluksen tämänhetkinen tilanne:
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan ja tunnukset tarkistetaan.
* Käyttäjät voivat olla peruskäyttäjiä tai moderaattoreita
    * Ainoastaan moderaattorit voivat lisätä uusia keskustelualueita
    * Moderaattorit voivat antaa moderointioikeudet toiselle käyttäjälle
    * Ainoastaan "superuser" (admin,admin) voi poistaa moderointioikeudet
    * Superuser admin ei pysty poistamaan itseltään käyttöoikeutta
* Samannimistä keskusteluaihetta ei voi luoda.
* Keskusteluaiheille ja viestin pituuksille määritelty maksimipituus.
* Viestejä ei voi vielä poistaa.
* Kaikki viestit listattu etusivulla, keskusteluaiheen viesteihin pääsee ylhäällä olevasta linkistä


Sovelluksen haluttuja toiminnallisuuksia:
* Keskustelut on jaettu alueisiin, joilla on viestejä sisältäviä viestiketjuja(threads)
* Käyttäjä voi olla peruskäyttäjä tai ylläpitäjä
    * Ylläpitäjä voi antaa peruskäyttäjälle ylläpito-oikeuden
* Käyttäjä voi luoda tunnuksen, luoda uusia ketjuja ja lähettää viestejä olemassaoleviin ketjuihin 
* Käyttäjä pystyy muokkaamaan viestiä ja poistamaan sen myöhemmin
* Viestejä voi etsiä hakutoiminnolla
    * Esim lähettäjän, lähetysajan tai sisällön mukaan
* Sovellukseen voi luoda myös salaisia alueita, jolle on pääsy vain tietyillä käyttäjillä

