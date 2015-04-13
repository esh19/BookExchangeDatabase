# BookExchangeDatabase
Pakki sem þarf: Django


Þrjár skrár til að vinna með: Prototype.py, Exchange.py, Seller.py.
Skrárnar eru fallasöfn til að vinna með gagnagrunnin.

Leiðbeiningar hvernig skal nota:
Þarf að gera: import Prototype, Exchange, Seller og svo er hægt að kalla á aðferðirnar með t.d. Prototype.getAll() eða Seller.createSeller(...).


Útskýringar:
Prototype.
Prototype er fyrirmynd af bók (frá stúdentasölu vefsíðunni).
Hægt er að leita eftir prótótýpum með t.d. Prototype.searchByKeyword(keyword) þar sem keyword er strengur. Fallakallið skilar niðurstöðum með lista af <Prototype objects>.
Eiginleikar prótótýpunnar má nálgast með t.d. Prototype.getTitle(prototype) þar sem prototype er <Prototype Object>

Seller.
Seller er seljandinn.
Hægt að búa til með Seller.createSeller(name, phoneNumber, email). Ef það er skráningarkerfi þá hefur hver Seller einstakt id.

Exchange.
Exchange táknar sölu.
Til að búa til sölu þarf að kalla á Exchange.create(prototype, seller, condition, price, date). Hér er prototype <Prototype object> og seller <Seller object>, condition er strengur, price heiltala. date ætti að virka með innbyggðu python 'import datetime' pakka.
Hægt að leita eftir nafn bókar sem er til sölu með Exchange.searchByTitle(title) sem skilar lista af <Exchange Object>. Leitin sættir sig við ef title er aðeins 'substring' af rétta title.
Til að gera almennari leit (leitar eftir nafni, bókarhöfund, vísindasvið o.fl) er hægt að nota Exchange.searchByKeyword(keyword).
Hægt að nálgast 'attributes' á <Exchange object> með t.d. Exchange.getPrice(exchange).
