from game_machine import GameMachine
import heapq


class Casino:
    casino_machines_dict = {}

    def __init__(self, name):
        self.name = name
        Casino.casino_machines_dict[name] = []

    def get_money(self):
        return sum([machine.get_money() for machine in Casino.casino_machines_dict[self.name]])

    def get_name(self):
        return self.name

    def get_machines_count(self):
        return len(Casino.casino_machines_dict[self.name])

    def create_machine(self, game_machine: GameMachine):
        Casino.casino_machines_dict[self.name].append(game_machine)
        # multiply money by -1, so "the richest" machines would be at the beginning of the priority queue
        heapq.heappush(GameMachine.all_game_machines_priority_queue, (game_machine.get_money() * (-1), game_machine))