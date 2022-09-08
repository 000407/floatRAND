import itertools
from decimal import getcontext, Decimal


class FloatRAND:
    # TODO: Add harvesting seeds from execution environment
    def __init__(self, seeds: tuple[float, float], prec: int = 23) -> None:
        self.num = Decimal(seeds[0])
        self.den = Decimal(seeds[1])
        self.prec = prec

    def reseed(self, seeds: tuple[float, float]) -> None:
        self.num = Decimal(seeds[0])
        self.den = Decimal(seeds[1])

    def get_mantissa_bit(self, num) -> tuple[int, Decimal]:
        getcontext().prec = self.prec
        m = ((num % 1) * 2)
        return int(m // 1), m % 1

    def get_n_bits(self, n: int) -> int:
        rem = (self.num / self.den) % 1
        res = 0
        for i in itertools.repeat(None, n):
            b, rem = self.get_mantissa_bit(rem)
            res = (res << 1) | b

        return res


if __name__ == '__main__':
    f = FloatRAND((314159, 236461))
    print(f.get_n_bits(100))
    print(f.get_n_bits(200))
    print(f.get_n_bits(400))
    print(f.get_n_bits(500))
