from flask import Flask, request

app = Flask(__name__)

# Keep only the functions and route for the question you receive.
# Delete the other question sections and simplify this file as needed.

# ---------- Q1: CALCULATOR ----------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# ---------- Q2: STUDENT GRADES ----------
def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    # Example grade thresholds; use the exact thresholds in the question.
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"
    return total, average, grade

# ---------- Q3: SHOPPING BILL ----------
def calculate_bill(price, quantity):
    total = price * quantity
    # Example discount for Push 2; adapt to the question.
    discount = total * 0.10
    return total, total - discount

# ---------- Q4: TEMPERATURE CONVERTER ----------
def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

# ---------- Q5: BANKING ----------
def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= 0:
        return balance, "Invalid amount"
    if amount > balance:
        return balance, "Insufficient balance"
    return balance - amount, "Withdrawal successful"

# ---------- Q6: LIBRARY ----------
def add_book(books, name):
    books[name] = True

def view_books(books):
    return [name for name, available in books.items() if available]

def issue_book(books, name):
    if name not in books:
        return "Book not found"
    if not books[name]:
        return "Book already issued"
    books[name] = False
    return "Book issued successfully"


# ---------- SIMPLE WEB PAGE ----------
# For the assessment, retain the route/logic for your chosen question.
@app.route("/")
def home():
    return """
    <h2>Practical Application</h2>
    <p>Change this page to match the question you receive.</p>
    <p>Calculator example: /run?a=10&b=5&operation=add</p>
    <p>Grades example: /run?marks=80,70,90</p>
    <p>Shopping example: /run?price=100&quantity=3</p>
    <p>Temperature example: /run?value=32&operation=f_to_c</p>
    <p>Banking example: /run?balance=500&amount=100&operation=deposit</p>
    <p>Library example: /run?operation=view</p>
    """

# Demo-only in-memory book list.
books = {"Python": True, "Docker": True}

@app.route("/run")
def run():
    try:
        # Q1: Calculator
        op = request.args.get("operation", "add")
        if "a" in request.args and "b" in request.args:
            a, b = float(request.args["a"]), float(request.args["b"])
            if op == "add":
                return f"Result: {add(a, b)}"
            if op == "subtract":
                return f"Result: {subtract(a, b)}"
            if op == "multiply":
                return f"Result: {multiply(a, b)}"
            if op == "divide":
                return f"Result: {divide(a, b)}"

        # Q2: Student grades
        if "marks" in request.args:
            marks = [float(x) for x in request.args["marks"].split(",")]
            total, average, grade = calculate_marks(marks)
            return f"Total: {total}; Average: {average}; Grade: {grade}"

        # Q3: Shopping bill
        if "price" in request.args and "quantity" in request.args:
            total, final_bill = calculate_bill(
                float(request.args["price"]), int(request.args["quantity"])
            )
            return f"Total: {total}; Final bill: {final_bill}"

        # Q4: Temperature
        if "value" in request.args:
            value = float(request.args["value"])
            if op == "c_to_f":
                return f"Result: {c_to_f(value)}"
            if op == "f_to_c":
                return f"Result: {f_to_c(value)}"

        # Q5: Banking
        if "balance" in request.args and "amount" in request.args:
            balance = float(request.args["balance"])
            amount = float(request.args["amount"])
            if op == "deposit":
                return f"Balance: {deposit(balance, amount)}"
            if op == "withdraw":
                new_balance, message = withdraw(balance, amount)
                return f"Balance: {new_balance}; {message}"

        # Q6: Library
        if op == "add":
            name = request.args.get("name")
            if name:
                add_book(books, name)
                return f"Added: {name}"
        if op == "view":
            return "Available: " + ", ".join(view_books(books))
        if op == "issue":
            return issue_book(books, request.args.get("name", ""))

        return "Invalid input or operation", 400
    except (ValueError, KeyError, ZeroDivisionError) as exc:
        return f"Error: {exc}", 400

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
