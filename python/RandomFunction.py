import random
import time

class Solutions:
    def generate_otp(self):
        otp = random.randint(100,999)
        print(f"OTP:{otp} \n")

    def dice_game(self):
        dice_number = random.randint(1,6)
        print(f"Dice number:{dice_number} \n")

    def sleep_timer(self):
        sleep_time = random.randint(3,9)
        print(f"Sleeping for {sleep_time} seconds")
        time.sleep(sleep_time)
    
    def random_number(self):
        random_num = random.randint(0,9)
        return random_num


if __name__ == "__main__":
    s = Solutions()
    print("Enter your choice for: \n 1. generate opt \n 2. dice game \n 3. sleep timer\n 4. guess number")
    choice = ""
    while True:
        option = input("Enter option here:").strip()
        if option == '1':
            s.generate_otp()
        elif option == '2':
            s.dice_game()
        elif option == '3':
            s.sleep_timer()
        elif option == '4':
            random_vlu = s.random_number()
            x = input("\n Enter your guess number (0-9):")
            if random_vlu == x:
                print("\nYour guessed number is correct.\n")
            else:
                print(f"\n Your guessed number is not correct.\n Correct number: {random_vlu}")
        else:
            print("Option is not valid.\n")
            continue
        
        choice = input("Do you want to continue (y/n):")
        if choice.lower() == 'n':
            print("\n Exiting the program... \n")
            break
        