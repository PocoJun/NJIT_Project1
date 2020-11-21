import random

def food_get():
    food_list = ["Pork Cutlet", "Bulgogi", "Ramen", "Macaron", "Kimchi", "Sushi", "Chicken Soup", "Udon"]
    # random food choice
    choose = random.choice(food_list)
    return choose