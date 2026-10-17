from enum import IntEnum, auto


class OpCodes(IntEnum):
    PUSH = auto()
    ADD = auto()
    PRINT = auto()
    HALT = auto()       