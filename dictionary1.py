# 1) Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!


 places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
 places ['Brazil'] = 2016

 # 2)  We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this.


medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
for akey in medal_events.keys():
        events = list(medal_events.keys())
              
