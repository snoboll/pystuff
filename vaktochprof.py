import matplotlib.pyplot as plt 

vakt = 28000 * 11
vakt_inc = 500 * 12

prof = 36000 * 11
prof_inc = 1000 * 12
month_living = 15000 * 12
yearly_return = 2
tax = 0.3

class Person():
    def __init__(self, salary, sal_inc):
        self.savings = 0
        self.salary = salary
        self.sal_inc = sal_inc

    def add_cash(self):
        self.savings += self.salary * (1-tax)

    def expense(self, cost):
        self.savings -= cost

    def increase_salary(self):
        self.salary += self.sal_inc

    def gain_interest(self):
        self.savings *= yearly_return

    def time_flies(self):
        self.add_cash()
        self.expense(month_living)
        self.gain_interest()
        self.increase_salary()
    
vakt = Person(vakt, vakt_inc)
prof = Person(prof, prof_inc)

vakt_list = []
prof_list = [0,0,0,0,0]
for i in range(50):
    vakt.time_flies()
    vakt_list.append(vakt.savings)
    if i >= 5:
        prof.time_flies()
        prof_list.append(prof.savings)


plt.plot(vakt_list, label='Vaktmästaren')
plt.plot(prof_list, label='Professorn')
plt.title('Vaktmästaren vs professorn, yearly return:' + str(yearly_return) + ', tax:' + str(tax))
plt.legend()
plt.show()