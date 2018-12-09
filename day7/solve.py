from collections import defaultdict

from commons import get_input, remove_empty


def get_requirement(line):
    return line[5], line[36]


def fill_requirements():
    for line in lines:
        needs, gives = get_requirement(line)
        requirements[gives].append(needs)
        _ = requirements[needs]  # to insert all steps, even the ones without gives/needs


def find_available_steps(known, done):
    return [
        gives for gives, needs in requirements.items()
        if gives in known or all(need in done for need in needs)
    ]


def find_order():
    done = set()
    available = set()
    steps = []
    while True:
        available = set(find_available_steps(available, done))
        found = available - set(steps)
        if len(found) == 0:
            break
        step = sorted(found)[0]
        steps.append(step)
        done.add(step)
    return steps


def process_order():
    done = set()
    available = set()
    time = 0
    steps = []
    worker = []

    while True:
        print(time)
        available = set(find_available_steps(available, done))
        found = available - set(steps) - set(map(lambda w: w[0], worker))
        if len(worker) == 0 and len(found) == 0:
            break
        for i in range(len(worker)):
            job, passed = worker[i]
            worker[i] = job, passed + 1

        finished = list(filter(lambda w: w[1] >= ord(w[0]) - ord('A') + 60, worker))
        for d in finished:
            done.add(d[0])
            steps.append(d[0])
        worker = list(filter(lambda w: w[1] < ord(w[0]) - ord('A') + 60, worker))

        for job in list(found)[:5 - len(worker)]:
            worker.append((job, 0))
        time += 1
    return time


lines = remove_empty(get_input(7).splitlines(keepends=False))
requirements = defaultdict(list)
fill_requirements()

if __name__ == '__main__':
    print('first:', ''.join(find_order()))
    print('second:', process_order())
