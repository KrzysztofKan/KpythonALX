def is_prime(num):
    flag = False
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            return False
        else:
            return True
        
def is_anagram(string1,string2):     
    # the sorted strings are checked
    if(sorted(string1)== sorted(string2)):
        return True
    else:
        return False
    