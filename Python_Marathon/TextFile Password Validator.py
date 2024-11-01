#a simple program to validate a password based on a text file by Brighton Masaraure (@rootzw).


#open the text file
myPassword = open('secret.txt')
#read contents of the text file
secretpsswrd = myPassword.read()
print('Enter your password')
typedPasswrd = input()
#compare user input with password stored in text file (validation)
if typedPasswrd == secretpsswrd:
    print('Access Granted')
    if typedPasswrd == '12345':
        print('You are a weirdo loser')
else:
    print('Access denied')