import pandas as pd


print('Hello world')


# university

name = ('Middlesex university')
qes = ('my university name')
id = ('my student id is M01101027.')
#print(qes,  'is',  name,  'and',  id)
print(f"{qes} is {name} and {id}")

#fruits

fruits = ["mango", "banana", "apple", "orange"]
prices = [10, 20, 30, 40,22]
for i in range(len(fruits)):
    print(f"the prices of {fruits[i]} is {prices[i]}")
fruits.append('grapes')
fruits.remove('banana')
print(fruits)

#people

students = ['Alice', 'Bob','charlie', 'Diana', 'Ethan', 'Fred']
age = [ 20, 21,23, 24, 25, 26000000]
grade = [ 'A', 'B', 'C','D', 'E', 'F']
score = [ 10,20,30,40,50,60]
for i in range(len(students)):
    print(f"{students[i]} is {age[i]} years old, has a grade of {grade[i]} and scored {score[i]} nmbers")
  #  df = pd.dataframe({'students': students, 'age': age, 'grade': grade, 'score': score})
#print(df)