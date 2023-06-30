try:
    numerator = int(input("Give Numerator:"))
    denominator = int(input("Give Denominator:"))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot Divide By Zero")


print("Code completed successfully")