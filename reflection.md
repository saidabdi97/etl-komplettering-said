# Reflektion

I detta projekt har jag byggt ett enkelt ETL-flöde i Python där jag har arbetat med att läsa in, bearbeta och vidareförmedla data. Målet var att skapa ett tydligt dataflöde från rådata till färdig statistik, och även visa hur datan kan exponeras och skickas vidare i ett system.

Jag började med att sätta upp ett GitHub-repo och en tydlig projektstruktur. Därefter skapade jag en CSV-fil med produktdata som jag använde som ingång till ETL-flödet. Med hjälp av pandas läste jag in datan, städade den genom att ta bort dubletter och hantera felaktiga värden, och tog sedan fram statistik som till exempel medelpris, antal produkter per kategori och de dyraste produkterna.

När ETL-delen fungerade lade jag till en FastAPI-endpoint som gör det möjligt att hämta statistiken via en webbadress. Detta gjorde att projektet kändes mer som en riktig applikation istället för bara ett script. Efter det implementerade jag en Kafka-producent som skickar vidare resultatet till ett topic, vilket visar hur datan kan ingå i ett större dataflöde.

Under arbetet försökte jag arbeta stegvis och testa varje del innan jag gick vidare, vilket fungerade bra. Däremot kunde jag ha arbetat mer agilt genom att planera arbetet tydligare i början, till exempel genom att dela upp det i mindre delar (user stories) och använda branches istället för att arbeta direkt i main. Det hade gjort utvecklingen mer strukturerad och lättare att följa.

En utmaning i projektet var att få igång Kafka och Docker, eftersom det krävde lite mer konfiguration än de andra delarna. När det väl fungerade blev det dock tydligt hur data kan skickas vidare mellan olika delar i ett system.

Sammanfattningsvis har projektet gett mig en bättre förståelse för hur ett ETL-flöde fungerar i praktiken och hur olika verktyg som pandas, FastAPI och Kafka kan användas tillsammans för att bygga en enkel dataplattform.