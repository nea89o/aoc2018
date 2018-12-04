from collections import defaultdict

from antlr4 import CommonTokenStream, ParseTreeWalker
from antlr4 import InputStream

from commons import get_input
from day4.GrammarLexer import GrammarLexer
from day4.GrammarListener import GrammarListener
from day4.GrammarParser import GrammarParser


def parse_date(date: GrammarParser.DateContext):
    mon = int(date.month.text)
    day = int(date.day.text)
    min = int(date.minute.text)
    return mon * 31 + day, min


class GuardTimeListener(GrammarListener):

    def enterWakeup(self, ctx: GrammarParser.WakeupContext):
        date: GrammarParser.DateContext = ctx.parentCtx.date()
        date = parse_date(date)
        events.append((date, 'wakeup'))

    def enterAsleep(self, ctx: GrammarParser.AsleepContext):
        date: GrammarParser.DateContext = ctx.parentCtx.date()
        date = parse_date(date)
        events.append((date, 'asleep'))

    def enterShift(self, ctx: GrammarParser.ShiftContext):
        date: GrammarParser.DateContext = ctx.parentCtx.date()
        date = parse_date(date)
        events.append((date, ctx.guard.text))


def find_times():
    current_guard = 0
    asleep_since = []
    for time, ev in events:
        if ev == 'asleep':
            asleep_since = time
        elif ev == 'wakeup':
            if type(current_guard) != str:
                print(type(current_guard))
                print(current_guard)
                print(time)
            day_table = guards[current_guard][asleep_since[0]]
            for minute in range(asleep_since[1], time[1]):
                day_table[minute] = True
        else:
            current_guard = ev


def parse_tree():
    lexer = GrammarLexer(InputStream(txt))
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.root()
    listener = GuardTimeListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


def find_sums():
    for guard, times in guards.items():
        sleepy_time[guard] = sum(map(sum, times.values()))


def find_sleepiest_minute(guard):
    mm = defaultdict(int)
    for day, minutes in guards[guard].items():
        for minute, sleeps in minutes.items():
            if sleeps:
                mm[minute] += 1
    return max(mm.items(), key=lambda x: x[1])


def find_sleepiest_minute_guard():
    currentmax = 0
    gm, mm = '0', 0
    for guard in guards.keys():
        minute, value = find_sleepiest_minute(guard)
        if value > currentmax:
            currentmax = value
            gm, mm = guard, minute
    return int(gm) * mm


txt = get_input(4)
events = []
sleepy_time = defaultdict(int)
guards = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
parse_tree()

events.sort()
find_times()
find_sums()

sleepiest = max(sleepy_time, key=sleepy_time.get)
sleepiest_minute = find_sleepiest_minute(sleepiest)[0]

if __name__ == '__main__':
    print('first:', sleepiest_minute * int(sleepiest))
    print('second:', find_sleepiest_minute_guard())
