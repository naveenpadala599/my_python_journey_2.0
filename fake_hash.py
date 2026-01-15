def simple_file_fingerprint(filename):
    total=0
    with open(filename, "rb") as f:
        while True:
            b=f.read(1)
            if b==b"":
                break
            total+=b[0]
    return total
print(simple_file_fingerprint("body.txt"))    
