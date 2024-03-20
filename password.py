master_pwd = input("What is the master password? ")
mode = input("Do you want to add a new password or view existing ones? (add/view) ")
def add():
    name = input('Input account name: ')
    pwd = input('Input account password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + ":\n" + pwd + "\n\n")
def view():
    # with open('passwords.txt', 'r') as f:
    #     f.read('passwords.txt')
    pass

if mode == "add":
    add()
elif mode == "view":
    view()
else:
    quit()