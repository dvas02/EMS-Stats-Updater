#!/usr/bin/python3

# Variables
        # numShifts
        # numCalls
        # coolestShift

# Call Specifications - Make each a function with their own questions
        # noCalls
        # dayShift
        # eveningShift
        # nightShift
        # cancelled // 10-03
        # hazallah
        # carCrash // 10-08
        # weakDizzy
        # heartAttack
        # stroke
        # fall
        # brokenBone
        # youngest
        # oldest
        # didSomething
        # burn
        # longest

# Notes
        # Rewrite the text file to have only the needed data, no words to make it easier to rewrite
        # Once the user has done something, the entire program needs to shut down to save the changes

################################################################################
#                                                                              #
#                                                                              #
#                                   Main Code                                  #
#                                                                              #
#                                                                              #
################################################################################

####
#INTERPRETING EMS_Stats_Data.txt
###

#fp = open("EMS_Stats_Data.txt", "r") #Open EMS Stats text file - READONLY

fp = open("EMS_Stats_Data_nums.txt", "r")


#Start with assigning the easy variables that require no looping

numShifts = int(fp.readline().strip())
numCalls = int(fp.readline().strip())
noCalls = int(fp.readline().strip())
dayShift = int(fp.readline().strip())
eveningShift = int(fp.readline().strip())
nightShift = int(fp.readline().strip())
cancelled = int(fp.readline().strip())


#Complex Variables (Includes the which number is said call)
hazallahNUM = int(fp.readline().strip())
hazallahARR = (fp.readline().strip()).split(",")

carCrashNUM = int(fp.readline().strip())
carCrashARR = (fp.readline().strip()).split(",")

weakDizzyNUM = int(fp.readline().strip())
weakDizzyARR = (fp.readline().strip()).split(",")

heartAttackNUM = int(fp.readline().strip())
heartAttackARR = (fp.readline().strip()).split(",")

strokeNUM = int(fp.readline().strip())
strokeARR = (fp.readline().strip()).split(",")

brokenBoneNUM = int(fp.readline().strip())
brokenBoneARR = (fp.readline().strip()).split(",")

burnNUM = int(fp.readline().strip())
burnARR = (fp.readline().strip()).split(",")

#Single call (record)

youngestAGE = fp.readline().strip()
youngestCALL = int(fp.readline().strip())

oldestAGE = fp.readline().strip()
oldestCALL = int(fp.readline().strip())

longestTIME = fp.readline().strip()
longestCALL = int(fp.readline().strip())

#Special
fallNUM = int(fp.readline().strip())
fallARR = (fp.readline().strip()).split(",")
fallHIGHEST = fp.readline().strip()

#Did something

oxygenNUM = int(fp.readline().strip())
oxygenCALL = (fp.readline().strip()).split(",")

#Notable Moments

numMoments = int(fp.readline().strip())
momentsDict = {}


for i in range(1,numMoments+1):
        momentsDict[i] = fp.readline().strip()
        

#Calls

callsDict = {}

for i in range(1,numCalls+1):
        callsDict[i] = fp.readline().strip()



####
#USER INPUT CALL INFORMATION
####


#Functions for Main Menu
#Once function is done, copy and paste it into while loop 




def GetInfo():
        # Lots of info here
        return("Done")




#MAIN MENU LOOP#

print("Welcome to the Dov's EMS Calls and Information Program\n")


while True:
        #Main print statements
        print("\n\nMenu Options")
        print("1. Add new shift")
        print("2. Remove shift")
        print("3. Add a new call")
        print("4. Produce charts")
        print("5. Add a new notable moment")
        print("6. Add shift with no calls")
        print("7. Remove shift with no calls")
        print("8. Add a cancelled call (10-03)")
        print("9. Remove a cancelled call (10-03)")
        print("10. Exit\n\n")


        
        userI = input("Enter an option 1-10: ")
        print("\n\n")

        if userI == "1":
                numShifts = numShifts + 1

                while True:
                        shiftType = input("Was the shift day, evening or night? ")
                        if shiftType == "day":
                                dayShift = dayShift + 1
                                print("Day shift added")
                                print(dayShift)
                                break
                        if shiftType == "evening":
                                eveningShift = eveningShift + 1
                                print("Evening shift added")
                                print(eveningShift)
                                break
                        if shiftType == "night":
                                nightShift = nightShift + 1
                                print("Night shift added")
                                print(nightShift)
                                break
        

        if userI == "2":
                numShifts = numShifts - 1

                while True:
                        shiftType = input("Was the shift you are removing day, evening or night? ")
                        if shiftType == "day":
                                dayShift = dayShift - 1
                                print("Day shift removed")
                                print(dayShift)
                                break
                        if shiftType == "evening":
                                eveningShift = eveningShift - 1
                                print("Evening shift removed")
                                print(eveningShift)
                                break
                        if shiftType == "night":
                                nightShift = nightShift - 1
                                print("Night shift removed")
                                print(nightShift)
                                break



        if userI == "3":
                
                numCalls = numCalls + 1
                print("You are at {d} calls".format(d=numCalls))


                #Add blurb about call
                callInfo = input("Describe call: ")
                callsDict[numCalls] = callInfo
                print(callsDict)


                #Call specifics questions
                print("Answer all questions with y/n")

                isHazallah = input("Was Hazallah there? ")
                if isHazallah == "y":
                        hazallahNUM=hazallahNUM+1
                        hazallahARR.append(numCalls)


                isCarCrash = input("Was it a car crash? ")
                if isCarCrash == "y":
                        carCrashNUM=carCrashNUM+1
                        carCrashARR.append(numCalls)

                isWeakDizzy = input("Was it a weak/dizzy call? ")
                if isWeakDizzy == "y":
                        weakDizzyNUM=weakDizzyNUM+1
                        weakDizzyARR.append(numCalls)
                
                isheartAttackNUM = input("Was it a heart attack? ")
                if isheartAttackNUM == "y":
                        heartAttackNUM=heartAttackNUM+1
                        heartAttackARR.append(numCalls)

                isstrokeNUM = input("Was it a stroke call? ")
                if isstrokeNUM == "y":
                        strokeNUM=strokeNUM+1
                        strokeARR.append(numCalls)

                isbrokenBoneNUM = input("Was it a broken bone? ")
                if isbrokenBoneNUM == "y":
                        brokenBoneNUM=brokenBoneNUM+1
                        brokenBoneARR.append(numCalls)

                isburnNUM = input("Was it a burn? ")
                if isburnNUM == "y":
                        burnNUM=burnNUM+1
                        burnARR.append(numCalls)

                isFall = input("Was it a fall? ")
                if isFall == "y":
                        fallNUM=fallNUM+1
                        fallARR.append(numCalls)

                #Check if record call of any sort
                print("Does it beat any of the following categories: ")
                print("Youngest: {d}".format(d=youngestAGE))
                print("Oldest: {d}".format(d=oldestAGE))
                print("Longest: {d}".format(d=longestTIME))
                print("Highest Fall: {d}".format(d=fallHIGHEST))
                isRecord = input("y/n: ")
                if isRecord == "y":
                        whichRecord = input("Which record did it beat? (youngest/oldest/longest/fall) ")
                        if whichRecord == "youngest":
                                newAge = input("What is the new youngest age? ")
                                youngestAGE=newAge
                                youngestCALL=numCalls
                                print("New youngest age is {age} old and it is call number {callNum}".format(age=youngestAGE, callNum=numCalls))                                

                        if whichRecord == "oldest":
                                newAge = input("What is the new oldest age? ")
                                oldestAGE=newAge
                                oldestCALL=numCalls
                                print("New oldest age is {age} old and it is call number {callNum}".format(age=oldestAGE, callNum=numCalls)) 

                        if whichRecord == "longest":
                                newTime = input("What is the new longest time? ")
                                longestTIME=newTime
                                longestCALL=numCalls
                                print("New longest time is {time} long and it is call number {callNum}".format(time=longestTIME, callNum=numCalls)) 

                        if whichRecord == "fall":
                                newHeight = input("What is the new highest fall height? ")
                                fallHIGHEST=newHeight
                                print("New heighest fall height is {height} high and it is call number {callNum}".format(height=fallHIGHEST, callNum=numCalls))



                #Check if did something
                print("Did you do any of the following? ")
                print("Provided Oxygen")
                #Epipen
                #Noloxone
                #Sugar
                #Splint
                #Bandage
                #CPR
                #DEFIB
                didSomething = input("y/n ")
                if didSomething == "y":
                        whichHelp = input("What did you do? (oxygen) ")
                        if whichHelp == "oxygen":
                                oxygenNUM=oxygenNUM+1
                                oxygenCALL.append(numCalls)
                                print("You have administered Oxygen {d} times".format(d=oxygenNUM))
                                





        if userI == "4":
                import numpy as np
                import matplotlib.pyplot as plt
                

                #Two pie charts, one for day/evening/night shifts
                #Other for type of call (stroke, heart attack, etc)
                #One bar graph for everything else (hazallah, no calls, cancelled, etc)
                #One graph for record calls
                
                ######
                #GRAPH 1 - Pie Chart - Day/Evening/Night
                #####

                fig, ax = plt.subplots(figsize=(6,3), subplot_kw=dict(aspect="equal"))
                
                callTypes = [str(dayShift) + " Day", str(eveningShift) + " Evening", str(nightShift) + " Night"]
                                        
                data = [float(x.split()[0]) for x in callTypes]
                shiftTypes = [x.split()[-1] for x in callTypes]
                
                def func(pct, allvals):
                        absolute = int(np.round(pct/100.*np.sum(allvals)))
                        return "{:.1f}%\n({:d} Shifts)".format(pct, absolute)
                

                wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="w"))

                ax.legend(wedges, shiftTypes, title="Time of Shift", loc="center left", bbox_to_anchor=(1,0,0.5,1))

                plt.setp(autotexts,size=8,weight="bold")
                ax.set_title("Percentage of the different types of shifts")
                plt.show()
                

                ########
                #GRAPH 2 - Pie Chart - carCrashNUM/weakDizzyNUM/heartAttackNUM/strokeNUM/brokenBoneNUM/burnNUM/fallNUM
                #######


                fig, ax = plt.subplots(figsize=(12,6), subplot_kw=dict(aspect="equal"))

                callTypes = [str(carCrashNUM) + " CarCrash", str(weakDizzyNUM) + " WeakDizzy", str(heartAttackNUM) + " HeartAttack", str(strokeNUM) + " Stroke", str(brokenBoneNUM) + " BrokenBone", str(burnNUM) + " Burn", str(fallNUM) + " Fall"]

                data = [float(x.split()[0]) for x in callTypes]
                shiftTypes = [x.split()[-1] for x in callTypes]

                def func(pct, allvals):
                        absolute = int(np.round(pct/100.*np.sum(allvals)))
                        return "{:.1f}%\n({:d} Calls)".format(pct, absolute)


                wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="w"))

                ax.legend(wedges, shiftTypes, title="Time of Shift", loc="center left", bbox_to_anchor=(1,0,0.5,1))

                plt.setp(autotexts,size=6,weight="bold")
                ax.set_title("Percentage of the different types of calls")
                plt.show()


                #######
                #Graph 3 - Bar Graph - noCalls/cancelled/hazallahNUM
                #######
                
                
                data = {"No Calls":noCalls, "Cancelled (10-03)":cancelled, "Hazallah":hazallahNUM}
                info = list(data.keys())
                values = list(data.values())
                
                fig = plt.figure(figsize = (10,5))

                plt.bar(info, values, color="maroon", width = 0.5)
                plt.title("Other call information and data")
                plt.show() 



                #############
                #Record Calls - Formatted Printing - youngestAGE/oldestAGE/longestTIME/fallHIGHEST
                #############

                print("Youngest Patient: {}".format(youngestAGE))
                print("Oldest Patient: {}".format(oldestAGE))
                print("Longest Call: {}".format(longestTIME))
                print("Highest Fall: {}".format(fallHIGHEST))
        


                
        if userI == "5":
                moment = input("Type in your moment here (Don't forget the date at the end): ")


                momentsDict[numMoments+1] = moment
                numMoments = numMoments + 1

                print(momentsDict)

        
        if userI == "6":
                noCalls = noCalls + 1
                print("Shift with no calls added")
                print("You have {d} shifts with no calls".format(d=noCalls))
                

        if userI == "7":
                noCalls = noCalls - 1
                print("Shift with no calls removed")
                print("You have {d} shifts with no calls".format(d=noCalls))


        if userI == "8":
                cancelled = cancelled + 1
                print("Shift added")
                print("You have {d} cancelled (10-03) calls".format(d=cancelled))
        

        if userI == "9":
                cancelled = cancelled - 1
                print("Cancelled shift removed")
                print("You have {d} cancelled (10-03) calls".format(d=cancelled))



        if userI == "10":
                print("Bye!\n\n")
                break




fp.close()




################
#              #
# REWRITE FILE #
#              #
################

fp = open("EMS_Stats_Data_nums.txt", "w")
fp.write(str(numShifts)+"\n")
fp.write(str(numCalls)+"\n")
fp.write(str(noCalls)+"\n")
fp.write(str(dayShift)+"\n")
fp.write(str(eveningShift)+"\n")
fp.write(str(nightShift)+"\n")
fp.write(str(cancelled)+"\n")

fp.write(str(hazallahNUM)+"\n")
for i in hazallahARR:
        if i == hazallahARR[len(hazallahARR)-1]:
                fp.write(str(i))        
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(str(carCrashNUM)+"\n")
for i in carCrashARR:
        if i == carCrashARR[len(carCrashARR)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(str(weakDizzyNUM)+"\n")
for i in weakDizzyARR:
        if i == weakDizzyARR[len(weakDizzyARR)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(str(heartAttackNUM)+"\n")
for i in heartAttackARR:
        if i == heartAttackARR[len(heartAttackARR)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(str(strokeNUM)+"\n")
for i in strokeARR:
        if i == strokeARR[len(strokeARR)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(str(brokenBoneNUM)+"\n")
for i in brokenBoneARR:
        if i == brokenBoneARR[len(brokenBoneARR)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(str(burnNUM)+"\n")
for i in burnARR:
        if i == burnARR[len(burnARR)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(youngestAGE+"\n")
fp.write(str(youngestCALL)+"\n")
fp.write(oldestAGE+"\n")
fp.write(str(oldestCALL)+"\n")
fp.write(longestTIME+"\n")
fp.write(str(longestCALL)+"\n")

fp.write(str(fallNUM)+"\n")
for i in fallARR:
        if i == fallARR[len(fallARR)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")
fp.write(fallHIGHEST+"\n")

fp.write(str(oxygenNUM)+"\n")
for i in oxygenCALL:
        if i == oxygenCALL[len(oxygenCALL)-1]:
                fp.write(str(i))
        else:
                fp.write(str(i)+",")
fp.write("\n")

fp.write(str(numMoments)+"\n")

for key in momentsDict:
        fp.write(momentsDict[key])
        fp.write("\n")

for key in callsDict:
        fp.write(callsDict[key])
        fp.write("\n")




fp.close()
