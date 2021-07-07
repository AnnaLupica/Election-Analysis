
#Creating list
counties=["Arapahoe", "Denver", "Jefferson"]
print(counties[2])

for county in counties
    print(county)

#Insert new item in list
counties.append("El Paso")
counties.insert(2,"El Paso")

#Remove item from list
counties.remove("El Paso")
counties.pop(3)
print(counties)

#Change item in list
counties[2]="El Paso"
print(counties)

#Mod list
counties[2]="Jefferson"
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties[2]="Denver"
counties[1]="Jefferson"
counties.append("Arapahoe")
print(counties)

#Tuples
counties_tuple=("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
counties_tuple[1]

#List of Dictionaries
voting_data=[]
voting_data.append=({"county":"Arapahoe","registered_voters":422839})
voting_data.append=({"county":"Denver","registered_voters":463353})
voting_data.append=({"county":"Jefferson","registered_voters":432438})
print(voting_data)
for county in counties_dict.keys():
    print(county)

#How many votes did you get?
my_votes=int(input("How many votes did you get in the election?"))

#Total votes in teh election
total_votes=int(input("What is the total votes in the election?"))

#Calculate the percentage of votes you've received
percentage_votes=(my_votes/total_votes)*100
print("I received"+str(percentage_votes)+"% of the total votes")

score = int(input("What is your test score?"))

if score >= 90:
    print('Your grade is an A')
elif score >= 80:
    print('Your grade is a B')
elif score >= 70:
    print('Your grade is a C')
elif score >= 60:
    print('Your grade is a D')
else:
    print('Your grade is an F')
    
    
