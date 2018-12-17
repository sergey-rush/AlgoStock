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

    def replace_nth_occurance(input, old_value, new_value, count):
        """ Replace nth occurance of a string with another string
        """
        #input.replace(old_value, new_value, count)
        for i in range(count):
            if i == 2:
                input.replace(old_value, new_value, i)
        return input

    def nth_repl_all(s, sub, repl, nth):
        find = s.find(sub)
        # loop util we find no match
        i = 1
        while find != -1:
            # if i  is equal to nth we found nth matches so replace
            if i == nth:
                s = s[:find]+repl+s[find + len(sub):]
                i = 0
            # find + len(sub) + 1 means we start after the last match
            find = s.find(sub, find + len(sub) + 1)
            i += 1
        return s

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
