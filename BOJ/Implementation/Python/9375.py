for test_case in range(int(input())):
    costume_count=dict()
    costumes=set()
    for clothes_input in range(int(input())):
        _,costume=input().split()
        try:   costume_count[costume] += 1
        except: costume_count[costume] = 1
        costumes.add(costume)

    product = 1
    for costume in costumes:
        product *= costume + 1
    print(product - 1)
