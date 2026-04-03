# Reflektion

I detta projekt har jag byggt ett ETL-flöde i Python där jag har arbetat med att läsa in, bearbeta och vidareförmedla data. Målet var att skapa ett tydligt dataflöde från rådata till färdig statistik, samt visa hur datan kan exponeras och skickas vidare i ett system.

Jag började med att sätta upp ett GitHub-repo och en tydlig projektstruktur. Därefter skapade jag en CSV-fil med produktdata som användes som ingång till ETL-flödet. Med hjälp av pandas läste jag in datan, städade den genom att ta bort dubletter och hantera felaktiga värden, och tog sedan fram statistik som till exempel medelpris, antal produkter per kategori och de dyraste produkterna.

När ETL-delen fungerade implementerade jag en FastAPI-endpoint för att exponera statistiken via ett API. Detta gjorde att projektet gick från att vara ett enkelt script till att likna en mer verklig applikation. Därefter lade jag till en Kafka-producent som skickar vidare resultatet till ett topic, vilket visar hur datan kan ingå i ett större dataflöde.

För att arbeta mer strukturerat använde jag GitHub Issues för att dela upp arbetet i mindre delar, till exempel ETL-implementation, API och Kafka-integration. Dessa fungerade som enklare user stories och gjorde det tydligare vad som behövde göras. Arbetet kan också delas in i tre steg (sprintar): först ETL med pandas, sedan API med FastAPI och till sist Kafka.

Under arbetet försökte jag arbeta stegvis och testa varje del innan jag gick vidare, vilket fungerade bra. En förbättring hade varit att arbeta ännu mer agilt genom att använda branches och pull requests istället för att arbeta direkt i main, samt använda GitHub Projects för att planera och följa upp arbetet mer visuellt.

En utmaning i projektet var att få igång Kafka och Docker, eftersom det krävde mer konfiguration än de andra delarna. När det väl fungerade blev det tydligt hur data kan skickas vidare mellan olika system.

Sammanfattningsvis har projektet gett mig en bättre förståelse för hur ett ETL-flöde fungerar i praktiken och hur olika verktyg som pandas, FastAPI och Kafka kan kombineras för att bygga en enkel dataplattform.