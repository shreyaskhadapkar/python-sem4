# Written by Shreyas Khadapkar      
string = input('Enter the string : ')
# print(len(string))
string = string.lower()
vowels,cons = 0,0
# print(vowels,cons)
# print(string)
for i in range(len(string)):
    if(string[i].isalpha()):
        # print('hi')
        if(string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'):
            vowels+=1
        else:
            cons+=1
    # else:
    #     print('else')
print('The input string contains {} vowels and {} consonants'.format(vowels,cons))