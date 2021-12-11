#Return the sum of unique values in an array
#Examples:
nums1 = [1, 2, 2, 3, 4] #expected value = 8
nums2 = [1, 1, 1, 1, 1] #expected value = 0
nums3 = [1, 2, 3, 4, 5] #expected value = 15

def unique_counter(nums):
    
    digit_counter = { 0 : 0, 1 : 0 , 2 : 0 , 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0 }

    print("Input: " + str(nums))
    
    sum = 0

    for i in range(len(nums)): #checking a range of indices the same length as the input array
        for count in digit_counter: # and checking each digit from 0-9 in the counter
            if nums[i] == count: #if the array value at this index is the same as the digit we are currently checking in the counter
                digit_counter[count] = digit_counter[count] + 1
                
                #Used these lines to debug the code:
                #print("Array value: " + str(nums[i]))
                #print("Checking for the digit: " + str(count))
                #print(str(count) + " counter increased to: " + str(digit_counter[count]))

    print('The unique numbers are:')

    #Calculate the sum of the unique values:
    
    for count in digit_counter:
        if digit_counter[count] == 1:
            print(str(count))
            sum = sum + count

    print("The sum of the unique values is: " + str(sum))


unique_counter(nums1)
unique_counter(nums2)
unique_counter(nums3)


