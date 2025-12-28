from time import sleep

BLACK = "█"
WHITE = "░"
# Rule 86: 1010110 :: 01101010
MAIN_RULESET = [0,1,1,0,1,0,1,0]




def print_row(row: list[int]):
    print("".join([BLACK if x else WHITE for x in row]))

def generate(cells, generations, gen_speed_seconds=0.2):
    for _ in range(1, generations):
        sleep(gen_speed_seconds)
        print_row(cells)
        cells = next_generation(cells)


def apply_rules(left, current, right, ruleset=MAIN_RULESET):
    return ruleset[(left * 4) + (current * 2) + (right * 1)]


def next_generation(cells: list[int]) -> list[int]:
    next_gen = []

    size = len(cells)

    for i in range(size):
        left = cells[i - 1] if i > 0 else 0
        current = cells[i]
        right = cells[i + 1] if i + 1 < size else 0
        next_gen.append(apply_rules(left, current, right))

    return next_gen

def generateWithOneInTheMiddle(cells_size: int, generations: int):
    cells = [0 for _ in range(cells_size)]
    cells[len(cells) // 2] = 1
    generate(cells, generations)


if __name__ == '__main__':
    generateWithOneInTheMiddle(100, 50)


