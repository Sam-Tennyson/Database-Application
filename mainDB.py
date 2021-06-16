from pythondb import DBHelper

def Application():
    db = DBHelper()
    while True:

        print("--------------WELCOME--------------")
        print()
        print("Press 1 to Insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()

        choice = int(input())

        try:

            if choice == 1:
                # Insert User
                uid = int(input("Enter user Id - "))
                uname = input("Enter user name - ")
                ph = input("Enter Phone - ")

                db.insert_user(uid, uname, ph)

            elif choice == 2:
                # display user
                db.fetch_all()
            
            elif choice == 3:
                # delete user
                uid = int(input("Enter the Userid you want to delete ?"))
                db.delete_user(uid)
            
            elif choice == 4:
                # update User
                uid = int(input("Enter user Id"))
                nUname = input("Enter NEW name")
                nph = input("Enter NEW Phone")

                db.update_user(uid, nUname, nph)
            
            elif choice == 5:
                break
        
            else:
                print("Invalid Input")

        except Exception as e:

            print(e)
            print("Invalid details | Try Again ...!!!")    



if __name__ == "__main__":
    Application()
