num_rows = 9 # initialise number of rows
for i in range(1, num_rows + 1):
    if i <= num_rows // 2 + 1: # for the first half of rows
        print('*' * i) # increasing number of stars will be printed for each row
    else:
        print('*' * (num_rows - i + 1)) # for the second half of rows a decreasing number of stard will be printed for each row
