
vowels = 'aeiou'

str = input("Enter the String:")

str = str.casefold()

count = {}.fromkeys(vowels,0)

for char in str:
   if char in count:
       count[char] += 1
print("vowels in sentences : vowel repetion\n",count)