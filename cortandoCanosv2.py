def findHighestNumber(n1, n2):
    if n1 >= n2:
        return n1
    else:
        return n2


def findMaxPrice(size_limit, pipes, prices, num_pipes):  # mochila booleana
    if num_pipes == 0 or size_limit == 0:  # primeira linha da tabela
        return 0
    if (pipes[num_pipes - 1] > size_limit):
        return findMaxPrice(size_limit, pipes, prices, num_pipes - 1)
    else:
        return findHighestNumber(prices[num_pipes - 1] + findMaxPrice(size_limit - pipes[num_pipes - 1], pipes, prices, num_pipes - 1),
            findMaxPrice(size_limit, pipes, prices, num_pipes - 1))

parameters = list(map(int,input().split()))
num_pipes = parameters[0]
size_limit = parameters[1]
pipes = [None for p in range(num_pipes)]
prices = [None for p in range(num_pipes)]

for i in range(num_pipes):
    numbers_input = list(map(int, input().split()))
    pipes[i] = numbers_input[0]
    prices[i] = numbers_input[1]

print(findMaxPrice(size_limit, pipes, prices, num_pipes))
