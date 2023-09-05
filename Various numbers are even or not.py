# Function we want to test
def is_even(number):
    return number % 2 == 0

# Test cases
def test_is_even():
    # Check if 2 is even (it should be)
    assert is_even(2) == True

    # Check if 5 is even (it should not be)
    assert is_even(5) == False

    # Check if 0 is even (it should be)
    assert is_even(0) == True

    # Check if -4 is even (it should be)
    assert is_even(-4) == True

    # Check if 7 is even (it should not be)
    assert is_even(7) == False

# Run the test cases
test_is_even()
print("All tests have passed successfully.")
