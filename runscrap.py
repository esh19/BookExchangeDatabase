import Prototype
import sys
sys.path.insert(0, './scrap')
import X2A


books = []

scraper = X2A.X2A(Prototype.createFromList)
scraper.scrape()

