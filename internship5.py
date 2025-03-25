def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def main():
    while True:
        print("\nText Reverser Menu:")
        print("1. Reverse Character Order")
        print("2. Reverse Word Order")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter text to reverse: ")
            if text.strip():
                print("Reversed Text:", reverse_characters(text))
            else:
                print("Error: Empty input detected!")
        
        elif choice == '2':
            text = input("Enter text to reverse words: ")
            if text.strip():
                print("Reversed Words:", reverse_words(text))
            else:
                print("Error: Empty input detected!")
        
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
