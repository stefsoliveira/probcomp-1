class Node():
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

class Queue(): #First In First Out
    def __init__(self):
        self._head = None
        self._tail = None

    def isEmpty(self):
        return self._head is None

    def add_to_queue(self, value): #add to the end
        new_node = Node(value)
        if self.isEmpty():
            self._head = self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

    def remove_from_queue(self): #remove from the beginning
        if self.isEmpty():
            return False
        first_node_value = self._head._value
        if self._head is self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head._next
        return first_node_value

parties  = int(input())
for n in range(parties):
    house_deck = Queue()
    players = {}
    k = 0
    while True:
        card = input().split()
        if card[0] == '-1':
            break
        elif k == 0:
            for j in card:
                house_deck.add_to_queue(j)
            k += 1
        else:
            players[str(k)] = Queue()
            for j in card:
                players[str(k)].add_to_queue(j)
            k += 1

    round = 1
    winner = False
    while round <= 1000:
        card_house = house_deck.remove_from_queue()
        for num, player in players.items():
            if player.isEmpty():
                print(num)
                round = 1000
                winner = True
            else:
                card_player = player.remove_from_queue()
                if card_player != card_house:
                    player.add_to_queue(card_player)
        house_deck.add_to_queue(card_house)
        round += 1
    if winner is False:
        print(0)