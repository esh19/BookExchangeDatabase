K��i samanstendur af eftirfarandi skr�m

__init__.py
connector.py
scraper.py
X2A.py

Eftirfarandi pakkar �urfa a� vera til sta�ar � python - nota t.d. pip install
til a� setja �� upp.

requests
beautifulsoup4
html5lib


S�nid�mi a� ne�an mi�ast vi� a� skr�rnar s�u � undirm�punni X2A

--------------

# -*- coding: utf-8 -*-

import json          # bara fyrir �etta s�nd�mi
from X2A import X2A  # importa a�al interface


# potstBooks er eithva� fall sem tekur vi� g�gnum fr� scraper, m� heita hva�
# sem er en ver�ur a� taka eitt vi�hengi sem er listi af dict hutum
#
# @lst listi af dict hlutum
#
# ATH h�r skrifum vi� bara g�gn fr� scraper �t � skr�, gagnagunnsteymi myndi
# v�ntanlega �tra sig yfir listann og setja hverja b�k inn � gagnagrunninn
#
def postBooks(lst):
    with open('dump.json', 'wb') as F:
        json.dump(lst, F)
    return True


# d�mi um notkun � scraper
def testScraper():
    # initalize-a scraper me� pointer � callback fall, scraper skilar g�gnum
    # til �essa vi�m�ts �egar skr�pun er loki�
    scraper = X2A.X2A(postBooks)

    # virkja skr�pun, h�gt a� senda int yfir sem parameter, �� stoppar scraper
    # eftir n fj�lda b�ka, ef n er sleppt skrapar hann alla b�kalista fyrir
    # H�sk�la �slands � boksala.is fyrir yfirstandandi �nn...
    scraper.scrape(50)


if __name__ == '__main__':
    testScraper()
