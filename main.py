class employee:
    def __init__(self, name, payroll):
        self.name = str(name)
        self.payroll = int(payroll)
    
    def __repr__(self):
        return f"{self.name} {self.payroll}"
    
    def __payroll_netto__(self):
       a = round(round(self.payroll * 0.0976,2) + round(self.payroll * 0.015,2) + round(self.payroll * 0.0245,2), 2)
       b = round(self.payroll-a,2)
       c = round(b*0.09, 2)
       e = round(b*0.0775, 2)
       f = round(111.25, 2)
       g = round(self.payroll - f - a, 2)
       h = round(g, 0)
       i = round(((h)*0.18)-46.33,2)
       j = round(i-e, 2)
       k = round(j, 0)
       self.payrollnetto = round((self.payroll - a - c - k), 2)
       return round(self.payrollnetto, 2)
    
    def __obliczanie_skladki__(self):
        self.skladki = round(self.payroll *0.0976, 2) + round(self.payroll*0.065, 2) + round(self.payroll*0.0193,2) + round(self.payroll*0.0245,2) + round(self.payroll*0.001,2)
        return round(self.skladki,2)

    def __koszt__(self):
        self.koszt = round(self.payroll + self.skladki, 2)
        return self.koszt
    def __razem__(self):
        return round(self.payroll + self.__obliczanie_skladki__(),2)      

all_emp = int(input())
emp = []
for n in range(all_emp):
    name_payroll = input().split()
    name = name_payroll[0]
    payroll = name_payroll[1]
    employee_obj = employee(name, payroll)
    emp.append(employee_obj)

rounded_costs = 0 

for m in range(all_emp):
    rounded_costs += emp[m].__razem__()
    name = emp[m].name
    payroll = emp[m].payroll
    print(name, f"{emp[m].__payroll_netto__():.2f}", f"{emp[m].__obliczanie_skladki__():.2f}", f"{emp[m].__koszt__():.2f}")

print(rounded_costs)