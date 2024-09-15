# start

while True:
    number1: int = int(input('enter a number1:'))
    number2: int = int(input('enter a number2:'))
    number3: int = int(input('enter a number3:'))
    is_valid_number1 = 0 <= number1 <= 100
    is_valid_number2 = 10 <= number2 <= 60
    is_valid_number3 = 60 <= number3 <= 100
    sum_numbers = number1 + number2 + number3
    avg_numbers = sum_numbers / 3

    if is_valid_number1 and is_valid_number2 and is_valid_number3 and not \
            avg_numbers != number2:
        break

# stop
