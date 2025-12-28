import argparse
from time import sleep

BLACK = "█"
WHITE = "░"


# Rule 86: 1010110 :: 01101010
MAIN_RULESET = [0,1,1,0,1,0,1,0]

def getRuleSet(x: int) -> list[int]:
    binX = str(bin(x))[::-1][:-2]
    if len(binX) < 8:
        binX += "0"
    return [int(y) for y in binX]

def print_row(row: list[int]):
    print("".join([BLACK if x else WHITE for x in row]))

def generate(cells, generations, ruleset, gen_speed_seconds=0.2):
    for _ in range(1, generations):
        sleep(gen_speed_seconds)
        print_row(cells)
        cells = next_generation(cells, ruleset=ruleset)

def apply_rules(left, current, right, ruleset):
    return ruleset[(left * 4) + (current * 2) + (right * 1)]

def next_generation(cells: list[int], ruleset) -> list[int]:
    next_gen = []

    size = len(cells)

    for i in range(size):
        left = cells[i - 1] if i > 0 else 0
        current = cells[i]
        right = cells[i + 1] if i + 1 < size else 0
        next_gen.append(apply_rules(left, current, right, ruleset=ruleset))

    return next_gen

def generateWithOneInTheMiddle(cells_size: int, generations: int, ruleset, speed):
    cells = [0 for _ in range(cells_size)]
    cells[len(cells) // 2] = 1
    generate(cells, generations, ruleset=ruleset, gen_speed_seconds=speed)

parser = argparse.ArgumentParser()
parser.add_argument("ruleSet", default=86, type=int)
parser.add_argument("--generations", default=50, type=int)
ruleSetNumber = parser.parse_args().ruleSet
generations = parser.parse_args().generations if parser.parse_args().generations else 50

if __name__ == '__main__':
    if not (0 <= ruleSetNumber <= 256):
        print("ERROR: The ruleSetNumber selected breaks the 2^8 principle! Stopping program.\n\n")
        exit()
    ruleset = getRuleSet(ruleSetNumber)
    generateWithOneInTheMiddle(200, generations, ruleset, 0.01)

