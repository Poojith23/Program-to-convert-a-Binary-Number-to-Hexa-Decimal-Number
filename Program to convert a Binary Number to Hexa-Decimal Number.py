
# Python3 code to convert BCD to its
# hexadecimal number(base 16).
 
# Function to convert BCD to hexadecimal
def bcdToHexaDecimal(s):
     
    len1 = len(s)
    check = 0
    num = 0
    sum = 0
    mul = 1
    ans = []
 
    # Iterating through the bits backwards
    i = len1 - 1
     
    while(i >= 0):
        sum += (ord(s[i]) - ord('0')) * mul
        mul *= 2
        check += 1
 
        # Computing the hexadecimal number formed
        # so far and storing it in a vector.
        if (check == 4 or i == 0):
             
            if (sum <= 9):
                ans.append(chr(sum + ord('0')))
            else:
                ans.append(chr(sum + 55));
 
            # Reinitializing all variables
            # for next group.
            check = 0
            sum = 0
            mul = 1
         
        i -= 1
         
    len1 = len(ans)
 
    # Printing the hexadecimal
    # number formed so far.
    i = len1 - 1
     
    while(i >= 0):
        print(ans[i], end = "")
        i -= 1
 
# Driver Code
if __name__ == '__main__':
     
    s = "100000101111"
 
    # Function Call
    bcdToHexaDecimal(s)
 
# This code is contributed by Samarth
