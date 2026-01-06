with open("body.txt", "r") as f:
    data = f.seek(1)
    a=f.read(2)
    print(a[0])
    print(a[1])
