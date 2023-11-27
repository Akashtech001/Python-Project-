# Conversion factors
GRAMS_TO_POUNDS = 0.002205
METERS_TO_MILLIMETERS = 1000
METERS_TO_KILOMETERS = 1000

def grams_to_pounds(grams):
    return grams * GRAMS_TO_POUNDS

def length_conversion(value, source_unit, target_unit):
    if source_unit == 1:  # Millimeters
        if target_unit == 2:  # Meters
            return value / METERS_TO_MILLIMETERS
        elif target_unit == 3:  # Kilometers
            return value / (METERS_TO_MILLIMETERS * METERS_TO_KILOMETERS)
    elif source_unit == 2:  # Meters
        if target_unit == 1:  # Millimeters
            return value * METERS_TO_MILLIMETERS
        elif target_unit == 3:  # Kilometers
            return value / METERS_TO_KILOMETERS
    elif source_unit == 3:  # Kilometers
        if target_unit == 1:  # Millimeters
            return value * METERS_TO_KILOMETERS * METERS_TO_MILLIMETERS
        elif target_unit == 2:  # Meters
            return value * METERS_TO_KILOMETERS
    return value

def main():
        print("Program starting.")
        print("Welcome to unit conversion program.")
        print("Options below:")
        print("1 - Grams to pounds")
        print("2 - Length conversions")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting...")
            return
        elif choice == "1":
            grams = float(input("Insert grams: "))
            pounds = grams_to_pounds(grams)
            print(f"{grams} grams converts to {pounds} pounds.")
        elif choice == "2":
            print("Select units from list: ")
            print("1 - Millimeters")
            print("2 - Meters")
            print("3 - Kilometers")
            source_unit = int(input("Source unit(1-3): "))
            target_unit = int(input("Target unit(1-3): "))
            distance = float(input("Insert distance: "))
            converted_distance = length_conversion(distance, source_unit, target_unit)
            unit_names = ["mm", "m", "km"]
            print(f"{distance} {unit_names[source_unit - 1]} converts to {converted_distance} {unit_names[target_unit - 1]}")
        else:
            print("Unknown option.")

if __name__ == "__main__":
    main()
    print("Program ending.")
