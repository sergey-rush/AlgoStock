class Issuer:
    def __init__(self, id, ticker):
        self.id = id
        self.ticker = ticker

    def __eq__(self, other):
        return self.ticker == other.ticker

    def __lt__(self, other):
        return self.ticker < other.ticker

# sort usage:
# card_sorted = sorted(self.hand_cards) - sorted object list
# rank_sorted = [c.rank for c in card_sorted] - sorted rank values


