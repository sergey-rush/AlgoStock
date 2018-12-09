# using enum34
from enum import Enum


class SuitType(Enum):
    Null = 0, 'Null'
    Heart = 1, 'Heart'
    Diamond = 2, 'Diamond'
    Club = 3, 'Club'
    Spade = 4, 'Spade'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

# usage:
# print(SuitType.Diamond)
# SuitType.Diamond
# print(int(SuitType.Diamond))
# 2
# print(SuitType.Diamond.fullname)
# Diamond
