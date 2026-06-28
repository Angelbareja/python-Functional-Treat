def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

while True:
    print("\nWelcome to the data analyzer and transformer program.")
    print("Main menu :")
    print("1.Input data")
    print("2.Display data summary")
    print("3.Calculate factorial")
    print("4.Filter data by threshold ")
    print("5.Sort data")
    print("6.Display dataset statistics")
    print("7.Exit program")
    
    choice = int(input("\n Please enter your choice :"))

    if choice == 1:
        data = list(map(int,input("\n Enter data for a 1D array :").split()))
        print("\n Data has been stored successfully!")

    elif choice == 2:
        if len(data) == 0:
            print("NO data available")
        else:    
            print("Data Summary :")
            print("-Total element :",len(data))
            print("-Minimum value :",min(data))
            print("-Maximum value :",max(data))
            print("-sum of all value :",sum(data))
            print("-Average value :",sum(data) / len(data))

    elif choice == 3:
        num = int(input("Enter a number to calculate its factorial :"))

        print("Factorial of (num) is :",factorial(num))

    elif choice == 4:
        threshold = int(input("Enter a threshold value to filter out data above this value :"))
        filtered = list(filter(lambda x:x > threshold, data))
        print("Filtered Data :",filtered)

    elif choice == 5:
        print("Choose sorting option :")
        print("1. Ascending")
        print("2. Descending")

        option = int(input("Enter your choice :"))

        if option == 1:
            data.sort()
            print("Sorted data in ascending order :",data)
        elif option == 2:
            data.sort(reverse=True)
            print("Sorted data in descending order :",data)

        else:
            print("Invalid choice!")

    elif choice == 6:
        print("Dataset Statistics :")
        print("-Minimum value :",min(data))
        print("-Maximum value :",max(data))
        print("-sum of all value :",sum(data))
        print("-Average value :",sum(data) / len(data))

    elif choice == 7:
        print("Thank you for using the data analyzer and transformer program. Goodbye!")

    else:
        print("Invalid choice! please try again.")
        
            

        
    
