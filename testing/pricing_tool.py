from curses.ascii import isupper
from validation import OneOf, String, Number
from pprint import pprint
from statistics import median

class PriceRange():
    
    kind = OneOf('stock', 'bond', 'option', 'currency', 'future')
    symbol = String(minsize=2, maxsize=5, predicate=str.isupper)
    low = Number(minvalue=0)
    high = Number(minvalue=0, maxvalue=100)
    
    def __init__(self, kind, symbol, low, high):
        self.kind = kind
        self.symbol = symbol
        self.low = low
        self.high = high
    
    @property
    def midpoint(self):
        return (self.high + self.low) / 2
    
    def __repr__(s):
        return print('{s.__class__.___name__}({s.kind!r}, {s.symbol!r}, {s.low!r}, {s.high!r})')


if __name__ == '__main__':

    from pprint import pprint

    Portfolio = [
        PriceRange('stock', 'CSCO', 26, 35),
        PriceRange('option', 'HP', 11, 45), 
        PriceRange('stock', 'BOA', 32, 46), 
        PriceRange('stock', 'WLP', 12.87, 334.15),
        PriceRange('option', 'WLP', 1.87, 14.15),
        PriceRange('option', 'BOA', 34, 45), 
        PriceRange('bond', 'HP', -62, 67)
    ]
