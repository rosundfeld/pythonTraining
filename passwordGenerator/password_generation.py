import random
import secrets

def generatePassWord(target_length):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_characters = "!@#$%*+=-&*"

    pools = [uppercase_letters, lowercase_letters, digits, special_characters]
    all_characters = ''.join(pools)

    if target_length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")
    
    chooser = secrets.choice
    shuffle = random.SystemRandom().shuffle

    password_chars = [chooser(pool) for pool in pools]
    password_chars += [chooser(all_characters) for _ in range(target_length - 4)]

    shuffle(password_chars)
    return ''.join(password_chars)
