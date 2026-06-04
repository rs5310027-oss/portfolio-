import random
import string

print("🔐 Password Generator")

length = int(input("Enter password length: "))
use_symbols = input("Include symbols? (yes/no): ").lower()
use_numbers = input("Include numbers? (yes/no): ").lower()

characters = string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)