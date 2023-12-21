first_word=input("Enter first word\n")
second_word=input("Enter second word\n")
list_1=list(first_word)
list_2=list(second_word)
list_1.sort()
list_2.sort()
if list_1==list_2:
    print("Given strings are anagrams")
else :
    print("Given strings are not anagrams")

