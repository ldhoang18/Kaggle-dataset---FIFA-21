import matplotlib
matplotlib.use('Agg')
import psycopg2
import matplotlib.pyplot as plt

#print records for players whose overall is greater than 85
connectionString = "dbname='ldhoang18_db' user='ldhoang18'"
connection = psycopg2.connect(connectionString)
cursor = connection.cursor()
sqlStatement = "SELECT player_name, position, dob, height, weight, overall FROM player WHERE overall >= 85;"
cursor.execute(sqlStatement)
records = cursor.fetchall()
for row in records:
	print(row)

print('------------End of record------------')
 
#print records for attacking players whose overall is greater than 85 
connectionString2 = "dbname='ldhoang18_db' user='ldhoang18'"
connection2 = psycopg2.connect(connectionString2)
cursor2 = connection2.cursor()
sqlStatement2 = "SELECT player_name, position, dob, height, weight, overall FROM player WHERE overall >= 85 AND best_position IN ('CAM', 'LW', 'RW', 'ST', 'CF');"
cursor2.execute(sqlStatement2)
records2 = cursor2.fetchall()
for row2 in records2:
	print(row2)
    
print('------------End of record------------')

#print records for defensive players whose overall is greater than 85
connectionString3 = "dbname='ldhoang18_db' user='ldhoang18'"
connection3 = psycopg2.connect(connectionString3)
cursor3 = connection3.cursor()
sqlStatement3 = "SELECT player_name, position, dob, height, weight, overall FROM player WHERE overall >= 85 AND best_position IN ('GK', 'RB', 'LB', 'RWB', 'LWB', 'CB', 'CDM');"
cursor3.execute(sqlStatement3)
records3 = cursor3.fetchall()
for row3 in records3:
	print(row3)
    
print('------------End of record------------')

#print records for teams whose overall is greater than 80
connectionString4 = "dbname='ldhoang18_db' user='ldhoang18'"
connection4 = psycopg2.connect(connectionString4)
cursor4 = connection4.cursor()
sqlStatement4 = "SELECT * FROM team WHERE overall >= 80;"
cursor4.execute(sqlStatement4)
records4 = cursor4.fetchall()
for row4 in records4:
    print(row4)

print('------------End of record------------')
#display data visualization for player height vs rating
def playervrating():
    height = []
    rating = []
    for row in records:
        height.append(row[3])
        rating.append(row[5])

    plt.plot(height, rating, '*')
    plt.xlabel('height')
    plt.ylabel('overall rating')
    plt.savefig("player_analysis.png")

#display data visualization for attacking player height vs rating
def attackvrating():
    height2 = []
    rating2 = []
    for row2 in records2:
        height2.append(row2[3])
        rating2.append(row2[5])

    plt.plot(height2, rating2, 'ro', color='green')
    plt.xlabel('Height')
    plt.ylabel('Overall')
    plt.savefig("attacking.png")
 
#display data visualization for defensive player height vs rating 
def defendvrating():
    height3 = []
    rating3 = []
    for row3 in records3:
        height3.append(row3[3])
        rating3.append(row3[5])

    plt.plot(height3, rating3, 'ro')
    plt.xlabel('Height')
    plt.ylabel('Overall')
    plt.savefig("defending.png")
    
#display data visualization for teams' attack and defense relationships
def attackvdefense():
    attack = []
    defense = []
    for row4 in records4:
        attack.append(row4[4])
        defense.append(row4[6])
        
    plt.plot(attack, defense, 'ro', color='purple')
    plt.xlabel('Defense rating')
    #plt.xticks(range(75,100))
    plt.ylabel('Attack rating')
    plt.savefig('teamattackdefense.png')
    
if __name__ == "__main__":
    playervrating()
    attackvrating()
    defendvrating()
    attackvdefense()