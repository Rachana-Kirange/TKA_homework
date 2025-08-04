# Creating database of 2021 box office movies 
print("Creating database of 2021 box office movies :- ")
movies_db2021 = {}
name = "Sooryavanshi"
casting = ["Akhay Kumar","Ranveer Singh","Ajay Devgan","Katrina Kaif","Niharica Raizada"]
name1 = "83"
casting1 = ["Ranveer Singh","Deepika Padukone"]
name2 = "Antim: The Final Truth"
casting2 = ["Salman Khan","Aayush Sharma","Mahima Makwana"]
movies_db2021[name] = casting
movies_db2021[name1] = casting1
movies_db2021[name2] = casting2
print(movies_db2021)
print("************--------------------------------**************---------------------------------**************")

# Creating database of 2022 box office movies 
print("Creating database of 2022 box office movies :- ")
movies_db2022 = {}
name1 = "Brahmastra"
casting1 = ["Ranbir Kapoor","Alia Bhatt","Abhitabh Bachhan","Mouni Roy"]
name2 = "Drishyam2"
casting2 = ["Ajay Devgan","Tabu","Akshaye Khanna"]
name3 = "Bhool Bhulaiyaa 2"
casting3 = ["Kartik Aaryan","Kiara Advani","Tabu"]
name4 = "Gangubai Kathiawadi"
casting4 = ["Alia Bhatt","Shantanu Maheshwari"]
movies_db2022[name1] = casting1
movies_db2022[name2] = casting2
movies_db2022[name3] = casting3
movies_db2022[name4] = casting4
print(movies_db2022)
print("************--------------------------------**************---------------------------------**************")

# Creating database of 2023 box office movies 
print("Creating database of 2023 box office movies :- ")
movies_db2023 = {}
name1 = "Jawan"
casting1 = ["Shah Rukh Khan","NayanThara","Deepika Padukone"]
name2 = "Pathaan"
casting2 = ["Shah Rukh Khan","Deepika Padukone","John Abraham"]
name3 = "Animal"
casting3 = ["Ranbir Kapoor","Anil Kapoor","Bobby Deol","Rashmika Mandana"]
name4 = "Gadar 2"
casting4 = ["Sunny Deol","Ameesha Patel","Utkarsh Sharma"]
movies_db2023[name1] = casting1
movies_db2023[name2] = casting2
movies_db2023[name3] = casting3
movies_db2023[name4] = casting4
print(movies_db2023)
print("************--------------------------------**************---------------------------------**************")

# Creating database of 2024 box office movies 
print("Creating database of 2024 box office movies :- ")
movies_db2024 = {}
name1 = "Stree 2"
casting1 = ["Shraddha Kapoor","Rajkumar Rao"]
name2 = "Bhool Bhulaiyaa 3"
casting2 = ["Kartik Aaryan","Vidya Balan","Madhuri Dixit","Tripti Dimri"]
name3 = "Singham Again"
casting3 = ["Ajay Devgan","Kareena Kapoor","Akshay Kumar"]
name4 = "Crew"
casting4 = ["Tabu","Kareena Kapoor","Kriti Sanon"]
movies_db2024[name1] = casting1
movies_db2024[name2] = casting2
movies_db2024[name3] = casting3
movies_db2024[name4] = casting4
print(movies_db2024)
print("************--------------------------------**************---------------------------------**************")

# Creating database of 2025 box office movies 
print("Creating database of 2025 box office movies :- ")
movies_db2025 = {}
name1 = "Housefull5"
casting1 = ["Ritesh Deshmukh","Abhishekh Bachhan","Akshay Kumar","Jacqueline Fernandez","Sonam Bajwa","Kriti Sanon"]
name2 = "Chhaava"
casting2 = ["Vicky Kaushal","Rashmika Mandana"]
name3 = "Sky Force"
casting3 = ["Akshay Kumar","Sara Ali Khan","Nimrit Kaur","Veer Pahariya"]
name4 = "Raid 2"
casting4 = ["Ajay Devgan","Ritesh Deshmukh","Vaani Kapoor"]
movies_db2025[name1] = casting1
movies_db2025[name2] = casting2
movies_db2025[name3] = casting3
movies_db2025[name4] = casting4
print(movies_db2025)
print("************--------------------------------**************---------------------------------**************")

big_db = {2021 : movies_db2021, 2022 : movies_db2022, 2023 : movies_db2023, 2024 : movies_db2024, 2025 : movies_db2025}

for y,m in big_db[2021].items():
    print(y,"----->",m)

print("************--------------------------------**************---------------------------------**************")
year_input = eval(input("Enter the year between 2021 - 2025 :-"))
for i in big_db:
    if i == year_input:
        for m in big_db[i]:
            print()
            print(m ,":")
            for c in range(len(big_db[i][m])):    
                print(big_db[i][m][c])

print("************--------------------------------**************---------------------------------**************")
year_input = eval(input("Enter the year between 2021 - 2025 :-"))
print("Actor who appears in most Movies of ",year_input,"is = ")
a = {}
actor_movies = {}
for movie in big_db[year_input]:
    for actor in big_db[year_input][movie]:
        if actor in a:
            a[actor] += 1
            actor_movies[actor].append(movie)
        else :
            a[actor] = 1
            actor_movies[actor] = [movie]
max_actor = ""
max_count = 0

for name in a:
    if a[name] > max_count:
        max_actor = name
        max_count = a[name]

print(max_actor)
print(max_count,"Movies in one year")
print("Movies are :- ")
for i in actor_movies[max_actor]:
    print("---",i)

print("************--------------------------------**************---------------------------------**************")

y = int(input("Enter year: "))
count = {}
actor_movies = {}
for movie in big_db[y]:
    for actor in big_db[y][movie]:
        found = False
        for a in count:
            if a == actor:
                count[a] = count[a] + 1
                actor_movies[a].append(movie)
                found = True
                break
        if not found:
            count[actor] = 1
            actor_movies[actor] = [movie]

max_count = 0
for actor in count:
    if count[actor] > max_count:
        max_count = count[actor]

print("Most movies in", y, ":")
for actor in count:
    if count[actor] == max_count:
        print(actor, "-", max_count)
        print("Movies are :- ")
        for i in actor_movies[actor]:
            print("---",i)
print()

print("************--------------------------------**************---------------------------------**************")

actor_name = input("Enter actor name: ")

for year in big_db:
    for movie in big_db[year]:
        cast = big_db[year][movie]
        for i in range(0, len(cast)):
            matched = True
            if len(actor_name) != len(cast[i]):
                matched = False
            else:
                for j in range(0, len(actor_name)):
                    if actor_name[j] != cast[i][j]:
                        matched = False
                        break
            if matched:
                print("Movie:", movie, "  Year:", year)
                break

print("************--------------------------------**************---------------------------------**************")

count = {}
actor_movies = {}

# Step 1: Count and track movies for each actor
for year in big_db:
    for movie in big_db[year]:
        for actor in big_db[year][movie]:
            found = False
            for a in count:
                if a == actor:
                    count[a] += 1
                    actor_movies[a].append(movie)
                    found = True
                    break
            if not found:
                count[actor] = 1
                actor_movies[actor] = [movie]

# Step 2: Find max movie count
max_count = 0
for actor in count:
    if count[actor] > max_count:
        max_count = count[actor]

# Step 3: Print top actor(s) and their movies
print("Actor who appeared in most movies in last 5 years :")
for actor in count:
    if count[actor] == max_count:
        print(actor, "-", max_count, "Movies")
        print("Movies:")
        for m in actor_movies[actor]:
            print(m)
        print("\n")

print("************--------------------------------**************---------------------------------**************")