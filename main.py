
def generate_urinals(n: int):
    return [0 for _ in range(n)]

def get_score(current: int, target: int):
    return 0.5 ** (abs(target - current) - 1)

def pick_urinal(urinals: list[int]):
    if all(urinals):
        return -1

    if not any(urinals):
        return 0

    least_score = None
    best_urinal = None

    for i, occupied in enumerate(urinals):
        if occupied:
            continue

        score = 0

        for j, other_occupied in enumerate(urinals):
            if j != i and other_occupied:
                score += get_score(i, j)

        if least_score is None or score <= least_score:
            least_score = score
            best_urinal = i

    return best_urinal

# Enjoy some example code
def fill_urinals(urinals):
    while not all(urinals):
        urinal = pick_urinal(urinals)
        
        if urinal == -1:
            break

        urinals[urinal] = 1
        print(urinals)
        input()

    print("All urinals have been filled")

fill_urinals(generate_urinals(10))
