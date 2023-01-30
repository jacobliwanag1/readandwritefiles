import csv

customers = open('customers.csv','r')


customer_file = csv.reader(customers, delimiter=',')

list = []

next(customer_file)

for record in customer_file:
 
    list.append(record)
    



csv_outfile=open('customer_country.csv','w')

csv_outfile.write('first name,last name,country')
csv_outfile.write('\n')

for record in list:
    csv_outfile.write(record[1])
    csv_outfile.write(',')
    csv_outfile.write(record[2])
    csv_outfile.write(',')
    csv_outfile.write(record[4])
    csv_outfile.write('\n')
csv_outfile.close()
