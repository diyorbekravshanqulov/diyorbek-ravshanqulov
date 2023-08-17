from os import system as sys
sys("cls")

# 1

def romanToInt(s: str) -> int:
    dct = {
        "I": 1, "V": 5, "X": 10, "L": 50, 
        "C": 100, "D": 500, "M": 1000
    }
    son = dct[s[0]]
    
    i = 1
    while i < len(s):
        if dct[s[i - 1]] >= dct[s[i]]:
            son += dct[s[i]]
        else:
            son += dct[s[i]] - dct[s[i - 1]] * 2 
        i+=1
    return son
print(romanToInt(input("Rim raqamini kiriting: ")))

# 2
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter number: "))
for i in range(len(nums)):
    if (nums[i]+nums[i+1]) == target:
        print(list((i, i+1)))
        break

# 3
num = input("Enter number: ")
print("true" if num == num[-1::-1] else "false")