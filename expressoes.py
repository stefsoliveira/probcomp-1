class Node():
    def __init__(self, value=None, next=None, previous=None):
        self._value = value
        self._next = next
        self._prev= previous

    def __str__(self):
        return str(self._value)

class Stack():
    def __init__(self):
        self._head = None

    def __str__(self):  #gerar a string
        if self.isEmpty():
            return '[]'
        aux_node = self._head
        strg = ''
        while aux_node is not None:
            strg += str(aux_node._value)
            aux_node = aux_node._next
            if aux_node is not None:
                strg +=' '
        return strg + ''

    def isEmpty(self):
        return self._head is None

    def push(self, value=None):
        new_node = Node(value)
        if self.isEmpty():
            self._head = new_node #alterar
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node #alterar

    def pop(self):
        if not self.isEmpty():
            if self._head._next == None:
                self._head = self._head._next #alterar
            else:
                self._head._prev = None
                self._head = self._head._next #alterar


def checkExpression(entrada):
    pilha = Stack()
    for i in range(len(entrada)):
        if entrada[i] == '{' or entrada[i] == '(' or entrada[i] == '[':
            pilha.push(entrada[i])
        elif entrada[i] == '}' or entrada[i] == ')' or entrada[i] == ']':
            if pilha.isEmpty():
                return "N"
            else:
                if pilha._head._value == '{' and entrada[i] == '}':
                    pilha.pop()
                elif pilha._head._value == '(' and entrada[i] == ')':
                    pilha.pop()
                elif pilha._head._value == '[' and entrada[i] == ']':
                    pilha.pop()
                else:
                    return "N"
    if pilha.isEmpty():
        return "S"
    else:
        return "N"

while True:
    try:
        entrada = input()
        print(checkExpression(entrada))
    except EOFError:
        break