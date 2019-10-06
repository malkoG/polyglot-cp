def message(year):
    if year % 4 == 0:
        if (year >= 1914 and year <= 1918) or (year >= 1939 and year <= 1945):
            return "Games cancelled"
        elif year > 2016:
            return "No city yet chosen"
        else:
            return "Summer Olympics"
    else:
        return "No summer games"

while True:
    n=int(input())
    if n == 0:
        break
    print("{} {}".format(n, message(n)))