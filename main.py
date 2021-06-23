from Box import Box
from Container import Container
from ContainerApi import *
from Costs import Costs

while True:
    try:
        #quantity input
        fitnessbankjeQ = int(input("How many fitness benches would you like to ship: "))
        fitnessmatQ = int(input("How many fitness mats would you like to ship: "))
        flessenQ = int(input("How many boxes of drinking bottles would you like to ship: "))
        voetballenQ = int(input("How many boxes of soccer balls with would you like to ship: "))
        break

    except:
        print("Invalid input, please try again")

#The object container is made below and the costs are determined
container = Container(5.85, 2.33, 2.37)
containerCosts = Costs(float(input("What are the estimated costs for shipping the container? EUROS: ")))

#all the different products that will be shipped, are made here as an object
fitnessMat1 = Box(0.63,0.2,0.2,"Blue")
fitnessBankje = Box(1.23,0.32,0.18,"Black/Red")
flessen = Box(0.77,0.395,0.295,"Black")
voetballen = Box(0.6,0.4,0.4,"default")


def fitCheck():
    """This functions calculates the total value of the products combined to see if it fits in the container.
        The program will tell you if it doesn't and you'll have to run the program again."""

    totalVolumeMat1 = fitnessMat1.get_volume()*fitnessmatQ
    totalVolumeBankje = fitnessBankje.get_volume()*fitnessbankjeQ
    totalVolumeFlessen = flessen.get_volume()*flessenQ
    totalVolumeVoetballen = voetballen.get_volume()*voetballenQ

    if (totalVolumeBankje+totalVolumeFlessen+totalVolumeVoetballen+totalVolumeMat1) > container.get_volumeC():
        quit(print("\nNOTE: The given quantities do not fit in one container, try again.\n\n"))


def calculateCostShare():
    """This funtion calculates the cost share per product, this costshare will
     eventually be added to the retail price"""

    #First we check if the products even fit in the container
    fitCheck()

    costs = containerCosts.getCosts()

    #Dividing the volume of a product by the volume of the container, then multipy it by 100%
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


calculateCostShare()



