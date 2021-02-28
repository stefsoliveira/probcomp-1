boots = int(input())
list_of_sizes = [[0,0] for i in range(31)]
counter = 0

for i in range(boots):
    boots_number = input().split()
    address = int(boots_number[0]) - 30
    if boots_number[1] == 'D':
        if list_of_sizes[address][1]>0:
            list_of_sizes[address][1] -= 1 #E
            counter+=1
        else:
            list_of_sizes[address][0] += 1  # D
    if boots_number[1] == 'E':
        if list_of_sizes[address][0] > 0:
            list_of_sizes[address][1]-=1  # E
            counter+=1
        else:
            list_of_sizes[address][1] += 1  # E


print(counter)
