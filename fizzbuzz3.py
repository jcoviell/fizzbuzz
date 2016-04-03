

try:
    n = int(sys.argv[1])
except (IndexError, ValueError, NameError):
    while True:
        try:
            n = int(raw_input("Please enter a number: "))
            break
        except ValueError:
            print("Please enter a number...")

for n in range(1,n+1):
    if n % 5 == 0 and n % 3 == 0:
        print "FizzBuzz"
    elif n % 3 == 0:
        print "Fizz"
    elif n % 5 == 0:
        print "Buzz"
    else:
        print n