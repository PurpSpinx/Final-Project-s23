from manager import Manager
PIN="0000"
def login():

    while True:
        p=input("Enter PIN: ")
        if p==PIN:
            break
def menu():
    print("pick an option")
    print("1. generate password")
    print("2. update password")
    print("3. delete password")
    print("4. get password")
    print("5. Quit")
    choice=input("Enter option:")
    return choice 
def generate_pass(m):
    site=input("Enter site name:")
    usr=input("Enter username:")
    length=input("password length: ")
    print("password:"+ m.generate_password(site,usr,length))
def get_pass(m):
    site=input("Enter site name:")
    usr=input("Enter username:")
    print("username:",usr)
    print("password:",m.get_password(site,usr))
def delete(m):
    site=input("Enter site:")
    usr=input("Enter username")
    m.delete(site,usr)
def update(m):
    site=input("enter site")
    usr=input("Enter usr")
    p=input("Enter new pass:")
    m.update(site,usr,p)
    print("password update")
def main():
    login()
    m=Manager()
    m.load()
    while True:
        choice=menu()
        if choice==1:
            generate_pass(m)
        elif choice==2:
            update(m)
        elif choice==3:
            delete(m)
        elif choice ==4:
            get_pass()
        else:
            m.save()
            break

main()
