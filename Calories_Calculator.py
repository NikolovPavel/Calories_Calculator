import psycopg2 as pg2
import math
# database connection

connection = pg2.connect(host='localhost', port='5432',
                              database='Products', user='postgres', password='Pavel_nikolov92')

print("Database Connected....")
cur = connection.cursor()
cur.execute('SELECT * FROM products')
print("--------------------------")
rows = cur.fetchall()

# body mass index and weight initial calculation

def bmi(weight, height):
    bmi = float(f"{weight / height ** 2 * 10000:.1f}")
    under_or_overweight = ""
    if bmi < 18.5:
        under_or_overweight = "underweight"
    elif 18.5 <= bmi <= 24.9:
        under_or_overweight = "normal"
    else:
        under_or_overweight = "overweight"
    return f"Your BMI is {bmi} which is considered {under_or_overweight}."


def suggested_weight(height, gender):
    male = height - 100
    female = height - 110
    if gender == "male":
        return f"Suggested weight is around {male} kg."
    else:
        return f"Suggested weight is around {female} kg."


def basal_metabolism_calculation(gender, weight, height, age, activity):
    if gender == 'male':
        bmr = float(weight * 10 + (6.25 * height - 5 * age) + 5)
    else:
        bmr = float(weight * 10 + (6.25 * height - age * 5) - 161)

    if activity == 'none':
        return f'The required calories for maintaining your weight are {math.ceil(bmr * 1.2)} per day!'
    elif activity == 'low':
        return f'The required calories for maintaining your weight are {math.ceil(bmr * 1.375)} per day!'
    elif activity == 'medium':
        return f'The required calories for maintaining your weight are {math.ceil(bmr * 1.55)} per day!'
    elif activity == 'high':
        return f'The required calories for maintaining your weight are {math.ceil(bmr * 1.725)} per day!'
    elif activity == 'very high':
        return f'The required calories for maintaining your weight are {math.ceil(bmr * 1.9)} per day!'


age = int(input("Your age: "))
weight = int(input("Weight in kilograms: "))
height = int(input("Height in centimeters: "))
gender = input("Gender: ").lower()
activity = input("What is your activity? Choose one of these: \n" 
                 "none - no physical activity at all \n"
                 "low  - 1 to 3 workouts per week \n"
                 "medium - 3 to 5 workouts per week \n"
                 "high - 6 to 7 workouts per week \n"
                 "very high - 6 -7 very intensive workouts per week:   ")
print(bmi(weight, height))
print(suggested_weight(height, gender))
print(basal_metabolism_calculation(gender, weight, height, age, activity))

# food input and calories calculation
# all products begin with capital letter and are in the following format 'Apple' !
food = input('What are you going to eat? : ')
food_found = False
total_calories = 0

# while loop, working with the rows from the database

while food != 'No':
    for row in rows:
        food_found = False
        if food in row:
            total_calories += int(row[2])
            print(f'Calories for 100gr of {food} are {row[2]}.')
            print(f'Total calories for your meal : {total_calories}.')
            food_found = True
            break

    if not food_found:
        print('No such food in the database!')
    food = input('Are you going to eat something else? : ')

# Koko ideqta mi za toq print dolu e slednata:
# v bydeshte da slojim promenliva koqto da opredelq kolko kalorii trqbva da qde 4oveka na den(v zavisimost dali iska
# da ka4va ili svalq i toq print da mu izkarva
# kolko mu ostavat za denq, no za momenta shte go ostavq prosto taka da go vidish.
print(f'Total calories for your meal : {total_calories}.')

# database connection closed
connection.close()

