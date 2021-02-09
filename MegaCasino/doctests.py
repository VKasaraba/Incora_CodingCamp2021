import doctest
from super_admin import SuperAdmin
from user import User
from casino import Casino


def DocTests():
    """
    --- Should create instances with no problem
    >>> super_admin = SuperAdmin('Volodya', 50_000.5)
    >>> user = User('Oksana', 1000)

    --- Check the value error is raised when necessary
    >>> super_admin2 = SuperAdmin('V', 500_000.5)
    Traceback (most recent call last):
     ...
    ValueError: Please put a valid name (2 chars or more)

    --- Check the value error is raised when necessary
    >>> super_admin3 = SuperAdmin('Volodya', -1)
    Traceback (most recent call last):
     ...
    ValueError: The amount of money should be 0 or greater

    --- Should create instances of casinos with no problem
    >>> super_admin.create_casino('My Casino')
    >>> super_admin.create_casino('Your Casino')

    --- Check the impossibility of creation of the same casino
    >>> super_admin.create_casino('My Casino')
    This casino already exists

    --- Check that 2 casinos are created by a given super_admin
    >>> print(len(super_admin.casinos))
    2

    --- Should create instances of game machines with no problem, transferring money from admin to his machines
    >>> print('Admin money before machines creation:', super_admin.get_money())
    Admin money before machines creation: 50000.5
    >>> super_admin.create_game_machine_in_casino(1_000, 'My Casino')
    >>> super_admin.create_game_machine_in_casino(5_000, 'My Casino')
    >>> super_admin.create_game_machine_in_casino(1_000.15, 'My Casino')
    >>> super_admin.create_game_machine_in_casino(10_000, 'Your Casino')
    >>> print('Admin money after machines creation:', super_admin.get_money())
    Admin money after machines creation: 33000.35

    --- Check that the numbers of machines in each casino are correct
    >>> print(len(Casino.casino_machines_dict[super_admin.casinos[0].get_name()]))
    3
    >>> print(len(Casino.casino_machines_dict[super_admin.casinos[1].get_name()]))
    1

    --- Check the method take money from casino My Casino
    >>> print('Admin money before collecting:', super_admin.get_money())
    Admin money before collecting: 33000.35
    >>> print('Casino money before collecting:', super_admin.casinos[0].get_money())
    Casino money before collecting: 7000.15
    >>> super_admin.take_money_from_casino('My Casino', 3000)
    >>> print('Admin money after collecting:', super_admin.get_money())
    Admin money after collecting: 36000.35
    >>> print('Casino money after collecting:', super_admin.casinos[0].get_money())
    Casino money after collecting: 4000.15

    --- Check the put money in machine method when trying to put money in machine with wrong id
    >>> super_admin.put_money_in_machine_by_id(9, 100_000)
    No game machine with this id found in casinos owned by this super admin

    --- Check put money in machine method, the initial amount of money in machine 1 is 0, after executing take money method
    >>> print('Admin money before putting money in a machine:', super_admin.get_money())
    Admin money before putting money in a machine: 36000.35
    >>> print('Machine money before receiving more money:', super_admin.find_machine_and_casino_by_id(1)[0].get_money())
    Machine money before receiving more money: 0
    >>> super_admin.put_money_in_machine_by_id(1, 1000)
    >>> print('Admin money after putting money in the machine:', super_admin.get_money())
    Admin money after putting money in the machine: 35000.35
    >>> print('Machine money after receiving more money:', super_admin.find_machine_and_casino_by_id(1)[0].get_money())
    Machine money after receiving more money: 1000

    --- Check the delete machine method when trying to put money in machine with wrong id
    >>> super_admin.delete_game_machine_by_id(9)
    No game machine with this id found in casinos owned by this super admin

    --- Check the delete machine method
    >>> print('Number of machines in My Casino before deleting:', len(Casino.casino_machines_dict[super_admin.casinos[0].get_name()]))
    Number of machines in My Casino before deleting: 3
    >>> super_admin.delete_game_machine_by_id(2)
    >>> print('Number of machines in My Casino after deleting:', len(Casino.casino_machines_dict[super_admin.casinos[0].get_name()]))
    Number of machines in My Casino after deleting: 2
    """


if __name__ == '__main__':
    doctest.testmod(verbose=True)
