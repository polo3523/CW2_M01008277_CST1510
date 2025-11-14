import bcrypt

password = 'hello'

def hash_password(pwd):
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def validate_password(pwd, hashed):
    password_bytes = pwd.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user():
    user_name = input('Enter username: ')
    user_password = input('Enter password: ')
    hashed_pwd = hash_password(user_password)
    with open('users.txt', 'a') as f:
        f.write(f'{user_name},{hashed_pwd}\n')
    print('User registered successfully.')
    print(f'User {user_name} registered with hashed password: {hashed_pwd}')
    
register_user()

def login_user():
    user_name = input('Enter username: ')
    user_password = input('Enter password: ')
    with open('users.txt', 'r') as f:
        for line in f:
            stored_name, stored_hashed_pwd = line.strip().split(',')
            if stored_name == user_name:
                if validate_password(user_password, stored_hashed_pwd):
                    print('Login successful.')
                else:
                    print('Invalid password.')
                return
    print('Username not found.')


hashed_password = hash_password(password)
print(f'Hashed password: {hashed_password}')
is_valid = validate_password(password, hashed_password)
print(f'Password is valid: {is_valid}')