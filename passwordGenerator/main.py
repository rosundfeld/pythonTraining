from password_generation import generatePassWord

def main():
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        password = generatePassWord(length)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()