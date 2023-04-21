import psycopg2 as pg2
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


weight = int(input("Weight in kilograms: "))
height = int(input("Height in centimeters: "))
gender = input("Gender: ").lower()

print(bmi(weight, height))
print(suggested_weight(height, gender))

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
            food = input('Are you going to eat something else? : ')

    if not food_found:
        print('No such food in the database!')
    food = input('Are you going to eat something else? : ')

print(f'Total calories for your meal : {total_calories}.')

# database connection closed
connection.close()

