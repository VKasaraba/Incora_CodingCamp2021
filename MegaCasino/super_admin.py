from user import User
from casino import Casino
from game_machine import GameMachine
import heapq


class SuperAdmin(User):
    def __init__(self, name: str, money: float):
        super().__init__(name, money)
        # I supposed that one super admin can create multiple casinos
        self.casinos = []

    def create_casino(self, casino_name: str):
        if len(casino_name) < 2:
            print('Please put a valid name (2 chars or more)')
            return
        if casino_name in [current_casino.get_name() for current_casino in
                           self.casinos]:
            print('This casino already exists')
        else:
            casino = Casino(casino_name)
            self.casinos.append(casino)

    def create_game_machine_in_casino(self, game_machine_money: float,
                                      casino_name: str):
        for current_casino in self.casinos:
            if casino_name == current_casino.get_name():
                if game_machine_money <= self.get_money():
                    self.set_money(self.get_money() - game_machine_money)
                    current_casino.create_machine(
                        GameMachine(game_machine_money))
                else:
                    print('This super admin does not have that much money')
                return
        print('There is no such casino owned by this super admin')

    def take_money_from_casino(self, casino_name: str, money_to_take: float):
        for casino in self.casinos:
            if casino_name == casino.get_name():
                if casino.get_money() >= money_to_take:
                    for machine in Casino.casino_machines_dict[casino_name]:
                        if money_to_take == 0:
                            return
                        GameMachine.all_game_machines_priority_queue.remove(
                            (machine.get_money() * (-1), machine))
                        if machine.get_money() >= money_to_take:
                            machine.take_money(money_to_take)
                            self.set_money(self.get_money() + money_to_take)
                            heapq.heappush(
                                GameMachine.all_game_machines_priority_queue,
                                (machine.get_money() * (-1), machine))
                            return
                        else:
                            money_to_take -= machine.get_money()
                            self.set_money(
                                self.get_money() + machine.get_money())
                            machine.take_money(machine.get_money())
                            heapq.heappush(
                                GameMachine.all_game_machines_priority_queue,
                                (machine.get_money() * (-1), machine))
                else:
                    print('There is not enough money in this casino')
                    return
            else:
                print('There is no such casino owned by this super admin')

    def find_machine_and_casino_by_id(self, game_machine_id: int):
        # Check every game machine in every casino created by this super admin
        for casino in self.casinos:
            for machine in Casino.casino_machines_dict[casino.get_name()]:
                if machine.get_id() == game_machine_id:
                    return machine, casino  # returns a tuple

    def put_money_in_machine_by_id(self, game_machine_id: int, money_to_put):
        queue_tuple = self.find_machine_and_casino_by_id(game_machine_id)
        if queue_tuple is None:
            print(
                'No game machine with this id found in casinos owned by this '
                'super admin')
            return
        found_machine = queue_tuple[0]
        if self.get_money() >= money_to_put:
            # remove the machine from the priority queue, and add it with a new
            # money value
            GameMachine.all_game_machines_priority_queue.remove(
                (found_machine.get_money() * (-1), found_machine))
            self.set_money(self.get_money() - money_to_put)
            found_machine.put_money(money_to_put)
            heapq.heappush(GameMachine.all_game_machines_priority_queue,
                           (found_machine.get_money() * (-1), found_machine))
        else:
            print('This super admin has not enough money')

    def delete_game_machine_by_id(self, game_machine_id: int):
        queue_tuple = self.find_machine_and_casino_by_id(game_machine_id)
        if queue_tuple is None:
            print(
                'No game machine with this id found in casinos owned by this '
                'super admin')
            return
        found_machine = queue_tuple[0]
        found_casino = queue_tuple[1]
        money_to_split = found_machine.get_money()
        GameMachine.all_game_machines_priority_queue.remove(
            (found_machine.get_money() * (-1), found_machine))
        Casino.casino_machines_dict[found_casino.get_name()].remove(
            found_machine)
        del found_machine
        number_of_machines = found_casino.get_machines_count()
        if number_of_machines > 0:
            for machine in Casino\
                    .casino_machines_dict[found_casino.get_name()]:
                # remove the machine from the priority queue, and add it with a
                # new money value
                GameMachine.all_game_machines_priority_queue.remove(
                    (machine.get_money() * (-1), machine))
                machine.put_money(money_to_split / number_of_machines)
                heapq.heappush(GameMachine.all_game_machines_priority_queue,
                               (machine.get_money() * (-1), machine))
        else:
            # if there are no more machines in the casino, give all money to
            # the casino's owner
            self.set_money(self.get_money() + money_to_split)
