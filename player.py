class player:
    def __init__(self,j, n, r, w, t):
        self.__jerceyno = j
        self.__name = n 
        self.__run = r
        self.__wicket = w
        self.__teamname = t
    def getjercey_no(self):
        return self.__jerceyno
    def setjercey_no(self, jercey_no):
        return self.__jerceyno == jercey_no
    def getname(self):
        return self.__name
    def setname(self, name):
        return self.__name == name
    def getrun(self):
        return self.__run
    def setrun(self, run):
        return self.__run == run
    def getwicket(self):
        return self.__wicket
    def setwicket(self, wicket):
        return self.__wicket == wicket
    def getteamname(self):
        return self.__jerceyno
    def setteamname(self, teamname):
        return self.__teamname == teamname
    def display_info(self):
        print(f"Jersey No: {self.__jerceyno}, Name: {self.__name}, Runs: {self.__run}, Wickets: {self.__wicket}, Team: {self.__teamname}")
    
    @staticmethod
    def display_team_info(Team):
        team_name = input("Enter team name to view players (MI / RCB / SRH / CSK) or 'ALL' for all teams: ").strip().upper()
        
        if team_name == "ALL":
            for name, team_list in Team.items():
                print(f"\n{name} Team Players:")
                for p in team_list:
                    p.display_info()
        elif team_name in Team:
            print(f"\n{team_name} Team Players:")
            for p in Team[team_name]:
                p.display_info()
        else:
            print("Invalid team name.")

    @staticmethod
    def best_bowler(Team):
        Team_Name = input("Enter team name (MI / RCB / SRH / CSK) or 'ALL' for all teams: ").strip().upper()

        if Team_Name == "ALL":
            # Combine all players into one list
            all_players = []
            for team in Team.values():
                all_players.extend(team)
            best_bowler = max(all_players, key=lambda p: p.getwicket())
            print("\nBest Bowler Across All Teams:")
            best_bowler.display_info()

        elif Team_Name in Team:
            best_bowler = max(Team[Team_Name], key=lambda p: p.getwicket())
            print(f"\nBest Bowler in {Team_Name}:")
            best_bowler.display_info()

        else:
            print("Invalid team name.")

    @staticmethod
    def best_batsman(Team):
        Team_Name = input("Enter team name (MI / RCB / SRH / CSK) or 'ALL' for all teams: ").strip().upper()
        if Team_Name == "ALL":
            all_players = []
            for team in Team.values():
                all_players.extend(team)
            best_batsman = max(all_players, key=lambda p: p.getrun())
            print("\nBest Batsman Across All Teams:")
            best_batsman.display_info()
        elif Team_Name in Team:
            best_batsman = max(Team[Team_Name], key=lambda p: p.getrun())
            print(f"\nBest Batsman in {Team_Name}:")
            best_batsman.display_info()
        else:
            print("Invalid team name.")

    @staticmethod
    def all_rounder(Team):
        Team_Name = input("Enter team name (MI / RCB / SRH / CSK) or 'ALL' for all teams: ").strip().upper()

        if Team_Name == "ALL":
            all_players = []
            for team in Team.values():
                all_players.extend(team)
            best_all_rounder = max(all_players, key=lambda p: p.getrun() + p.getwicket() * 20)
            print("\nBest All-Rounder Across All Teams:")
            best_all_rounder.display_info()
        elif Team_Name in Team:
            best_all_rounder = max(Team[Team_Name], key=lambda p: p.getrun() + p.getwicket() * 20)
            print(f"\nBest All-Rounder in {Team_Name}:")
            best_all_rounder.display_info()
        else:
            print("Invalid team name.")

MI_Team = []
# print("MI Team Players Information :-")
p = player(45, "Rohit Sharma", 6500, 29, "MI")
MI_Team.append(p)
p1 = player(99, "Jasprit Bumrah", 200, 110, "MI")
MI_Team.append(p1)
p2 = player(1, "Ishan Kishan", 2200, 0, "MI")
MI_Team.append(p2)
p3 = player(55, "Suryakumar Yadav", 3000, 2, "MI")
MI_Team.append(p3)
p4 = player(93, "Tilak Varma", 950, 1, "MI")
MI_Team.append(p4)
p5 = player(36, "Tim David", 800, 0, "MI")
MI_Team.append(p5)
p6 = player(21, "Cameron Green", 1000, 25, "MI")
MI_Team.append(p6)
p7 = player(7, "Piyush Chawla", 500, 90, "MI")
MI_Team.append(p7)
p8 = player(17, "Jofra Archer", 250, 75, "MI")
MI_Team.append(p8)
p9 = player(6, "Arjun Tendulkar ", 100, 10, "MI")
MI_Team.append(p9)
p10 = player(11, "Nehal Wadhera", 450, 0, "MI")
MI_Team.append(p10)

RCB_Team = []
# print("RCB Team Players Information :-")
p11 = player(18, "Virat Kohli", 7300, 5, "RCB")
RCB_Team.append(p11)
p12 = player(17, "Faf Du Plessis", 4200, 0, "RCB")
RCB_Team.append(p12)
p13 = player(1, "Glenn Maxwell", 2800, 35, "RCB")
RCB_Team.append(p13)
p14 = player(10, "Dinesh karthik", 4000, 0, "RCB")
RCB_Team.append(p14)
p15 = player(19, "Harshal Patel", 250, 95, "RCB")
RCB_Team.append(p15)
p16 = player(11, "Mohammed Siraj", 150, 60, "RCB")
RCB_Team.append(p16)
p17 = player(15, "Wanindu Hasaranga", 350, 70, "RCB")
RCB_Team.append(p17)
p18 = player(2, "Mahipal Lomror", 600, 5, "RCB")
RCB_Team.append(p18)
p19 = player(5, "Suyash Prabhudessai", 450, 2, "RCB")
RCB_Team.append(p19)
p20 = player(33, "Karn Sharma", 300, 50, "RCB")
RCB_Team.append(p20)
p21 = player(12, "Anuj Rawat", 750, 1, "RCB")
RCB_Team.append(p21)

SRH_Team = []
# print("SRH Team Players Information :-")
p22 = player(1, "Abhishekh Sharma", 1300, 5, "SRH")
SRH_Team.append(p22)
p23 = player(3, "Rahul Tripathi", 1700, 0, "SRH")
SRH_Team.append(p23)
p24 = player(11, "Aiden Markram", 1200, 10, "SRH")
SRH_Team.append(p24)
p25 = player(29, "Heinrich Klaasen", 950, 0, "SRH")
SRH_Team.append(p25)
p26 = player(5, "Mayank Agarwal", 2300, 1, "SRH")
SRH_Team.append(p26)
p27 = player(33, "Washington Sundar", 850, 30, "SRH")
SRH_Team.append(p27)
p28 = player(15, "Marco Jansen", 400, 35, "SRH")
SRH_Team.append(p28)
p29 = player(14, "Bhuvneshwar Kumar", 300, 140, "SRH")
SRH_Team.append(p29)
p30 = player(12, "t Natrajan", 150, 45, "SRH")
SRH_Team.append(p30)
p31 = player(91, "Umran Malik", 100, 35, "SRH")
SRH_Team.append(p31)
p32 = player(6, "Glenn Phillips", 600, 2, "SRH")
SRH_Team.append(p32)

CSK_Team = []
# print("CSK Team Player Information :-")
p33 = player(7, "MS Dhoni", 5000, 1, "CSK")
CSK_Team.append(p33)
p34 = player(12, "Ravindra Jadeja", 2500, 85, "CSK")
CSK_Team.append(p34)
p35 = player(3, "Ruturaj Gaikwad", 2200, 0, "CSK")
CSK_Team.append(p35)
p36 = player(11, "Moeen Ali", 1800, 35, "CSK")
CSK_Team.append(p36)
p37 = player(99, "Deepak Chahar", 400, 60, "CSK")
CSK_Team.append(p37)
p38 = player(45, "Devon Conway", 1300, 0, "CSK")
CSK_Team.append(p38)
p39 = player(13, "Ambati Rayudu", 4200, 2, "CSK")
CSK_Team.append(p39)
p40 = player(27, "Ben Stokes", 1500, 40, "CSK")
CSK_Team.append(p40)
p41 = player(8, "Matheesha Pathirana", 100, 30, "CSK")
CSK_Team.append(p41)
p42 = player(22, "Shivam Dube", 1200, 10, "CSK")
CSK_Team.append(p42)
p43 = player(28, "Tushar Deshpande", 80, 20, "CSK")
CSK_Team.append(p43)

All_Team = {"MI" : MI_Team,
            "RCB" : RCB_Team,
            "SRH" : SRH_Team,
            "CSK" : CSK_Team}

print()
print("The team information :-")
p.display_team_info(All_Team)
print("For the best bowler :-")
p.best_bowler(All_Team)
print("For the best batsman :-")
p.best_batsman(All_Team)
print("For All rounder :-")
p.all_rounder(All_Team)