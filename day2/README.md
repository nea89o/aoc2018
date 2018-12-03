## Day 2

### Part One
For this part i made use of a python standardlib functionality. You can
use a `Counter("")` to count all chars with the string in a dict-like
type. In the next step we just `sum()` a list comprehension which
filters for either 2 or 3. Lastly we multiply both to find the
checksum.

### Part Two
For this i settled for a simple for loop. The two interesting parts are
that we first ignore identical IDs since we don't want to compare the
same element to itself and we transform the strings into lists, since we
can not subindexes on strings.
