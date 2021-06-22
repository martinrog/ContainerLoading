from Box import Box
from Container import Container
from ContainerApi import *
from Costs import Costs

try:
    fitnessbankjeQ = int(input("How many fitness benches would you like to ship: "))
    fitnessmatQ = int(input("How many fitness mats would you like to ship: "))
    flessenQ = int(input("How many boxes of drinking bottles would you like to ship: "))
    voetballenQ = int(input("How many boxes of soccer balls with would you like to ship: "))
except:
    print("Invalid input, please try again")


container = Container(5.85, 2.33, 2.37)
containerCosts = Costs(float(input("What are the estimated costs for shipping the container? EUROS: ")))

fitnessMat1 = Box(0.63,0.2,0.2,"Blue")
fitnessMat2 = Box(0.63,0.2,0.2,"Black")
fitnessMat3 = Box(0.63,0.2,0.2,"Purple/Pink")
fitnessBankje = Box(1.23,0.32,0.18,"Black/Red")
flessen = Box(0.77,0.395,0.295,"Black")
voetballen = Box(0.6,0.4,0.4,"default")

def calculateCostShare():

    costs = containerCosts.getCosts()
    fitnessBankShare = (fitnessBankje.get_volume()/container.get_volumeC())*100
    fitnessMatShare = (fitnessMat1.get_volume()/container.get_volumeC())*100
    bottleShare = (flessen.get_volume()/container.get_volumeC())*100
    ballShare = (voetballen.get_volume()/container.get_volumeC())*100

    print(  "\nAll products contain a different amount of volume, so the products carry their own percentage cost.\n"
            "The percentages are as follows:\n\n"
            "A fitness bench will have a share of: ",round(fitnessBankShare,3),"% what comes to ",((costs/100)*fitnessBankShare),"EUROS per product.\n"
            "A fitness mat will have a share of: ",round(fitnessMatShare,3),"% what comes to ",((costs/100)*fitnessMatShare),"EUROS per product.\n"
            "A box of bottles will have a share of: ",round(bottleShare,3),"% what comes to ",((costs/100)*bottleShare),"EUROS per product.\n"
            "A box of soccer balls will have a share of: ",round(ballShare,3),"% what comes to ",((costs/100)*ballShare),"EUROS per product.\n")

def fitCheck():
    totalVolumeMat1 = fitnessMat1.get_volume()*fitnessmatQ
    totalVolumeBankje = fitnessBankje.get_volume()*fitnessbankjeQ
    totalVolumeFlessen = flessen.get_volume()*flessenQ
    totalVolumeVoetballen = voetballen.get_volume()*voetballenQ

    if (totalVolumeBankje+totalVolumeFlessen+totalVolumeVoetballen+totalVolumeMat1) > container.get_volumeC():
        quit(print("\nNOTE: The given quantities do not fit in one container, try again.\n\n"))


calculateCostShare()
fitCheck()


