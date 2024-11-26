import streamlit as st
import math

# Set up the app layout to make it look like a real calculator
st.set_page_config(page_title="Advanced Calculator", layout="centered")

# Custom function to handle different calculator operations
def calculate(operation, num1, num2=None):
    try:
        if operation == 'Add':
            return num1 + num2
        elif operation == 'Subtract':
            return num1 - num2
        elif operation == 'Multiply':
            return num1 * num2
        elif operation == 'Divide':
            if num2 == 0:
                return 'Cannot divide by zero!'
            return num1 / num2
        elif operation == 'Power':
            return num1 ** num2
        elif operation == 'Square Root':
            return math.sqrt(num1)
        elif operation == 'Logarithm':
            return math.log(num1, num2)
        elif operation == 'Sin':
            return math.sin(math.radians(num1))
        elif operation == 'Cos':
            return math.cos(math.radians(num1))
        elif operation == 'Tan':
            return math.tan(math.radians(num1))
        elif operation == 'Factorial':
            return math.factorial(int(num1))
        else:
            return "Invalid Operation"
    except Exception as e:
        return str(e)

# App Header
st.title("Advanced Python Calculator")

# Option for basic or advanced mode
mode = st.selectbox("Choose Mode", ["Basic Calculator", "Advanced Calculator"])

# Display basic calculator UI
if mode == "Basic Calculator":
    st.subheader("Basic Calculator")

    # User inputs for basic calculator
    num1 = st.number_input("Enter the first number", value=0)
    num2 = st.number_input("Enter the second number", value=0)

    # Dropdown for basic operation selection
    operation = st.selectbox(
        "Choose an operation",
        ("Add", "Subtract", "Multiply", "Divide")
    )

    if st.button("Calculate"):
        result = calculate(operation, num1, num2)
        st.write(f"Result: {result}")

# Display advanced calculator UI
elif mode == "Advanced Calculator":
    st.subheader("Advanced Calculator")

    # User inputs for advanced calculator
    num1 = st.number_input("Enter the first number", value=0)
    
    # Additional input for second number (only for binary operations)
    num2 = None
    advanced_operations = (
        "Add", "Subtract", "Multiply", "Divide", 
        "Power", "Square Root", "Logarithm", 
        "Sin", "Cos", "Tan", "Factorial"
    )

    operation = st.selectbox("Choose an advanced operation", advanced_operations)

    if operation not in ("Square Root", "Sin", "Cos", "Tan", "Factorial"):
        num2 = st.number_input("Enter the second number", value=0)

    # Perform the calculation for the advanced calculator
    if st.button("Calculate"):
        if operation in ("Square Root", "Sin", "Cos", "Tan", "Factorial"):
            result = calculate(operation, num1)
        else:
            result = calculate(operation, num1, num2)

        st.write(f"Result: {result}")

