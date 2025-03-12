import hashlib
import itertools
import string
import random 

def hash_password(password): 
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_crack(hash_value, max_length=4):
    chars = string.ascii_lowercase + string.digits 
    for length in range(1, max_length +1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            if hash_password(guess) == hash_value:
                return guess 
    return None

def password_strength(password):
    length_score = min(len(password) / 12, 1)
    complexity_score = sum(bool(set(password) & set(c)) for c in (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)) / 4
    score = (length_score + complexity_score) / 2 * 100
    if score < 50:
        return "Weak"
    elif score < 80:
        return "Moderate"
    return "Strong"

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

password = input("Enter a password to hash: ")
hashed_password = hash_password(password)
print(f"\nSHA-256 Hash: {hashed_password}")

if len(password) <= 4 and password.islower():
    print("\nAttempting to crack...")
    cracked_password = brute_force_crack(hashed_password)
    if cracked_password:
        print(f"Cracked Password: {cracked_password}")
    else:
        print("Could not crack the password (too complex)")

strength = password_strength(password)
print(f"\nPassword Strength: {strength}")
if strength == "Weak":
    print(f"Suggest Strong Password: {generate_strong_password()}")