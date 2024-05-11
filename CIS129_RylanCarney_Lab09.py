##Rylan Carney
##CIS129
##May 07, 2024
##This code is to create a csv file using with open

#import csv so we can use its functions
import csv


with open('grades.csv', mode='w', newline='') as grades:
    writer = csv.writer(grades)
    writer.writerow(['Mary', 'Sue', 96, 90, 92])
    writer.writerow(['John', 'Smith', 90, 76, 86])
    writer.writerow(['Henry', 'Hooligan', 65, 72, 94])
    writer.writerow(['Rylan', 'Carney', 15, 10, 5])
    writer.writerow(['Klungo', 'Kersimmin', 100, 100, 100])


with open('grades.csv', 'r', newline='') as grades:
    print(f'{"Firstname":<10}{"Lastname":<10}{"Exam1Grade":<10}\
          {"Exam2Grade":<10}{"Exam3Grade":>15}')
    reader = csv.reader(grades)
    for record in reader:
        Firstname, Lastname, exam1grade, exam2grade, exam3grade = record
        print(f'{Firstname:<10}{Lastname:<10}{exam1grade:^10} \
              {exam2grade:<10}{exam3grade:^10}')

        
