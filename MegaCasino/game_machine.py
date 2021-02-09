from random import randint
import heapq


class GameMachine:
    # priority queue to avoid iterating machines, while looking for one with enough money to pay the biggest prize
    all_game_machines_priority_queue = []
    last_machine_index = 0

    def __init__(self, money):
        self.money = money
        GameMachine.last_machine_index += 1
        self.id = GameMachine.last_machine_index

    # To avoid errors while comparing game machines with equal amount of money,
    # while pushing them to a priority queue
    def __lt__(self, other):
        return self.get_money() >= other.get_money()

    def get_money(self):
        return self.money

    def get_id(self):
        return self.id

    def take_money(self, sum_to_take):
        if sum_to_take <= self.money:
            self.money -= sum_to_take
        else:
            print('Not enough money in this machine')

    def put_money(self, sum_to_put):
        self.money += sum_to_put

    def play(self, sum_to_put):
        self.put_money(sum_to_put)
        result = str(randint(100, 999))
        duplicates = 1  # each number is present at least once
        seen = [result[0]]
        for i in range(1, len(result)):
            if result[i] in seen:
                duplicates += 1
            seen.append(result[i])
        if duplicates == 1:
            profit = 0
        else:
            profit = sum_to_put * duplicates
            self.take_money(profit)
        # add the machine back to the list with new money value
        heapq.heappush(GameMachine.all_game_machines_priority_queue, (self.get_money() * (-1), self))
        return profit
