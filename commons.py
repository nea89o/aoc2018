from pathlib import Path

import requests

root: Path = Path(__file__).parent
cache: Path = root / 'cache'
cache.mkdir(parents=True, exist_ok=True)
session: str = (root / 'session.txt').read_text().strip()
cookies = dict(session=session)


def identity(x):
    return x


def remove_empty(seq):
    return filter(identity, seq)


def get_input(day: int) -> str:
    cache_file = cache / str(day)
    if cache_file.exists():
        return cache_file.read_text()
    text = requests.get('http://adventofcode.com/2018/day/{}/input'.format(day),
                        cookies=cookies).text.strip()
    cache_file.write_text(text)
    return text

