import X2A


books = []


def postBooks(lst):
    global books
    books = lst
    return True


# dæmi um notkun á scraper
def testScraper():
    # initalize-a scraper með pointer á callback fall, scraper skilar gögnum
    # til þessa viðmóts þegar skröpun er lokið
    scraper = X2A.X2A(postBooks)

    # virkja skröpun, hægt að senda int yfir sem parameter, þá stoppar scraper
    # eftir n fjölda bóka, ef n er sleppt skrapar hann alla bókalista fyrir
    # Háskóla íslands á boksala.is fyrir yfirstandandi önn...
    scraper.scrape(10)


testScraper()