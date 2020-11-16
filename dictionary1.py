# 1) Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!


 places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
 places ['Brazil'] = 2016

 # 2)  We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this.


medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
for akey in medal_events.keys():
        events = list(medal_events.keys())
              
# 3  Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
words = sentence.split()
word_counts = {} 
for word in words:
      if word not in word_counts:
            word_counts[word] = 0
      word_counts[word] = word_counts[word] + 1
print(word_counts)
   
# 4 Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "what can I do"
char_d = {}
for c in stri:
    if c not in char_d:
        char_d[c] = 0 
    char_d[c] = char_d[c] + 1

    
