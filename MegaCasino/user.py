import heapq


from game_machine import GameMachine


class User:
    def __init__(self, name: str, money: float):
        if len(name) >= 2:
            self.name = name
        else:
            raise ValueError('Please put a valid name (2 chars or more)')
        if money >= 0:
            self.money = money
        else:
            raise ValueError('The amount of money should be 0 or greater')

    def get_money(self):
        return self.money

    def set_money(self, money: float):
        self.money = money

    def play(self, money: float):
        if money > self.get_money():
            print('This user does not have that much money')
            return
        if len(GameMachine.all_game_machines_priority_queue) == 0:
            print('There are no game machines created yet')
            return
        # choose machine with the most money from priority queue
        game_machine = \
            heapq.heappop(GameMachine.all_game_machines_priority_queue)[1]
        # check if machine has enough money to pay the biggest prize
        if game_machine.get_money() >= money * 3:
            self.set_money(self.get_money() - money)
            profit = game_machine.play(money)
            self.set_money(self.get_money() + profit)
            return profit
        else:
            print('Please put less money or wait for machines to be recharged')
            return 0
