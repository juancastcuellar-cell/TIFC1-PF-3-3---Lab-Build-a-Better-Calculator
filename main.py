def addmultiplenumbers(numbers):
  total = 0
  for n in numbers:
    total = total + n
  return total

def subtractmultiplenumbers(numbers):
  if len(numbers) == 0:
    raise ValueError("Need at least one number")
  result = numbers[0]
  for n in numbers[1:]:
    result = result - n
  return result


def multiplymultiplenumbers(numbers):
  result = 1
  for n in numbers:
    result = result * n
  return result

def dividemultiplenumbers(numbers):
  if len(numbers) == 0:
    raise ValueError("Need at least one number")
  result = numbers[0]
  for n in numbers[1:]:
    result = result / n  
  return result


def isitaninteger(num):
  return float(num).is_integer()


def isiteven(num):
  return isitaninteger(num) and num % 2 == 0


def ask_for_numbers():
  text = input("Enter numbers separated by spaces: ")
  return [float(part) for part in text.split()]


def main():
  print("calculator")
  while True:
    print("\n1) Add numbers")
    print("2) Subtract numbers")
    print("3) Multiply numbers")
    print("4) Divide numbers")
    print("5) Is it even?")
    print("6) Is it an integer?")
    print("7) Quit")
    choice = input("Choose an option: ")

    if choice == "7":
      print("Goodbye!")
      break

    try:
      if choice == "1":
        print("Result:", addmultiplenumbers(ask_for_numbers()))
      elif choice == "2":
        print("Result:", subtractmultiplenumbers(ask_for_numbers()))
      elif choice == "3":
        print("Result:", multiplymultiplenumbers(ask_for_numbers()))
      elif choice == "4":
        print("Result:", dividemultiplenumbers(ask_for_numbers()))
      elif choice == "5":
        print(isiteven(float(input("Enter a number: "))))
      elif choice == "6":
        print(isitaninteger(float(input("Enter a number: "))))
      else:
        print("Please choose 1-7.")
    except ZeroDivisionError:
      print("You can't divide by zero!")
    except ValueError:
      print("That wasn't a valid number, or you entered no numbers. Try again.")


if __name__ == "__main__":
  main()
