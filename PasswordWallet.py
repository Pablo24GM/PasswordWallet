<<<<<<< Updated upstream
def add_psw():
    old_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                old_act, old_psw = old_line.rstrip().split(" , ")
                old_dict = {"account": old_act, "password": old_psw}
                old_list.append(old_dict)
    except FileNotFoundError:
        pass
    print('\n-------------------------------')
    act = input("Account's Name: ").lower()
    for existing_act in old_list:
        if existing_act["account"] == act:
            print('\n------------------------------------------------------------------------------------------------')
            print('Account already exists. You can look for it in "1. Look for a Password" Option at the Main menu.')
            print('------------------------------------------------------------------------------------------------\n')
            return
    print('\n-------------------------------')
    psw = input("Account's Password: ")

    dic_line = create_dic_line(act, psw)
    new_data = create_new_data(old_list, dic_line)
    update_wallet(new_data)

    print('\n-----------------------------------------------------')
    print(f'The Account "{act}" was succesfully added!')
    print('-----------------------------------------------------\n')

def create_dic_line(a, b):
    c = {'account': a, 'password': b}
    return c

def create_new_data(d, e):
    d.append(e)
    f = sorted(d, key=lambda x: x['account'].lower())
    g = "\n".join([f"{h['account']} , {h['password']}" for h in f])
    return g

def update_wallet(i):
    with open("password_wallet.txt", "w") as j:
        j.write(i)
##################################################
def view_psw():
    account_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                account_dict = {"account": act, "password": psw}
                account_list.append(account_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    print('\n-------------------------------------------------')
    account_name = input("What is the Account's name you are looking for?: ").lower()
    for act in account_list:
        if act["account"] == account_name:
            print('\n-------------------------------------------------------------------------')
            print(f"The Password for {act['account']} is: {act['password']}")
            print('-------------------------------------------------------------------------\n')
            return
    print('\n-----------------------------------------------------------------------------------------------------------------------------')
    print(f'The Account "{account_name}" was not found. You can add it to your Wallet in "2. Add a new Password" Option at the Main menu.')
    print('-----------------------------------------------------------------------------------------------------------------------------\n')

def edit_psw():
    old_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                old_dict = {"account": act, "password": psw}
                old_list.append(old_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    print('\n-------------------------------------------------')
    account_name = input("What Account's Password would you like to edit?: ").lower()
    for current_act in old_list:
        if current_act["account"] == account_name:
            print('\n-------------------------------------------------------------------')
            print(f'The current Password for "{current_act["account"]}" is:')
            print(f"{current_act['password']}")
            print('\n-------------------------------------------------------------------')
            new_psw = input("Please enter the new Password for this Account: ")
            while new_psw == current_act["password"]:
                print('\n------------------------------------------------------------------------------------------')
                print("You are repeating the same existing Password for this Account, please try something different.")
                new_psw = input("\nPlease enter the new Password for this Account: ")
            print('\n---------------------------------------------------------------')
            user_confirmation = input("Are you sure you wish to continue with this change? ( y / n ): ")
            while user_confirmation not in ("y", "n"):
                print('\n---------------------------------------------')
                print("Invalid choice, please select a valid option.")
                user_confirmation = input("Are you sure you wish to continue with this change? ( y / n ): ")
            if user_confirmation == "y":
                current_act["password"] = new_psw
                print('\n--------------------------------------------------------------------------')
                print(f'New Password for "{current_act["account"]}" has been changed successfully!')
                print('--------------------------------------------------------------------------\n')
                break
            elif user_confirmation == "n":
                print('\n------------------------------------------------')
                print("The Account's Password change has been canceled.")
                print('------------------------------------------------\n')
                return
    else:
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
        print(f'The Account "{account_name}" was not found. You can add it to your Wallet in "2. Add a new Password" Option at the Main menu.')
        print('-----------------------------------------------------------------------------------------------------------------------------\n')

    new_list = sorted(old_list, key=lambda x: x["account"].lower())
    new_data = "\n".join([f"{a['account']} , {a['password']}" for a in new_list])

    with open("password_wallet.txt", "w") as file:
        file.write(new_data)

def del_psw():
    old_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                old_dict = {"account": act, "password": psw}
                old_list.append(old_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    print('\n------------------------------------------------------------------')
    account_name = input("What Account would you like to Delete?: ").lower()
    for current_act in old_list:
        if current_act["account"] == account_name:
            print('\n------------------------------------------------------------------------------------------------')
            user_confirmation = input(f'Are you sure you wish to Delete the "{current_act["account"]}" Account & Password? ( y / n ): ')
            while user_confirmation not in ("y", "n"):
                print('\n---------------------------------------------')
                print("Invalid choice, please select a valid option.")
                print('\n------------------------------------------------------------------------------------------------')
                user_confirmation = input(f'Are you sure you wish to Delete the "{current_act["account"]}" Account & Password? ( y / n ): ')
            if user_confirmation == "y":
                print('\n--------------------------------------------------------------------------------------------------')
                print(f'The Account and Password for "{current_act["account"]}" has been Deleted successfully!')
                print('--------------------------------------------------------------------------------------------------\n')
                old_list.remove(current_act)
                break
            elif user_confirmation == "n":
                print('\n-----------------------------------------------')
                print("The Account's Delete process has been canceled.")
                print('-----------------------------------------------\n')
                return
    else:
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
        print(f'The Account "{account_name}" was not found. You can add it to your Wallet in "2. Add a new Password" Option at the Main menu.')
        print('-----------------------------------------------------------------------------------------------------------------------------\n')

    new_list = sorted(old_list, key=lambda x: x["account"].lower())
    new_data = "\n".join([f"{a['account']} , {a['password']}" for a in new_list])

    with open("password_wallet.txt", "w") as file:
        file.write(new_data)

def show_all_psw():
    account_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                account_dict = {"account": act, "password": psw}
                account_list.append(account_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    if not account_list:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return
    else:
        print('\n----------------------------------')
        for account in account_list:
            print(f"{account['account']}")
        print('----------------------------------\n')

def main():
    while True:
        print(" =========================================================================== ")
        print("                    Welcome to your Password Wallet                          ")
        print(" A safe place where you can store, view, edit, and delete all your passwords ")
        print(" =========================================================================== ")

        print(" ---------------------------------")
        print(" ---- What do you want to do? ----")
        print(" ---------------------------------")
        print(" | 1. Look for a Password        |")
        print(" | 2. Add a new Password         |")
        print(" | 3. Edit an existing Password  |")
        print(" | 4. Delete a Password          |")
        print(" | 5. Show All Accounts          |")
        print(" | 6. Exit the Wallet            |")
        print(" ---------------------------------")

        choice = input(" Enter your choice ( 1 | 2 | 3 | 4 | 5 | 6 ): ")
        if choice == "1":
            view_psw()
        elif choice == "2":
            add_psw()
        elif choice == "3":
            edit_psw()
        elif choice == "4":
            del_psw()
        elif choice == "5":
            show_all_psw()
        elif choice == "6":
            print("\n=================================================")
            print("Thank you for using The Password Wallet. Goodbye.")
            print("=================================================\n")
            break
        else:
            print("\n ----------------------------------------------- ")
            print("  Invalid choice, please select a valid option.  ")
            print(" ----------------------------------------------- \n")

if __name__ == "__main__":
    main()
=======
def add_psw():
    old_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                old_act, old_psw = old_line.rstrip().split(" , ")
                old_dict = {"account": old_act, "password": old_psw}
                old_list.append(old_dict)
    except FileNotFoundError:
        pass
    print('\n-------------------------------')
    act = input("Account's Name: ").lower()
    for existing_act in old_list:
        if existing_act["account"] == act:
            print('\n------------------------------------------------------------------------------------------------')
            print('Account already exists. You can look for it in "1. Look for a Password" Option at the Main menu.')
            print('------------------------------------------------------------------------------------------------\n')
            return
    print('\n-------------------------------')
    psw = input("Account's Password: ")

    dic_line = create_dic_line(act, psw)
    new_data = create_new_data(old_list, dic_line)
    update_wallet(new_data)

    print('\n-----------------------------------------------------')
    print(f'The Account "{act}" was succesfully added!')
    print('-----------------------------------------------------\n')

def create_dic_line(a, b):
    c = {'account': a, 'password': b}
    return c

def create_new_data(d, e):
    d.append(e)
    f = sorted(d, key=lambda x: x['account'].lower())
    g = "\n".join([f"{h['account']} , {h['password']}" for h in f])
    return g

def update_wallet(i):
    with open("password_wallet.txt", "w") as j:
        j.write(i)
##################################################
def view_psw():
    account_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                account_dict = {"account": act, "password": psw}
                account_list.append(account_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    print('\n-------------------------------------------------')
    account_name = input("What is the Account's name you are looking for?: ").lower()
    for act in account_list:
        if act["account"] == account_name:
            print('\n-------------------------------------------------------------------------')
            print(f"The Password for {act['account']} is: {act['password']}")
            print('-------------------------------------------------------------------------\n')
            return
    print('\n-----------------------------------------------------------------------------------------------------------------------------')
    print(f'The Account "{account_name}" was not found. You can add it to your Wallet in "2. Add a new Password" Option at the Main menu.')
    print('-----------------------------------------------------------------------------------------------------------------------------\n')

def edit_psw():
    old_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                old_dict = {"account": act, "password": psw}
                old_list.append(old_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    print('\n-------------------------------------------------')
    account_name = input("What Account's Password would you like to edit?: ").lower()
    for current_act in old_list:
        if current_act["account"] == account_name:
            print('\n-------------------------------------------------------------------')
            print(f'The current Password for "{current_act["account"]}" is:')
            print(f"{current_act['password']}")
            print('\n-------------------------------------------------------------------')
            new_psw = input("Please enter the new Password for this Account: ")
            while new_psw == current_act["password"]:
                print('\n------------------------------------------------------------------------------------------')
                print("You are repeating the same existing Password for this Account, please try something different.")
                new_psw = input("\nPlease enter the new Password for this Account: ")
            print('\n---------------------------------------------------------------')
            user_confirmation = input("Are you sure you wish to continue with this change? ( y / n ): ")
            while user_confirmation not in ("y", "n"):
                print('\n---------------------------------------------')
                print("Invalid choice, please select a valid option.")
                user_confirmation = input("Are you sure you wish to continue with this change? ( y / n ): ")
            if user_confirmation == "y":
                current_act["password"] = new_psw
                print('\n--------------------------------------------------------------------------')
                print(f'New Password for "{current_act["account"]}" has been changed successfully!')
                print('--------------------------------------------------------------------------\n')
                break
            elif user_confirmation == "n":
                print('\n------------------------------------------------')
                print("The Account's Password change has been canceled.")
                print('------------------------------------------------\n')
                return
    else:
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
        print(f'The Account "{account_name}" was not found. You can add it to your Wallet in "2. Add a new Password" Option at the Main menu.')
        print('-----------------------------------------------------------------------------------------------------------------------------\n')

    new_list = sorted(old_list, key=lambda x: x["account"].lower())
    new_data = "\n".join([f"{a['account']} , {a['password']}" for a in new_list])

    with open("password_wallet.txt", "w") as file:
        file.write(new_data)

def del_psw():
    old_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                old_dict = {"account": act, "password": psw}
                old_list.append(old_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    print('\n------------------------------------------------------------------')
    account_name = input("What Account would you like to Delete?: ").lower()
    for current_act in old_list:
        if current_act["account"] == account_name:
            print('\n------------------------------------------------------------------------------------------------')
            user_confirmation = input(f'Are you sure you wish to Delete the "{current_act["account"]}" Account & Password? ( y / n ): ')
            while user_confirmation not in ("y", "n"):
                print('\n---------------------------------------------')
                print("Invalid choice, please select a valid option.")
                print('\n------------------------------------------------------------------------------------------------')
                user_confirmation = input(f'Are you sure you wish to Delete the "{current_act["account"]}" Account & Password? ( y / n ): ')
            if user_confirmation == "y":
                print('\n--------------------------------------------------------------------------------------------------')
                print(f'The Account and Password for "{current_act["account"]}" has been Deleted successfully!')
                print('--------------------------------------------------------------------------------------------------\n')
                old_list.remove(current_act)
                break
            elif user_confirmation == "n":
                print('\n-----------------------------------------------')
                print("The Account's Delete process has been canceled.")
                print('-----------------------------------------------\n')
                return
    else:
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
        print(f'The Account "{account_name}" was not found. You can add it to your Wallet in "2. Add a new Password" Option at the Main menu.')
        print('-----------------------------------------------------------------------------------------------------------------------------\n')

    new_list = sorted(old_list, key=lambda x: x["account"].lower())
    new_data = "\n".join([f"{a['account']} , {a['password']}" for a in new_list])

    with open("password_wallet.txt", "w") as file:
        file.write(new_data)

def show_all_psw():
    account_list = []
    try:
        with open("password_wallet.txt") as file:
            for old_line in file:
                act, psw = old_line.rstrip().split(" , ")
                account_dict = {"account": act, "password": psw}
                account_list.append(account_dict)
    except FileNotFoundError:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return

    if not account_list:
        print('\n--------------------------------------------------------------------------------------------------------------------')
        print('There are no accounts registered yet. You can save new passwords in "2. Add a new Password" Option at the Main menu.')
        print('--------------------------------------------------------------------------------------------------------------------\n')
        return
    else:
        print('\n----------------------------------')
        for account in account_list:
            print(f"{account['account']}")
        print('----------------------------------\n')

def main():
    while True:
        print(" =========================================================================== ")
        print("                    Welcome to your Password Wallet                          ")
        print(" A safe place where you can store, view, edit, and delete all your passwords ")
        print(" =========================================================================== ")

        print(" ---------------------------------")
        print(" ---- What do you want to do? ----")
        print(" ---------------------------------")
        print(" | 1. Look for a Password        |")
        print(" | 2. Add a new Password         |")
        print(" | 3. Edit an existing Password  |")
        print(" | 4. Delete a Password          |")
        print(" | 5. Show All Accounts          |")
        print(" | 6. Exit the Wallet            |")
        print(" ---------------------------------")

        choice = input(" Enter your choice ( 1 | 2 | 3 | 4 | 5 | 6 ): ")
        if choice == "1":
            view_psw()
        elif choice == "2":
            add_psw()
        elif choice == "3":
            edit_psw()
        elif choice == "4":
            del_psw()
        elif choice == "5":
            show_all_psw()
        elif choice == "6":
            print("\n=================================================")
            print("Thank you for using The Password Wallet. Goodbye.")
            print("=================================================\n")
            break
        else:
            print("\n ----------------------------------------------- ")
            print("  Invalid choice, please select a valid option.  ")
            print(" ----------------------------------------------- \n")

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
