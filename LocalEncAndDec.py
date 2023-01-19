# This is Debug code and not need to be distributed

with open("outenc.txt", "rb") as in_file:
    data = in_file.read()

with open("indec.txt", "wb") as out_file:
    out_file.write(data)
