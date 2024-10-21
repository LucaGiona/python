def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

chessboard(3)
#in range solution

def chessboard(length):
    for raw in range(length):
        line = ""
        for col in range(length):
            if (raw +col) %2 == 0:
                line += "1"
            else:
                line += "0"
        print("second", line)

chessboard(3)