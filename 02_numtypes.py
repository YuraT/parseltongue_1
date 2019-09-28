def main():
    age = int(input("Greetings, human. What is your age? \n"))
    print("In five years you will be {}.".format(age+5))
    print("When you live ten times as long you will be {}.".format(age*10))
    print("Your age divided by 3 equals {} remainder {}.".format(age//3, age%3))
main()