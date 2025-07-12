try:
    while True:
        Input_for_list_of_numbers = input("Enter a list of numbers separated by spaces: ")
        
        list_of_numbers_str = Input_for_list_of_numbers.split()
        list_of_numbers = [int(num) for num in list_of_numbers_str]
        
        total = sum(list_of_numbers)
        average = total / len(list_of_numbers)
        
        print(list_of_numbers)
        print(average)

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")




                      
