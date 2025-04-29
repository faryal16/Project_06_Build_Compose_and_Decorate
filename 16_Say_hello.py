# 16. Function Decorators Assignment:
# Write a decorator function log_function_call that
# prints "Function is being called" before a function executes. Apply it to a function say_hello().


def run():
    # Decorator function
    def log_function_call(func):
        """
        Decorator that logs a message before calling the target function.
        """
        def wrapper():
            print("\nFunction is being called...")
            return func()
        return wrapper

    # Function with decorator
    @log_function_call
    def say_hello():
        """
        Function to greet the user.
        """
        print("\n👋 Hello there! Welcome!")
        
    # Call the decorated function
    say_hello()


# call the main function
if __name__ == "__main__":
    run() 