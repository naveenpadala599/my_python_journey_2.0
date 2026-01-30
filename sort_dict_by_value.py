dt = {5:4, 1:6, 6:3}

print({key:value for key, value in sorted(dt.items(), key=lambda x:x[1])})
