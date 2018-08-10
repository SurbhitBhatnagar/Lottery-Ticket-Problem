
'''
Here are the instructions to run the program.
From the directory of the code, write 'python Lottery.py' in the CLI.
The 'input' array is the input to the program, and is a list of all the lottery tickets to choose from.

'run_program(input)' is the entry point of the whole code.

'''

def find_lottery(input):     # This function handles the array of lottery tickets as input and returns the selected lottery numbers according to the constraints.
    result = []
    for i in range(len(input)):
        digits_arr = split_num(input[i])        # Check the validity of each lottery number
        temp_res = []
        if len(digits_arr)> 0:                  #the lottery number is valid if the array is not empty
            temp_res.append(input[i])
            temp_res.append(digits_arr)
            result.append(temp_res)
    return result

def split_num(num_str):             # This function handles individual lottery numbers as a string input and checks its validity.
    dig_arr = []
    nmap = {}
    if len(num_str) == 7:      # Handle a 7-digit lottery number
        for i in range(len(num_str)):
            if int(num_str[i]) == 0:        # check if the number is not zero, if any character is zero it makes the number invalid
                return []
            else:
                if int(num_str[i]) not in nmap.keys():          #Check if each digit is unique through hash map
                    nmap[int(num_str[i])] = True
                    dig_arr.append(int(num_str[i]))
    elif len(num_str) >7 and len(num_str) <= 14:           #handle a number which is greater than 7 digits, max number string length can be 7x2 = 14
        dig_arr = singleDoubleValidity(num_str)                # Call function to handle lottery tickets with length between 8 to 14, since the max individual number in the 7 number lottery ticket should be less than 59 (a pair)


    return dig_arr                  #return the array of numbers between 1 to 59 for a valid 7 number long lottery ticket



def singleDoubleValidity(num_str):         # Find pairs, less than 59 and handle lottery numbers with size greater than 7. Example, 4938532894754 -> 49 38 53 28 9 47 54
    size = len(num_str)
    pairCount = len(num_str) - 7        # 7 is the offset to maintain the amount of numbers to be 7, so for example an 8 digit lottery number shall have 8-7 = 1 pair, and 6 single digits

    num_arr = []
    num_map = {}

    new_str = findDoubleDigits(num_str,pairCount)      #brings pair of same digits to the start of the string to be considered as a pair and avoids the condition of repeating numbers
    print ('The new string is {}'.format(new_str))

    i=1
    temp = 0
    while i < len(new_str):
        temp = int(new_str[i-1])
        temp = temp*10 + int(new_str[i])    #find pairs
        if temp <= 59 and pairCount > 0:        #check if pair is valid (< 59)
            pairCount -= 1
            if temp not in num_map.keys():      #check if pair is not repeating in the lottery number
                num_map[temp] = True
                num_arr.append(temp)
            if i+2 < size:
                i += 2
            else:
                i += 1
        else:
            if int(new_str[i-1]) not in num_map.keys():         #Append individual 1-digit numbers if the temp is not a valid pair
                num_arr.append(int(new_str[i-1]))
                num_map[int(new_str[i-1])] = True
            if i == len(new_str)-1:                                 #Handle edge case
                if int(new_str[i]) not in num_map.keys():
                    num_arr.append(int(new_str[i]))
                    num_map[int(new_str[i])] = True
            i += 1
    # return num_arr
    if pairCount == 0 and len(num_arr) == 7:            #Check the validity of the array/ Lottery number
        return num_arr
    else:
        return []

def findDoubleDigits(num_str,pair_count):       #In the scenario of a pair <59, with repeating digits. For eg., '44', '55' etc.
    new_str=""
    double_arr = [ True for i in range(len(num_str))]  #Consider them first as a pair so that they the lottery number can be considered as valid otherwise the lottery number will become invalid under the constrained of repeating numbers out of the 7 numbers in the lottery.

    for i in range(1,len(num_str)):
        if pair_count <= 0:
            break

        if num_str[i-1] == num_str[i]:
            double_arr[i-1] = False
            double_arr[i] = False
            pair_count -= 1

    for j in range(len(double_arr)):
        if double_arr[j] == False:
            new_str = new_str + num_str[j]

    for j in range(len(double_arr)):
        if double_arr[j] == True:
            new_str = new_str + num_str[j]
    return new_str        #Return a modified strig which will consider valid pair of numbers with repeating digits


def run_program(input):         #The main function which runs the whole program by calling the find_lottery function as entry point.
    Result = find_lottery(input)
    print "For the input {}, the lottery tickets are:- \n".format(input)
    for i in range(len(Result)):
        print "{} -> {} ".format(Result[i][0],Result[i][1])
#The input of the program.
input = [ "569815571556", "4938532894754", "1234567", "472844278465445","57984423"]
run_program(input)
