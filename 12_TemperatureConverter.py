# 12. Static Methods Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

def run():
    class TemperatureConverter:
        @staticmethod
        def celsius_to_fahrenheit(c):
            return (c * 9/5) + 32

    # Example usage
    temp_c = 37
    print(f"\n🔄 Converting \033[1;34m{temp_c}°C\033[0m to Fahrenheit...\n")
    temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
    print(f"🌡️ {temp_c}°C is equal to \033[1;33m{temp_f}°F\033[0m")


# call the main function
if __name__ == "__main__":
    run() 