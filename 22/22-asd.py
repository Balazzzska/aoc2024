import os
import time


class Sequence:
    def __init__(self, num):
        self._num = num
        self._old_num = None
        self._price = self._compute_price()
        self._old_price = None
        self._prices = {}
        self._diffs = []

    def _mix(self, val):
        self._num = self._num ^ val

    def _prune(self):
        self._num = self._num % 16777216

    def _compute_price(self):
        return self._num % 10

    def _update_diffs(self):
        self._diffs.append(self._price - self._old_price)

        if len(self._diffs) > 4:
            self._diffs.pop(0)

        if len(self._diffs) == 4 and tuple(self._diffs) not in self._prices:
            self._prices[tuple(self._diffs)] = self._price

    def step(self):
        self._old_num = self._num
        self._old_price = self._price

        self._mix(self._num * 64)
        self._prune()

        self._mix(self._num // 32)
        self._prune()

        self._mix(self._num * 2048)
        self._prune()

        self._price = self._compute_price()

        self._update_diffs()

    def get_num(self):
        return self._num

    def get_price(self):
        return self._price

    def get_prices(self):
        return self._prices


def parse_input():
    with open(
        r"C:\Users\maage\OneDrive\Asztali gép\__Python\aoc2024\22\22-input.txt", "r"
    ) as file:
        txt = file.read().strip()

    return list(map(int, txt.split("\n")))


def solve_level_1():
    """
    Solve level 1
    """

    # Read input file
    nums = parse_input()

    tot = 0

    for num in nums:
        seq = Sequence(num)
        for _ in range(2000):
            seq.step()
        tot += seq.get_num()

    return tot


def solve_level_2():
    """
    Solve level 2
    """

    # Read input file
    nums = parse_input()

    all_prices = {}

    for num in nums:
        seq = Sequence(num)
        for _ in range(2000):
            seq.step()
        for s, p in seq.get_prices().items():
            if s not in all_prices:
                all_prices[s] = 0
            all_prices[s] += p

    return max(all_prices.values())


if __name__ == "__main__":
    debug = True

    start = time.time()
    print(solve_level_2())  # 1499
    stop = time.time()
