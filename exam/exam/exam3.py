thirtyonedays = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
thirtydays = ["Apr", "Jun", "Sep", "Nov"]
lessthanthirtydays = ["Feb"]
X = 0
days = input(" how many days in the year : ")
if days == "365":
    for x in thirtydays:
        if x in thirtydays:
            X += 15
        else:
            continue
    for x in thirtyonedays:
        if x in thirtyonedays:
            X += 15
            X += 1
        else:
            continue
    for x in lessthanthirtydays:
        if x in lessthanthirtydays:
            X += 14
        else:
            continue
elif days == "366":
    for x in thirtydays:
        if x in thirtydays:
            X += 15
        else:
            continue
    for x in thirtyonedays:
        if x in thirtyonedays:
            X += 15
            X += 1
        else:
            continue
    for x in lessthanthirtydays:
        if x in lessthanthirtydays:
            X += 14
            X += 1
        else:
            continue
else:
    print(" error na kubbbbbbbbbb ")

print(int(X), "is all add days.")