import random
rand = random.randint(1,10)
# print(f'Random number: {rand}')
def check_num(rand):
    attempts=3
    for attempt in range(attempts):
        num = int(input(f"Attempt {attempt + 1}/{attempts} - Please Guess The Number: "))
        statment=''
        if num+1== rand or num-1==rand:
            statment='your number is too Close'
        elif num<rand:
            statment='your number is too low'
        elif num>rand:
            statment='your number is too High'
        elif rand== num:
            statment='Congrats you guess the number'
            return statment.title()
        print(statment.title())
    return f"Sorry, you've used all attempts. The correct number was {rand}."

print(check_num(rand))  

