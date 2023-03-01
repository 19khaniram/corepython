class maths:
    def sum(a, b):
        c = a + b
        print("sum=", c)
        return c


    def diff(a, b):
        c = a - b
        print(c)
        return c


    def mult(a, b):
        c = a * b
        print(c)
        return c


    def div(self, a, b):
        c = a / b
        print(c)
        return c

    def factorial(a):
        num = int(input("Enter a number: "))
        value = 1

        for i in range(1, num + 1):
            value = value * i

        print("Factorial of Number=", value)
        return num


    def max(a, b):
        val1 = int(input("enter num 1 ="))
        val2 = int(input("enter num 2 ="))
        if (val1 > val2):
            print("val1 is greater", val1)
        else:
            print("val2 is greater", val2)
            return val1, val2