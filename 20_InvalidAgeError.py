# 20. Creating a Custom Exception Assignment:
# Create a custom exception InvalidAgeError.
# Write a function check_age(age) that raises this exception
# if age < 18. Handle it with try...except.

def run():
    # Custom Exception
    class InvalidAgeError(Exception):
        def __init__(self, message= "\nAge must be 18 or older."):
            self.message = message
            super().__init__(self.message)
            
            
    # Function thta uses the custom exception
    def check_age(age):
        if age < 18:
            raise InvalidAgeError(f"\nInvalid age: \033[1;3;31m{age}\033[0m. You must be 18 or older.")
        else:
            print(f"\n✅ Access granted. Age is \033[1;3;92m{age}\033[0m.")
            
            
    # Testing
    try:
        age_input = int(input("\n\033[1;3;34mEnter your age: \033[0m"))
        check_age(age_input)
    except InvalidAgeError as e:
        print("\n❌ Error:", e)
    except ValueError:
        print("\n⚠️  Please enter a valid number.")
        

# call the main function
if __name__ == "__main__":
    run() 