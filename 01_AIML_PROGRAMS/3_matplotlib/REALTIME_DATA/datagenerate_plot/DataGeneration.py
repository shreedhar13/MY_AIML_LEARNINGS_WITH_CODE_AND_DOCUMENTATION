import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]
#newline='' so that each row is writen without giving gap in between preceeding rows,if u dont use newline='' then after writing each row ,1row place is leaved
''' ie;
x_value,total_1,total_2

0,1000,1000

1,994,998

2,988,997

3,989,993

4,986,995 like this
''' 
'''x_value,total_1,total_2
   0,1000,1000
   1,1001,1004
   2,1001,1000
   3,1003,996  if u use newline=''
'''

with open('data.csv', 'w',newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a',newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(1)