word = "dgdhjdghdf"
alphabet = "fgh"
for x in range(len(word)):
    threealphabet = word [x:x+3]
    print(threealphabet)
    if alphabet in threealphabet :
         print("1")
    else:
         print("-1")