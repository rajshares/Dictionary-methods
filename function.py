## 1) Write a function named same that takes a string as input, and simply returns that string.

def same (string):
    return string
    
## 2) Write a function called same_thing that returns the parameter, unchanged.

def same_thing(a):
    return a

## 3) Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.

def subtract_three (a):
    return a-3
    
## 4) Write a function called change that takes one number as its input and returns that number, plus 7.

def change(a):
    return a+7

## 5) Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.

def s_change(a):
     return a + " for fun."

##6) Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.

def decision(s1):
    if len(s1) > 17:
        return ("This is a long string")
    else:
        return ("This is a short string")
    

##7) Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”

def intro(str1):
    return("Hello, my name is "+ str1+ " and I love SI 106.")

intro("Becky") #calling the function named intro
               #and passing the parameter Becky
