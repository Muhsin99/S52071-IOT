#!/usr/bin/env python
# coding: utf-8

# In[2]:


def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
    
if __name__ == '__main__':
    dec_val = 30
    
    DecimalToBinary(dec_val)


# In[15]:


import string

def find_max_letter_count(word):

    alphabet = string.ascii_lowercase
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in word:
        dictionary[letters] += 1

    dictionary = sorted(dictionary.items(), 
                        reverse=True, 
                        key=lambda x: x[1])

    for position in range(0, 26):
        print (dictionary[position])
        if position != len(dictionary) - 1:
            if dictionary[position + 1][1] < dictionary[position][1]:
                break

find_max_letter_count("ihaveapenihaveaapple")


# In[17]:


try_string = "Hi saya belajar python 3"
print ("The original string is : " + try_string)
res = len(try_string.split())
print ("The number of words are : " + str(res))


# In[18]:


x = 10
a = 3
b = 4

def multiply_by_two(x):
    return x*2
    
def add_numbers(a,b):
    return a+b
    
augmented = {x:10,a:3,b:4}

print (multiply_by_two(10))
print ("Arguments are:" +str(x))
print (add_numbers(3,4))
print ("Arguments are: "+str(a)+", "+str(b))


# In[ ]:




