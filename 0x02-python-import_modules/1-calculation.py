#!/usr/bin/python3

if __name__=="__main__":
    """print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub,mul,div

    a = 10
    b = 5

    print("{}+{}={}".format(a,b,add,add(a,b)))
    print("{}-{}={}".format(a,b,add,sub(a,b)))
    print("{}*{}={}".format(a,b,add,mul(a,b)))
    print("{}/{}={}".format(a,b,add,div(a,b)))
