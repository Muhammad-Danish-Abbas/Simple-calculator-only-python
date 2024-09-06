# prompt: Write the code age calculator, you ask me date, month and year so you give me reply second, minutes, hours, days, months and years with months. 

import datetime

def age_calculator():
    """Calculates age in seconds, minutes, hours, days, months, and years."""

    # Get birthdate from the user
    try:
        birth_day = int(input("Enter your birth day (1-31): "))
        birth_month = int(input("Enter your birth month (1-12): "))
        birth_year = int(input("Enter your birth year: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Get current date
    now = datetime.datetime.now()
    birthdate = datetime.datetime(birth_year, birth_month, birth_day)

    # Calculate age
    age = now - birthdate

    # Calculate age in different units
    age_seconds = age.total_seconds()
    age_minutes = age_seconds / 60
    age_hours = age_minutes / 60
    age_days = age_hours / 24
    age_years = age_days / 365.25  # Account for leap years
    age_months = age_years * 12

    # Print the results
    print(f"Your age in seconds: {age_seconds:.2f}")
    print(f"Your age in minutes: {age_minutes:.2f}")
    print(f"Your age in hours: {age_hours:.2f}")
    print(f"Your age in days: {age_days:.2f}")
    print(f"Your age in months: {age_months:.2f}")
    print(f"Your age in years: {age_years:.2f}")

# Call the function to start the age calculator
age_calculator()