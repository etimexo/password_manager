mode = input("Do you want to add a new password or view existing ones? (add/view) ")
def add():
    name = input('Input account name: ')
    pwd = input('Input account password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + pwd + "\n")
def view():
    with open('passwords.txt', 'r') as f:
        
        for line in f.readlines():
            data = line.rstrip()
            print()
            user, passw =  data.split(": ")
            print(user, "\n Password: ",passw)

if mode == "add":
    add()
elif mode == "view":
    view()
else:
    quit()