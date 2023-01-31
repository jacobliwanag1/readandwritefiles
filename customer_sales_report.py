import csv

customers = open('sales.csv','r')


customer_file = csv.reader(customers, delimiter=',')
   
next(customer_file)


csv_outfile=open('salesreport.csv','w')

csv_outfile.write('Customer,Total')
csv_outfile.write('\n')

cust_id = 250
GTOTAL=0

for record in customer_file:
    if int(record[0])==cust_id:
        T3=float(record[3])
        T4=float(record[4])
        T5=float(record[5])
        TOTAL=T3+T4+T5
        GTOTAL=GTOTAL+TOTAL
    
    elif int(record[0])!=cust_id:
        csv_outfile.write(str(cust_id))
        csv_outfile.write('\t')
        csv_outfile.write(str(GTOTAL))
        csv_outfile.write('\n')
        cust_id+=1
        GTOTAL=0
        T3=float(record[3])
        T4=float(record[4])
        T5=float(record[5])
        TOTAL=T3+T4+T5
        GTOTAL=GTOTAL+TOTAL
    elif cust_id==262:
        StopIteration

customers.close()
csv_outfile.close()


    



    
        
