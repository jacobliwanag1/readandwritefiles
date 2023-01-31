import csv

customers = open('EmployeePay.csv','r')


customer_file = csv.reader(customers, delimiter=',')


next(customer_file)

for i in customer_file:
    print('EmpFName:',i[1])
    print('EmpLName:',i[2])
    print('Salary',i[3])
    print('Bonus',i[4])
    S = int(i[3])
    B= float(i[4])
    TP=S+(B*S)
    print('Total Pay:',TP)
    print('\n')
