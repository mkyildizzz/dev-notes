data = [154, 138, 164, 166, 146, 156]

decoded = "".join([chr(x - 77) for x in data])

print(decoded)
