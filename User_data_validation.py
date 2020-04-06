import random
import string


def user_validation(): #Main function
    def append_users(user_details, first_name, last_name, user_mail, pass_reset, user_id): #funtion appends each user detail dictionary to overall user details dictionary
        user = {
            "id": user_id,
            "firstname": first_name,
            "lastname": last_name,
            "email": user_mail,
            "password": pass_reset
        }
        user_details.append(user)

    def generate_pass(first_name, last_name, string_length=5): #function to generate password
        letters = string.ascii_lowercase
        rand_let = ''
        for i in range(string_length):
            rand_let += random.choice(letters)

        user_password = ''
        user_password += first_name[:2] + last_name[:2] + rand_let
        return user_password

    def user_output(user_details): #function to print all user details
        for i in range(len(user_details)):
            output = (f"""
                                  id: {user_details[i]['id']} 
                                  firstname: {user_details[i]['firstname']} 
                                  lastname: {user_details[i]['lastname']} 
                                  email: {user_details[i]['email']} 
                                  password: {user_details[i]['password']}
                                  {'- ' * 20}"""
                      )
            print(output)

    user_details = [] #Dictionary to store all user details

    user_id = 0
    while True:
        print('Please enter your Details')
        first_name = input('Enter your First name: ')
        last_name = input('Enter your Last name: ')
        user_mail = input('Enter your E-mail: ')
        if len(first_name) < 2 or len(last_name) < 2:
            print('''First or last name cannot be less than 2 characters. Please enter correct details again''')
            continue
        user_password = generate_pass(first_name, last_name)
        print('Your system generated password is', user_password)
        while True:
            pass_choice = input(''' Do you like your Like generated password?
                          Enter 'Yes' to save password
                          Enter 'No' to create custom password: ''').lower()
            if pass_choice == 'yes':
                print(f'Your password {user_password} is saved')
                user_id += 1
                append_users(user_details, first_name, last_name, user_mail, user_password, user_id)
                break
            elif pass_choice == 'no':
                while True:
                    user_generated = input('Please input your desired password: ')
                    if len(user_generated) < 7:
                        print('Password must not be less than 7 characters')
                        continue
                    break
                user_id += 1
                append_users(user_details, first_name, last_name, user_mail, user_generated, user_id)
                print(f'Your password is now saved as: {user_generated} ')
                break
            else:
                print("please choose either 'Yes' or 'No'")
                continue

        while True:
            user_choice = input('''Enter another user data?
Yes or No: ''').lower()
            if not user_choice == 'yes' and not user_choice == 'no':
                continue
            break
        if user_choice == "no":
            user_output(user_details)
            break
        elif user_choice == "no":
            continue


user_validation()
