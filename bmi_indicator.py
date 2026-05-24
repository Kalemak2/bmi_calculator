def indicator(bmi):
    match bmi:
        case float() | int() as val if val < 18.5:
            return "Underweight"
        case float() | int() as val if 18.5 <= val < 25:
            return "Normal weight"
        case float() | int() as val if 25.0 <= val < 30:
            return "Overweight"
        case float() | int() as val if val >= 30:
            return "Obesity"