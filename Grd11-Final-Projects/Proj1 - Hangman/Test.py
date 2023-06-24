pieces_in_row = [(5, 6)]
x = 5
y = 6

if (x, y) not in pieces_in_row:
    pieces_in_row.append((x, y))
else:
    print("already present")

print(pieces_in_row)
print(len(pieces_in_row))