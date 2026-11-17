
import random

num = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10")
        continue

    attempts = attempts - 1

    if guess == num:
        print("You guessed it! Congratulations!")
        break

    elif guess < num:
        print("Your guess is too low")

    else:
        print("Your guess is too high")

else:
    print("Better luck next time!")
    print("The correct number is:", num)


n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

result = calculate_bmi(weight, height)

print("Your BMI is: {:.2f}".format(result))