import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))

for arg in sys.argv[1:]:
    print(arg)

    user_input = int(arg)
        
    if user_input:
        for n in range(1,user_input):
            if n % 5 == 0 and n % 3 == 0:
                print "FizzBuzz"
            elif n % 3 == 0:
                print "Fizz"
            elif n % 5 == 0:
                print "Buzz"
            else:
                print n
    
    else:
        user_input = input("Enter the highest number to which you want to play Fizzbuzz: ")
        user_input = int(user_input)
    
        for n in range(1,user_input):
            if n % 5 == 0 and n % 3 == 0:
                print "FizzBuzz"
            elif n % 3 == 0:
                print "Fizz"
            elif n % 5 == 0:
                print "Buzz"
            else:
                print n