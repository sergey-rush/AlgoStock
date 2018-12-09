# using enum34
from enum import Enum


class CardType(Enum):
    Ace = 1, 'Ace'
    Two = 2, 'Two'
    Three = 3, 'Three'
    Four = 4, 'Four'
    Five = 5, 'Five'
    Six = 6, 'Six'
    Seven = 7, 'Seven'
    Eight = 8, 'Eight'
    Nine = 9, 'Nine'
    Ten = 10, 'Ten'
    Jack = 11, 'Jack'
    Queen = 12, 'Queen'
    King = 13, 'King'
    Joker = 14, 'Joker'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value
