class Stock:
    def __init__(self, id, issuer_id, ticker, per, trade_date, open, high, low, close, volume):
        self.id = id
        self.issuer_id = issuer_id
        self.ticker = ticker
        self.per = per
        self.trade_date = trade_date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __eq__(self, other):
        return self.ticker == other.ticker

    def __lt__(self, other):
        return self.ticker < other.ticker

# sort usage:
# card_sorted = sorted(self.hand_cards) - sorted object list
# rank_sorted = [c.rank for c in card_sorted] - sorted rank values


# id integer DEFAULT nextval('stocks_id_seq'::regclass),
# issuer_id integer,
# ticker text,
# per text,
# trade_date text,
# open text,
# high text,
# low text,
# close text,
# volume text
