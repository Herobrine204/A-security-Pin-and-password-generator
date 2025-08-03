import random
def pin():
    c= str(random.randint(1000, 9999))
    print("Your pin is: ", c)
def password():
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits='0123456789'
    symbols='!@#$%^&*()'
    all=lower+upper+digits+symbols
    length=int(input("Enter the length of password(for stronger passwords use a 12 character password): "))
    password = ''.join(random.choice(all) for i in range(length))
    print("Your password is: ", password)
    
def main():
    ch=input("Enter your choice for security password(Pin/Password): ")
    if ch.lower()=='pin':
        print(pin())
    else:
        password()
        
main()

while True:
    ch=input("Do you want to generate a new password? (yes/no): ")
    if ch.lower()=='yes':
        main()
    else:
        break
