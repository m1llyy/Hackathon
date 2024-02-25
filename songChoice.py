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
    print(song)




if __name__ == "__main__":
    print(try1())