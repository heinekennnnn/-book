word = "ghhfhfdjdu"
alphabet = "hhfhf"
for x in range (len (word)) :
    fivealphabet = word [x:x+5]
    print(fivealphabet)
    if alphabet in fivealphabet :
        print("1")
        break
    else:
        print("-1")
