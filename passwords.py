#I added an else statement for the user who doesn't want participate within the Main() function. I also added a bit of flare to the initial prompt to make it less mechanical.

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive = False):

    with open(filename, "r", encoding = "utf-8") as file:
    
        for line in file:
            line = line.strip()

            if case_sensitive:
                if word == line:
                    return True
            
            else:
                if word.lower() == line.lower():
                    return True 
            
    return False 


def word_has_character(word, character_list):

    for character in word:
        if character in character_list:
            return True
        
    return False 


def word_complexity(word):

    complex = 0

    if word_has_character(word, LOWER):
        complex += 1

    if word_has_character(word, UPPER):
        complex += 1

    if word_has_character(word, DIGITS):
        complex += 1

    if word_has_character(word, SPECIAL):
        complex += 1 

    return complex    

def password_strength(password, min_length = 10, strong_length = 16):

    if word_in_file(password, "wordlist.txt"): 
        print("Password is a word found in the word list, this does not work. ")
        return 0
    
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a common password, this does not work. ")
        return 0

    if len(password) < min_length:
        print("Password is too short, this does not work. ")
        return 0

    if len(password) >= strong_length:
        print("Password is long and complex, this is a good password. ")
        return 5
        
    complex = word_complexity(password)
    
    strength = 1 + complex
    
    return strength 

def main():

    password =""

    while password.lower() != "q":

        password = input("Enter your password if you dare. If you want to quit, just push 'q': ")

        if password.lower() != "q":

            strength = password_strength(password)

            print(f"Password strength score: {strength}/5")

        else: 
            print("No worries, come back when you're ready to strengthen your password.")

if __name__== "__main__":
    main()


