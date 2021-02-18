inc_dict = {'wage': 20, 'bonus': 10}
class Worker:
    name = ''
    surname = ''
    position = ''
    _income = inc_dict

class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)
    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'))

first_worker = Position()
first_worker.name = 'Cory'
first_worker.surname = 'Taylor'
first_worker.position = 'Slipknot'
first_worker._income = {'wage': 25, 'bonus': 10}

second_worker = Position()
second_worker.name = "Jonathan"
second_worker.surname = 'Davis'
second_worker.position = 'Korn'
second_worker._income = {'wage': 30, 'bonus': 10}

first_worker.get_full_name()
first_worker.get_total_income()
second_worker.get_full_name()
second_worker.get_total_income()