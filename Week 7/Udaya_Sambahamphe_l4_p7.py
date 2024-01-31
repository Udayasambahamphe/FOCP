#1
def get_unique_letters(s):
    return sorted(set(s.lower() for s in s if s.isalpha()))
print(get_unique_letters('cheese')) 
print(get_unique_letters('PythonProgramming')) 
print(get_unique_letters('HelloWorld')) 
print(get_unique_letters('Able was I ere I saw Elba')) 


#2
def union_letters(word1, word2):
    
    return sorted(set(word1) | set(word2))

def intersection_letters(word1, word2):
    
    return sorted(set(word1) & set(word2))

def sym_difference_letters(word1, word2):
    
    return sorted(set(word1) ^ set(word2))
print(union_letters("prasi","josi"))  
print(intersection_letters('Hello', 'duniya'))
print(sym_difference_letters('sun', 'shine'))  


#3
dict_of_capitals = {'Nepal': 'Kathmandu', 'India': 'Delhi', 'United Kingdom': 'London'}

while True:
    country = input("Country name: ").title()
    if country in dict_of_capitals:
        print("The capital city of", country, "is",dict_of_capitals[country])
    else:
        capital = input("We don't know the capital city. Please enter it: ")
        dict_of_capitals[country] = capital