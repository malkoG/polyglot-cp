answer=0
while True:
    try: answer+=input().count("joke")
    except: break
print(answer)
