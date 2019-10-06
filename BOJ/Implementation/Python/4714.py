while True:
    s=input()
    if s[0]=='-':
        break
    s=float(s)
    print("Objects weighing {} on Earth will weigh {} on the moon.".format("%.2f" % s, "%.2f" % (s*0.167)))
