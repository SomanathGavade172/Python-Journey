def main():
    Arr = list()

    print("Enter How many Elements You Want to Store ..?")
    Size = int(input())

    print("Please Enter a Values : ")
    
    for i in range(0, Size):
        No = int(input())
        Arr.append(No)      # Arr.insert(i,no)

    print(Arr)


if __name__ == "__main__":
    main()

