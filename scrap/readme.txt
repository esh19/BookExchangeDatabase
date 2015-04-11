Kóði samanstendur af eftirfarandi skrám

__init__.py
connector.py
scraper.py
X2A.py

Eftirfarandi pakkar þurfa að vera til staðar í python - nota t.d. pip install
til að setja þá upp.

requests
beautifulsoup4
html5lib


Sýnidæmi að neðan miðast við að skrárnar séu í undirmöpunni X2A

--------------

# -*- coding: utf-8 -*-

import json          # bara fyrir þetta sýndæmi
from X2A import X2A  # importa aðal interface


# potstBooks er eithvað fall sem tekur við gögnum frá scraper, má heita hvað
# sem er en verður að taka eitt viðhengi sem er listi af dict hutum
#
# @lst listi af dict hlutum
#
# ATH hér skrifum við bara gögn frá scraper út í skrá, gagnagunnsteymi myndi
# væntanlega ítra sig yfir listann og setja hverja bók inn í gagnagrunninn
#
def postBooks(lst):
    with open('dump.json', 'wb') as F:
        json.dump(lst, F)
    return True


# dæmi um notkun á scraper
def testScraper():
    # initalize-a scraper með pointer á callback fall, scraper skilar gögnum
    # til þessa viðmóts þegar skröpun er lokið
    scraper = X2A.X2A(postBooks)

    # virkja skröpun, hægt að senda int yfir sem parameter, þá stoppar scraper
    # eftir n fjölda bóka, ef n er sleppt skrapar hann alla bókalista fyrir
    # Háskóla íslands á boksala.is fyrir yfirstandandi önn...
    scraper.scrape(50)


if __name__ == '__main__':
    testScraper()
