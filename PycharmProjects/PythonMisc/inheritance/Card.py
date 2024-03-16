class Card:
    """ Represents a card """
    def __str__(self):
        return '% : %' % ( self.suit , self.rank )
    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.rank = rank


queen_of_diamonds = Card(1,12)
print(queen_of_diamonds)