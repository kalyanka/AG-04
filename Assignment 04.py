
# coding: utf-8

# ## Assignment 04
# 
# ### Problem Statement 01
# 
# Write a Python Program(with class concepts) to find the area of the triangle using the belowformula.
# 
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# 
# Function to take the length of the sides of triangle from user should be defined in the parentclass and function to calculate the area should be defined in subclass.

# In[1]:


class TriangleBase:
    def __init__(self, a, b, c, s):
        self.a = a
        self.b = b
        self.c = c
        self.s = s

class Triangle(TriangleBase):
    def getArea(self):
        return (self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)) ** 0.5

t = Triangle(1, 2, 3, 4)
print(t.getArea())


# ### Problem Statement 02
# Write a function filter_long_words() that takes a list of words and an integer n and returnsthe list of words that are longer than n.

# In[2]:


def  filter_long_word(words, n):
    return filter(lambda word: len(word) > n, words)

list(filter_long_word(['AB', 'BC', 'CD'], 1))


# ### Problem Statement 03:
# 
# Write a Python program using function concept that maps  list of words into a list of integersrepresenting the lengths of the corresponding words.
# 
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]Here 2,3 and 4 are the lengths of the words in the list.

# In[3]:


def wordLengths(words):
    return map(lambda word: len(word), words)

list(wordLengths(['A', 'AB', 'ABC']))


# ### Problem Statement 04:
# 
# Write a Python function which takes a character (i.e. a string of length 1) and returns True ifit is a vowel, False otherwise.

# In[4]:


def isVowel(c):
    try:
        "aeiou".index(c)
        return True
    except:
        pass

    return False

print(isVowel('a'))
print(isVowel('z'))

