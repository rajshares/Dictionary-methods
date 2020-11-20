#1 Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []
for list in lst_tups:
      t_check.append(list[2])
print(t_check)

#2 Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = []
for list in tups:
      seconds.append(list[1])
print(seconds)

#  Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”

olympics=('Beijing','London','Rio','Tokyo')

#   The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country. 

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country=[]
for i in tuples_lst:
    country.append(i[1])
    
#  With only one line of code, assign the variables city, country, and year to the values of the tuple olymp. 

olymp = ('Rio', 'Brazil', 2016)
city=olymp[0]
country=olymp[1]   
year=olymp[2]
#  Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order. 

def info(name,gender,age,bday_month,hometown):
    f=(name,gender,age,bday_month,hometown)
    return f
info('sanjay','male',23,10,'bhopal')


#  Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method. 

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for i in gold.items():
    num_medals.append(i[1])
 
 
