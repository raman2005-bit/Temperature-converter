def detect_value_and_unit(user_input):
    """
    Extract number and unit from input like '100C' or '273.15K'
    """
    user_input = user_input.strip().lower()
    value_str = ""
    unit = ""

    # Separate number and unit
    for char in user_input:
        if char.isdigit() or char == "." or char == "-":
            value_str += char
        else:
            unit += char

    try:
        value = float(value_str)
    except ValueError:
        return None, None

    unit = unit.strip()
    return value, unit


def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Convert to Celsius first
    if from_unit == "c":
        temp_c = value
    elif from_unit == "f":
        temp_c = (value - 32) * 5/9
    elif from_unit == "k":
        temp_c = value - 273.15
    else:
        return None

    # Convert Celsius to desired unit
    if to_unit == "c":
        return temp_c
    elif to_unit == "f":
        return (temp_c * 9/5) + 32
    elif to_unit == "k":
        return temp_c + 273.15
    else:
        return None


print("🌡 Temperature Converter (Multi Output) | Type 'exit' to quit")

while True:
    from_input = input("\nEnter temperature with unit (e.g., 100C, 212F, 273K): ")
    if from_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    value, from_unit = detect_value_and_unit(from_input)

    if value is None or from_unit not in ["c", "f", "k"]:
        print("❌ Invalid input! Example: 100C, 212F, 273K")
        continue

    print("\n✅ Conversion Results:")
    for unit in ["c", "f", "k"]:
        if unit != from_unit:  # Don't convert to same unit
            result = convert_temperature(value, from_unit, unit)
            print(f"   {result:.2f}°{unit.upper()}")
