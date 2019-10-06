from math import atan2, pi

def get_angle(d, h):
    return atan2(h, h+d) / pi * 180.0
    

for i in range(1, int(input()) + 1):
    h,a=map(float, input().split())
    epsilon=0.0000001
    lo = -h + epsilon
    hi = 10**50

    while hi-lo > epsilon:
        mid = (lo + hi) / 2

        angle = get_angle(mid, h)

        if angle > a:
            lo = mid + epsilon
        else:
            hi = mid

    result = "%0.8f" % abs(mid)
    print("Case {}: {}".format(i, result))
