def sortNums(list_to_sort, start=0, end=None):
    if end is None:
            end = (len(list_to_sort))
    if (end - start > 1):
        middle = (start + end) // 2
        sortNums(list_to_sort, start, middle)
        sortNums(list_to_sort, middle, end)
        mergeNums(list_to_sort, start, middle, end)
    return list_to_sort

def mergeNums(list_to_sort, start, middle, end):
    left_list = list_to_sort[start:middle]
    right_list = list_to_sort[middle:end]
    l, r = 0,0
    for n in range(start, end):
        if l >= len(left_list):
            list_to_sort[n] = right_list[r]
            r = r + 1
        elif r >= len(right_list):
            list_to_sort[n] = left_list[l]
            l = l + 1
        elif left_list[l] < right_list[r]:
            list_to_sort[n] =left_list[l]
            l = l+1
        else:
            list_to_sort[n] =right_list[r]
            r = r+1


parameters = list(map(int,input().split()))
num_files = parameters[0]
bytes_limit = parameters[1]
files = list(map(int,input().split()))
sorted_files = sortNums(files)
folders = [0 for i in range(num_files)]


i = 0
j = len(sorted_files) - 1
k=0
while i<j:
    if sorted_files[i] + sorted_files[j] > bytes_limit:
        folders[k] = sorted_files[j]
        j -= 1
        k += 1
    else:
        if folders[k] + sorted_files[i] + sorted_files[j] <= bytes_limit:
            folders[k] += sorted_files[i] + sorted_files[j]
        else:
            k += 1
            folders[k] = sorted_files[i] + sorted_files[j]
        i += 1
        j -= 1

if i == j:
    if folders[k] + sorted_files[i] <= bytes_limit:
        folders[k] += sorted_files[i]
    else:
        k += 1
        folders[k] = sorted_files[i]

counter = 0
for i in range(len(folders)):
    if folders[i] != 0:
        counter += 1
    else:
        break

print(counter)
