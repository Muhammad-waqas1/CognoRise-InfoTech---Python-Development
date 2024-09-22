import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def password_generator():
    try:
        length = int(input("Enter the desired password length (min 8): "))
        if length < 8:
            raise ValueError("Password length should be at least 8.")
        
        password = generate_password(length)
        print(f"Generated password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    password_generator()
