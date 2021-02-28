This is a project for admission to Incora Coding Camp 2021.
The project task is described in the file task.pdf.

-- How to download --
git clone https://github.com/VKasaraba/Incora_CodingCamp2021.git

-- Running the tests --
Open the PowerShell in a folder with doctests.py file and run the following command:
'python3 doctests.py'
OR run the file explicitly in your IDE

-- Project Structure --
Files casino.py, game_machine.py, user.py, super_admin.py contain corresponding classes.
File doctests.py contains doctests to test the methods' validity. 
File runner.py is for you to create new instances and use all methods written in the project.


-- Classes description --
Class SuperAdmin inherits from class User. When created an instance of SuperAdmin class,
you can use methods create_casino(casino_name: str) and create_game_machine_in_casino(game_machine_money: float, casino_name: str)
to create instances of Casino class and GameMachine class, even without importing them into your runner.py file.
The method take_money_from_casino(casino_name: str, money_to_take: float) substracts given amount of money
from game machines that belong to this casino (subtraction occurs in sequence from the machine with the most amount of money to 
the smallest amount) and adds it to the super admin's sum of money that created this casino. 
On the country, method put_money_in_machine_by_id(game_machine_id: int, money_to_put) substructs given amount
of money from super admin (casino's creator) and adds it to the specific game machine by id. 
The method delete_game_machine_by_id(game_machine_id: int) deletes the game machine and splits its money equally between other game machines in the same casino. If there are no more game machines, the money
go to super admin. 

The method play() is available to instances of User class and its children (SuperAdmin class). For this method,
a priority queue 'all_game_machines_priority_queue' in class GameMachine is created. When the method play()
is called, it pops the machine with the most amount of money, to have greater chances it has enough money to pay
the biggest prize, and avoid iterating through all created machines. If "the richest" machine doesn't have enough money
to pay the biggest prize, the corresponding message is shown. 

To keep track of which machines belong to which casino, a 'casino_machines_dict' dictionary was created. It stores
values in format key:value, where the 'key' is a casino's name, and the 'value' is a list of machines.
