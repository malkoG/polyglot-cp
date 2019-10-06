
while True:
    s=input()
    if s == "0.0":
        break

    mile = float(s)
    roman_mile = mile * 5280.0 / 4854.0
    result1 = "%.2f" % mile
    result2 = "%.2f" % roman_mile
    print("{} English miles equals {} Roman miles or {} paces.".format(result1, result2, round(roman_mile * 1000.0)))
