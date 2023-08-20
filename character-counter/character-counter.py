def main():
    user_input = input("Enter a sentence or phrase: ")
    character_count = len(user_input.replace(" ", ""))
    print(f"The number of characters (excluding spaces) in the input is: {character_count}")

if __name__ == "__main__":
    main()
