s = input("Input the sentence\n").upper()  #Get the input from the user then converting it to uppercase
v = ['A','E','I','O','U']  
r = []                                     #Creating two empty list to store and display the result
k = []
for i in v:
    if i in s:
        r.append(i)                                                           #If a vowel is present,then append it in list 'r'
        k.append(s.count(i))                                                  #Appending the count of that vowel
print("Vowels in sentence -",r,"\nEach vowel is repeated as -",k)             #Display the output
        
