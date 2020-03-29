def parse_ranges(ranges_string):
    result = []
    for part in ranges_string.split(','):
        if '-' in part:
            a, b = part.split('-')
            a, b = int(a), int(b)
            result.extend(range(a, b + 1))
        else:
            a = int(part)
            result.append(a)
    return result
    


from itertools import chain

def parse_range(rng):
    parts = rng.split('-')
    if 1 > len(parts) > 2:
        raise ValueError("Bad range: '%s'" % (rng,))
    parts = [int(i) for i in parts]
    start = parts[0]
    end = start if len(parts) == 1 else parts[1]
    if start > end:
        end, start = start, end
    return range(start, end + 1)

def parse_range_list(rngs):
    return sorted(set(chain(*[parse_range(rng) for rng in rngs.split(',')])))




print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
#[1, 2, 4, 8, 9, 10]
#[0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]

