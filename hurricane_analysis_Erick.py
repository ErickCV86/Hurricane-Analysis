# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#print(len(deaths))

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def convert_damages_data(damages):
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    elif damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    elif damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages_data(damages)
# test function by updating damages
#print(convert_damages_data(damages))

#1.1
def convert_damages_data_2(damages):
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(0.)
    elif damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    elif damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages2 = convert_damages_data_2(damages)
# test function by updating damages
#print(convert_damages_data(damages))


# 2 
# Create a Table
def hurricanes(names, months, years,max_sustained_winds, areas_affected, damages, deaths):
  lista = []

  for i in range(len(names)):
    diccionario = {}
    diccionario.update({"Name": names[i] , "Month": months[i], "Year": years[i] , "Max Sustained Wind": max_sustained_winds[i] ,"Areas Affected": areas_affected[i] , "Damage": damages[i],"Deaths": deaths[i] })
    lista.append(diccionario)
  
  huracanes = {key:value for key, value in zip(names, lista)}
  return huracanes

# Create and view the hurricanes dictionary
hurricanes = hurricanes(names, months, years,max_sustained_winds, areas_affected, damages, deaths) 
# print(hurricanes)

#2.1
def hurricanes_2(names, months, years,max_sustained_winds, areas_affected, updated_damages2, deaths):
  lista = []

  for i in range(len(names)):
    diccionario = {}
    diccionario.update({"Name": names[i] , "Month": months[i], "Year": years[i] , "Max Sustained Wind": max_sustained_winds[i] ,"Areas Affected": areas_affected[i] , "Damage": updated_damages2[i],"Deaths": deaths[i] })
    lista.append(diccionario)
  
  huracanes = {key:value for key, value in zip(names, lista)}
  return huracanes

# Create and view the hurricanes dictionary
hurricanes2 = hurricanes_2(names, months, years,max_sustained_winds, areas_affected, updated_damages2, deaths) 
# print(hurricanes2)


# 3
# Organizing by Year
def hurricane_by_year_dictionary(hurricanes):
  sorted_years = sorted(years)
  unique_sorted_years = [sorted_years[0]]

  for i in range(1, len(sorted_years)):
    if sorted_years[i-1] < sorted_years[i]:
      unique_sorted_years.append(sorted_years[i])

  lista = []
  for unique_sorted_year in unique_sorted_years:
    sublista = []
    for datos in hurricanes.values():
      if datos["Year"] == unique_sorted_year:
        sublista.append(datos)
    lista.append(sublista)
  
  return {key:value for key, value in zip(unique_sorted_years, lista)}

# create a new dictionary of hurricanes with year and key
#print(hurricane_by_year_dictionary(hurricanes))

#3.1 
def hurricane_by_year_dictionary2(hurricanes2):
  new_dict = {}
  for hurricane in hurricanes2:
    # current_year.append(hurricanes2[hurricane]['Year'])
    # current_cane.append(hurricanes2[hurricane])
    current_year = hurricanes2[hurricane]['Year']
    current_cane = hurricanes2[hurricane]
    
    if current_year in new_dict:
      new_dict[current_year].append(current_cane)
    else: 
      new_dict[current_year] = [current_cane]
  return new_dict

#print(hurricane_by_year_dictionary2(hurricanes2))

# 4
# Counting Damaged Areas
# areas_affected : cantidad de veces que fueron afectadas

def counting_damaged_areas(hurricanes):
  lista = []
  for datos in hurricanes.values():
    lista.append(datos["Areas Affected"])

  nueva_lista = [] 
  for i in range(len(lista)):
    for j in range(len(lista[i])):
      nueva_lista.append(lista[i][j])
  
  sorted_list = sorted(nueva_lista)
  unique_list_element = [sorted_list[0]]

  for i in range(1,len(sorted_list)):
    if sorted_list[i-1] < sorted_list[i]:
      unique_list_element.append(sorted_list[i])
  
  counter = []
  for elemento1 in unique_list_element:
    counter.append(sorted_list.count(elemento1))
        
  return {key:value for key, value in zip(unique_list_element,counter)}

# create dictionary of areas to store the number of hurricanes involved in
affected_area = counting_damaged_areas(hurricanes)
# print(affected_area)

#4.1
def counting_damaged_areas2(hurricanes2):
  new_dictionary = {}

  for hurricane in hurricanes2:
    for area in hurricanes2[hurricane]['Areas Affected']:
      if area in new_dictionary:
        new_dictionary[area] += 1
      else:
        new_dictionary[area] = 1
  return new_dictionary

affected_areas = counting_damaged_areas2(hurricanes2)
#print(affected_areas)

# 5 
# Calculating Maximum Hurricane Count
def maximun_hurricane_count(affected_area):
  counters = []
  for elemento in affected_area.values():
    counters.append(elemento)
  
  sorted_list = sorted(counters)
  unique_list_element = [sorted_list[0]]

  for i in range(1,len(sorted_list)):
    if sorted_list[i-1] < sorted_list[i]:
      unique_list_element.append(sorted_list[i])
  maximo = max(unique_list_element)
  
  
  for key, value in affected_area.items():
    if value == maximo:
      print(key + ":", value)
  
# find most frequently affected area and the number of hurricanes involved in
#maximun_hurricane_count(affected_area)

#5.1
def maximun_hurricane_count2(affected_areas):
  max_area = 'Central America'
  max_area_count = 0

  for affected_area in affected_areas:
    if affected_areas[affected_area] > max_area_count:
      max_area = affected_area
      max_area_count = affected_areas[affected_area]
  print(max_area + ":", max_area_count)

#maximun_hurricane_count2(affected_areas)

# 6
# Calculating the Deadliest Hurricane

def greatest_number_of_deaths(hurricane):
  deaths = []

  for values1 in hurricane.values():
    deaths.append(values1['Deaths'])
  maximum_deaths = max(deaths)
  
  lista = []
  for values1 in hurricane.values():
    if values1['Deaths'] == maximum_deaths:
      lista.append(values1['Name'])
  
  for elemento in lista:
    print(elemento + ":",maximum_deaths)

# find highest mortality hurricane and the number of deaths
#greatest_number_of_deaths(hurricanes)

#6.1 
def greatest_number_of_deaths2(hurricanes2):
  max_mortality_cane = 'Cuba I'
  max_mortality = 0

  for hurricane in hurricanes2:
    if hurricanes2[hurricane]['Deaths'] > max_mortality:
      max_mortality_cane = hurricanes2[hurricane]['Name']
      max_mortality = hurricanes2[hurricane]['Deaths']
  print(max_mortality_cane + ":",max_mortality)

#greatest_number_of_deaths2(hurricanes2)

# 7
# Rating Hurricanes by Mortality
# key, value mortality rating, (list)

def rating_hurricanes_by_mortality(hurricanes):
  mortality_scale = { 0: 0, 
                      1:100,
                      2:500,
                      3: 1000,
                      4: 10000}
  mortality_rate = []
  for key in mortality_scale.keys():
    mortality_rate.append(key)
  mortality_rate.append(5)
  

  ratings = [] 
  names_rated = []  
  for key1, values1 in hurricanes.items():
    if values1['Deaths'] == 0:
     x, y = mortality_rate[0], values1
    elif 0 < values1['Deaths'] and values1['Deaths'] <= 100:
      x, y  = mortality_rate[1], values1
    elif 100 < values1['Deaths'] and values1['Deaths'] <= 500:
      x, y = mortality_rate[2], values1
    elif 500 < values1['Deaths'] and values1['Deaths'] <= 1000:
      x, y = mortality_rate[3], values1
    elif 1000 < values1['Deaths'] and values1['Deaths'] <= 10000:
      x, y = mortality_rate[4], values1
    elif 10000 < values1['Deaths']:
      x, y = 5, values1
    ratings.append(x)
    names_rated.append(y)

  
  lista = []
  for element1 in mortality_rate:
    sublista = []
    for element2, element3 in zip(ratings, names_rated):
      if element1 == element2:
        sublista.append(element3)
    lista.append(sublista)

  # print(len(mortality_rate))
  # print(len(lista))
  return {key: value for key, value in zip(mortality_rate, lista)}

# categorize hurricanes in new dictionary with mortality severity as key

#print(rating_hurricanes_by_mortality(hurricanes))


#7.1 
def rating_hurricanes_by_mortality2(hurricanes2):
  hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

  for hurricane in hurricanes2:
    if hurricanes2[hurricane]['Deaths'] == 0:
       hurricanes_by_mortality[0].append(hurricanes2[hurricane])
    elif 0 < hurricanes2[hurricane]['Deaths'] and hurricanes2[hurricane]['Deaths'] <= 100:
       hurricanes_by_mortality[1].append(hurricanes2[hurricane])
    elif 100 < hurricanes2[hurricane]['Deaths'] and hurricanes2[hurricane]['Deaths'] <= 500:
       hurricanes_by_mortality[2].append(hurricanes2[hurricane])
    elif 500 < hurricanes2[hurricane]['Deaths'] and hurricanes2[hurricane]['Deaths'] <= 1000:
       hurricanes_by_mortality[3].append(hurricanes2[hurricane])
    elif 1000 < hurricanes2[hurricane]['Deaths'] and hurricanes2[hurricane]['Deaths'] <= 10000:
       hurricanes_by_mortality[4].append(hurricanes2[hurricane])
    else:
        hurricanes_by_mortality[5].append(hurricanes2[hurricane])

  return hurricanes_by_mortality

#print(rating_hurricanes_by_mortality2(hurricanes2))


# 8 Calculating Hurricane Maximum Damage
def hurricane_maximum_damage(hurricanes):
  lista = []
  for key1, dict1 in hurricanes.items():
    for key2 in dict1.keys():
      if key2 == 'Damage':
        if dict1['Damage'] == 'Damages not recorded':
          lista.append('0M')
        else:
          lista.append(dict1['Damage'])
  updated_damage = convert_damages_data(lista)
  index_maximum_damage = updated_damage.index(max(updated_damage))

  hurricane_names = []
  for key1 in hurricanes.keys():
    hurricane_names.append(key1)
  a = hurricane_names[index_maximum_damage]

  print(a + ":", max(updated_damage))

# find highest damage inducing hurricane and its total cost
#hurricane_maximum_damage(hurricanes)

#8.1 
def hurricane_maximum_damage2(hurricanes2):
  max_damage_cane = 'Cuba I'
  max_damage = 0

  for hurricane in hurricanes2:
    if hurricanes2[hurricane]['Damage'] > max_damage:
      max_damage_cane = hurricanes2[hurricane]['Name']
      max_damage = hurricanes2[hurricane]['Damage']
  print(max_damage_cane + ":", max_damage)

#hurricane_maximum_damage2(hurricanes2)


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating(hurricanes2):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  
  damage_rate = []
  for key in damage_scale.keys():
    damage_rate.append(key)
  damage_rate.append(5)
   
  ratings = [] 
  names_rated = []  
  for key1, values1 in hurricanes2.items():
    if values1['Damage'] == 0:
     x, y = damage_rate[0], values1
    elif 0 < values1['Damage'] and values1['Damage'] <= 100000000:
      x, y  = damage_rate[1], values1
    elif 100000000 < values1['Damage'] and values1['Damage'] <= 1000000000:
      x, y = damage_rate[2], values1
    elif 1000000000 < values1['Damage'] and values1['Damage'] <= 10000000000:
      x, y = damage_rate[3], values1
    elif 10000000000 < values1['Damage'] and values1['Damage'] <= 50000000000:
      x, y = damage_rate[4], values1
    elif 50000000000 < values1['Damage']:
      x, y = 5, values1
    ratings.append(x)
    names_rated.append(y)

  
  lista = []
  for element1 in damage_rate:
    sublista = []
    for element2, element3 in zip(ratings, names_rated):
      if element1 == element2:
        sublista.append(element3)
    lista.append(sublista)

  return {key: value for key, value in zip(damage_rate, lista)}

#print(damage_rating(hurricanes2))

#9.2
def damage_rating2(hurricanes2):
  hurricanes_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

  for hurricane in hurricanes2:
    if hurricanes2[hurricane]['Damage'] == 0:
      hurricanes_by_damage[0].append(hurricanes2[hurricane])
    elif 0 < hurricanes2[hurricane]['Damage'] and hurricanes2[hurricane]['Damage'] <= 100000000:
      hurricanes_by_damage[1].append(hurricanes2[hurricane])
    elif 100000000 < hurricanes2[hurricane]['Damage'] and hurricanes2[hurricane]['Damage'] <= 1000000000:
      hurricanes_by_damage[2].append(hurricanes2[hurricane])
    elif 1000000000 < hurricanes2[hurricane]['Damage'] and hurricanes2[hurricane]['Damage'] <= 10000000000:
      hurricanes_by_damage[3].append(hurricanes2[hurricane])
    elif 10000000000 < hurricanes2[hurricane]['Damage'] and hurricanes2[hurricane]['Damage'] <= 50000000000:
      hurricanes_by_damage[4].append(hurricanes2[hurricane])
    else:
        hurricanes_by_damage[5].append(hurricanes2[hurricane])
  return hurricanes_by_damage

print(damage_rating2(hurricanes2))    