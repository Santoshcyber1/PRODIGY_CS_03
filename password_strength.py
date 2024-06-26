import re

def password_strength(password):
    # Criteria checks
    length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Feedback messages
    feedback = []

    if not length:
        feedback.append("Password must be at least 8 characters long.")
    if not has_upper:
        feedback.append("Password must include at least one uppercase letter.")
    if not has_lower:
        feedback.append("Password must include at least one digit.")
    if not has_digit:
        feedback.append("Password must include at least one special character.")
    if not has_special:
        feedback.append("Password must include at least one special character.")

    # Assessing strength
    if length and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length and (has_upper or has_lower) and (has_digit or has_special):
        strength = "Medium"
    else:
        strength = "Weak"

    # Output the result
    return {
        "strength": strength,
        "feedback": feedback if feedback else ["Password meets all criteria."]
    }

# Example usage
password = input("Enter your password: ")
result = password_strength(password)
print(f"Strength: {result['strength']}")
print("Feedback:")
for item in result['feedback']:
    print(f"- {item}")
