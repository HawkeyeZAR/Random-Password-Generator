import random
import string
import sys


class PasswordGenerator:
    '''
        Generates random list using uppercase, lowercase, numbers and
        special chars.

        Has one function, generate which is using the random library.

        Constructor takes four param, either default values or from input

    '''

    def __init__(self, u, l, n, s):
        """ Initiate constructor """
        self.UPPER = random.choices(string.ascii_uppercase, k=u)
        self.LOWER = random.choices(string.ascii_lowercase, k=l)
        self.NUMBERS = random.choices(string.digits, k=n)
        self.SPECIAL = random.choices('~!@#$%&?', k=s)
  
    def generate(self, l):
        '''
            Generate random selection using the random.sample method
            on a combined list of characters

            return a string of random chars
        '''
        random_sel = self.UPPER + self.LOWER + self.NUMBERS + self.SPECIAL
        #  Shuffle the new list using the sample method
        password = random.sample(random_sel, l)
        return "".join(password)


def get_length():
    '''
        Get the number of chars to be used for each selection.

        return list of int
    '''
    lower_amount, number_amount, special_amount = "", "", ""
    char_types = [lower_amount, number_amount, special_amount]
    char_name = ["lowercase letters", "numbers", "special char's"]

    for i in range(3):
        char_types[i] = input(f"How many {char_name[i]} to use? Range: 2-8 ")
        if int(char_types[i]) >= 2 and int(char_types[i]) <= 8:
            pass
        else:
            print("Sorry, must be between 2 and 8 in length")
            sys.exit()       
    return [char_types[0], char_types[1], char_types[2]]


def main():
    '''
        Prompt user for rquired length pet char type
        Or use X for default values
    '''
    message = print("\nPress X if you want to use system defaults")
    upper_amount = input("How many uppercase letters? Range: 2-5 ") 

    if upper_amount.upper() == 'X':
        print("Using default password length of 16")
        new_password = PasswordGenerator(4, 8, 2, 2)
        pass_len = 16
    else:
        if int(upper_amount) >= 2 and int(upper_amount) <= 5:
            pass_len = get_length()
            u = int(upper_amount)
            l = int(pass_len[0])
            n = int(pass_len[1])
            s = int(pass_len[2])
            new_password = PasswordGenerator(u, l , n , s)
            pass_len = u+l+n+s
        else:
            print("Sorry, must be between 2 and 5 in length")
            sys.exit()
        
    password = new_password.generate(pass_len)
    print(f"\nYour password is: {password}")
    
if __name__ == '__main__':
    main()

