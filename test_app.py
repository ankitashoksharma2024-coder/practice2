# Keep/update the tests for the question you choose.
# These basic tests cover all six sets of helper functions.
from app import (
    app, add, subtract, multiply, divide, calculate_marks,
    calculate_bill, c_to_f, f_to_c, deposit, withdraw,
    add_book, view_books, issue_book
)

def test_calculator():
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(2, 3) == 6
    assert divide(10, 2) == 5

def test_grades():
    total, average, grade = calculate_marks([80, 70, 90])
    assert total == 240
    assert average == 80
    assert grade == "B"

def test_shopping():
    assert calculate_bill(100, 3) == (300, 270.0)

def test_temperature():
    assert c_to_f(0) == 32
    assert f_to_c(32) == 0

def test_banking():
    assert deposit(500, 200) == 700
    assert withdraw(500, 200) == (300, "Withdrawal successful")
    assert withdraw(100, 200) == (100, "Insufficient balance")

def test_library():
    data = {}
    add_book(data, "Python")
    assert view_books(data) == ["Python"]
    assert issue_book(data, "Python") == "Book issued successfully"
    assert view_books(data) == []

def test_health():
    client = app.test_client()
    assert client.get("/health").status_code == 200
