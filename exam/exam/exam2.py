print("in this year")
monday = 4
counttheweek = 1

for i in range(100):
    monday += 7
    if monday <= 365:
        counttheweek += 1
    else:
        continue

print(int(counttheweek), "is all monday.")
