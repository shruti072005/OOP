class Player:
    def __init__(self, name, jersey_no, runs, wickets, team_name):
        self._name = name
        self._jersey_no = jersey_no
        self._runs = runs
        self._wickets = wickets
        self._team_name = team_name

    # Getter methods
    def get_name(self):
        return self._name

    def get_jersey_no(self):
        return self._jersey_no

    def get_runs(self):
        return self._runs

    def get_wickets(self):
        return self._wickets

    def get_team_name(self):
        return self._team_name

    # Setter methods
    def set_runs(self, runs):
        self._runs = runs

    def set_wickets(self, wickets):
        self._wickets = wickets

    def set_team_name(self, team_name):
        self._team_name = team_name

    def get_all_info(self):
        return f"Name: {self._name}, Jersey No: {self._jersey_no}, Runs: {self._runs}, Wickets: {self._wickets}, Team: {self._team_name}"


# Creating list of teams
teamRCB = []
teamMI = []
teamCSK = []

P1=Player("Virat Kohli",18, 7900, 5, "RCB")
P2=Player( "Glenn Maxwell",5, 2800, 54, "RCB")
P3=Player( "Faf du Plessis",97, 4500, 36, "RCB")
P4=Player( "Dinesh Karthik",19, 4516, 42, "RCB")
P5=Player( "Rajat Patidar",15, 861, 52, "RCB")
P6=Player("Cameron Green",6,  500, 52, "RCB")
P7=Player( "phil salt",28, 1056, 0, "RCB")
P8=Player( "Mohammed Siraj",10, 52, 78, "RCB")
P9=Player( "Mayank Dagar",54, 72, 53, "RCB")
P10=Player( "Yash Dayal",31, 15, 51, "RCB")
P11=Player( "Anuj Rawat",13, 393, 57, "RCB")

P12=Player("rohit sharma",45,6628,15,"MI")
P13=Player("hardik pandya",33,2749,78,"MI")
P14=Player("suryakumar yadav",63,4311,0,"MI")
P15=Player("tilak varma",9,1499,0,"MI")
P16=Player("naman dhir",31,392,51,"MI")
P17=Player("mitchell santner",74,110,55,"MI")
P18=Player("jasprit bumrah",93,69,183,"MI")
P19=Player("trent boult",18,85,143,"MI")
P20=Player("karn sharma",33,351,83,"MI")
P21=Player("deepak chahar",90,117,88,"MI")
P22=Player("ashwani kumar",42,0,11,"MI")

P23=Player("Ruturaj Gaikwad",9,  1797, 33, "CSK")
P24=Player( "MS Dhoni",7, 5243, 25, "CSK")
P25=Player("Ravindra Jadeja",8,  2692, 152, "CSK")
P26=Player("Ajinkya Rahane",44,  4433, 19, "CSK")
P27=Player( "Matheesha Pathirana",90, 20, 55, "CSK")
P28=Player( "Shivam Dube",33, 1521, 4, "CSK")
P29=Player( "Moeen Ali",5, 1130, 33, "CSK")
P30=Player( "Devon conway",88, 1080, 0, "CSK")
P31=Player( "Tushar Deshpande",19, 12, 52, "CSK")
P32=Player( "Maheesh Theekshana",20, 25, 56, "CSK")
P33=Player( "Ben Stokes",21, 935, 58, "CSK")

teamRCB.append(P1)
teamRCB.append(P2)
teamRCB.append(P3)
teamRCB.append(P4)
teamRCB.append(P5)
teamRCB.append(P6)
teamRCB.append(P7)
teamRCB.append(P8)
teamRCB.append(P9)
teamRCB.append(P10)
teamRCB.append(P11)

teamMI.append(P12)
teamMI.append(P13)
teamMI.append(P14)
teamMI.append(P15)
teamMI.append(P16)
teamMI.append(P17)
teamMI.append(P18)
teamMI.append(P19)
teamMI.append(P20)
teamMI.append(P21)
teamMI.append(P22)

teamCSK.append(P23)
teamCSK.append(P24)
teamCSK.append(P25)
teamCSK.append(P26)
teamCSK.append(P27)
teamCSK.append(P28)
teamCSK.append(P29)
teamCSK.append(P30)
teamCSK.append(P31)
teamCSK.append(P32)
teamCSK.append(P33)

# Function to get info of a particular player by name
def show_player_RCB(player_name, info_type="all"):
    for player in teamRCB:
        if player.get_name().lower() == player_name.lower():
                print(player.get_all_info())

                if player.get_runs()>1000 and player.get_wickets()> 50:
                    print("Player is all rounder")

                elif player.get_runs()>1000:
                 print("Player is batsman")
                
                elif player.get_wickets()>50:
                 print("Player is bowler")

                else:    
                    print("Player is not in criteria")
            
                

def show_player_MI(player_name, info_type="all"):
    for player in teamMI:
        if player.get_name().lower() == player_name.lower():
                print(player.get_all_info())

                if player.get_runs()>1000 and player.get_wickets()> 50:
                    print("Player is all rounder")

                elif player.get_runs()>1000:
                 print("Player is batsman")
                
                elif player.get_wickets()>50:
                 print("Player is bowler")

                else:    
                    print("Player is not in criteria")

def show_player_CSK(player_name, info_type="all"):
    for player in teamCSK:
        if player.get_name().lower() == player_name.lower():
                print(player.get_all_info())

                if player.get_runs()>1000 and player.get_wickets()> 50:
                    print("Player is all rounder")

                elif player.get_runs()>1000:
                 print("Player is batsman")
                
                elif player.get_wickets()>50:
                 print("Player is bowler")

                else:    
                    print("Player is not in criteria")   


# Example usage:
e1=str(input("enter player name: "))
show_player_RCB(e1)
show_player_MI(e1)
show_player_CSK(e1)