print("Application to Demonstration Industrial Programming")

def Addition(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def main():
    print("Enter First Number : ")
    No1 = int(input())
    print("Enter Second Number : ")
    No2 = int(input())

    Sum = Addition(No1, No2)
    print("addition is : ", Sum)

if __name__ == "__main__":
    main()