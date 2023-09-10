def WHERE_MINMAX(li_No): #nums_list #max_num #min_num
    if len(li_No) == 0:
        return "No numbers provided. Therefore nothing is made"  # When empty list occurs
    MX_No = li_No[0]
    MI_No = li_No[0]
    for num in li_No:
        if num > MX_No:
            MX_No = num
        if num < MI_No:
            min_num = num
    return MX_No, MI_No
    
def main():
    # Where user registers a list of numbers (making sure they are spaced out ex. [1 2 3])
    # Where the conversion is occuring
    #The array in question #input_numbers
    IN_No = [] 
    IN_User = input("Enter a list of numbers separated by spaces: ")
    try:
        IN_No = [int(num) for num in IN_User.split()]
    except ValueError:
        print("Registered Values Are Invalid (Make Sure they are NUMBERS and are spaced apart. (ex = 1 2 3")
        return
    Output = WHERE_MINMAX(IN_No)

    if isinstance(Output, str):  # Check if the result is a string using isisntance)():
        print(Output) 
    else:
        max_number, min_number = Output
        print(f"The Maxmimum Given Amount Within The List Is: {max_number}") #Output for Maximum Value
        print(f"The Minumum Given Amount Within The List Is: {min_number}") #Output for Minimum Value

if __name__ == "__main__":
    main()