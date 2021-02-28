class Node():
    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_next(self):
        return self.__next

    def set_next(self, value):
        self.__next = value


class List():
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):  #gerar a string
        if self.isEmpty():
            return '[]'
        aux_node = self.__head
        strg = ''
        while aux_node is not None:
            strg += str(aux_node.get_value())
            aux_node = aux_node.get_next()
            if aux_node is not None:
                strg +=' '
        return strg + ''

    def isEmpty(self):
        return self.__head is None

    def add_to_end(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def remove(self, value_to_remove):
        aux_node = self.__head
        aux_prev_node = None
        while aux_node != None:  # pode usar um for se souber o tamanho da lista
            if value_to_remove == aux_node.get_value():
                if aux_prev_node is not None:
                    aux_prev_node.set_next(aux_node.get_next())
                else:
                    self.__head = aux_node.get_next()
                break
            else:
                aux_prev_node = aux_node
                aux_node = aux_node.get_next()


total_of_people = int(input())
line_of_people = input().split()
total_of_removals = int(input())
people_to_remove = input().split()
line = List()
for i in range(total_of_people):
    line.add_to_end(line_of_people[i])

for j in range(total_of_removals):
    line.remove(people_to_remove[j])
print(line)







