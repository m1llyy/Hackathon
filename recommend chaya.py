# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:09:29 2024

@author: mushk
"""

import pandas as pd
import random
def try1():
    num= input("Which song do you like more: enter number." + "\n"
                r"1 Mercy by shawn mendez" + "\n "
                r"2 Respect by Areana Franklin" + "\n"
                r"3 We will Rock You by Queen" + "\n"
                r"4 I know you want me by Pittbull" + "\n"
                r"5 Sweet Caroline by Neil Diamond" + "\n"
                r"6 Beverly Hills by Weezer:" + "\n")

    if num == '1':
        song = ["Respect","Aretha Franklin","FALSE","jazz blues","0.7","-6.4","115.0"]
    elif num == '2':
        song = ["Mercy","Shawn Mendez","FALSE","pop","0.6","-4.9","148.3"]
    elif num == '3':
        song = ["We will Rock You","Queen","FALSE","classic rock","0.7","-7.3","81.3"]
    elif num == '4':
        song = ["I Know You Want Me","Pittbull","FALSE","hip hop","0.8","-6.0","127.0"]
    elif num == '5':
        song = ["Sweet Caroline","Neil Diamond","FALSE","folk rock","0.5","-16.1","63.1"]
    elif num == '6':
        song = ["Beverly Hills","Weezer","FALSE","alternative","0.7","-3.8","87.9"]
    return song




"""if __name__ == "__main__":
    try1()"""
    
    

file_name = r"C:\Users\mushk\Downloads\my_hack - top_10000_1960-now.csv"
open_file = pd.read_csv(file_name)
df = pd.DataFrame(open_file)
#print(open_file)
#print(open_file.dtypes)

#print(df[my_filt])

data = try1()
filt = df["Track Name"] != data[0]
pos = df[filt]
filt1 = pos["Artist Genres"].str.contains(data[3], na = False)
pos1 = pos[filt1]
filt2 = pos1["Tempo"]> float(data[6])//10*10
pos2 = pos1[filt2]
filt3 = pos2["Tempo"]<float(data[6])//10*10+10
pos3 = pos2[filt3]
filt4 = pos["Danceability"]==float(data[4])
pos4 = pos3[filt4]

my_list = list(pos4.loc[filt, "Track Name"])
try:
    random_number = random.randint(0, len(my_list)-1)
    print(my_list[random_number])
except ValueError:
    my_list = list(pos3.loc[filt, "Track Name"])
    random_number = random.randint(0, len(my_list)-1)
    print(my_list[random_number])
#print(pos4.loc[filt, ["Track Name", "Artist Name(s)"]])
