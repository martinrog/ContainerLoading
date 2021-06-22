from Box import Box
from Container import Container
from ContainerApi import *

fitnessbankjeQ = int(input("Hoeveel dozen met fitnessbankjes wilt u vervoeren: "))
fitnessmatQ = int(input("Hoeveel dozen met fitnessmatten wilt u vervoeren: "))
flessenQ = int(input("Hoeveel dozen met drink flessen wilt u vervoeren: "))
voetballenQ = int(input("Hoeveel dozen met voetballen wilt u vervoeren: "))
container = Container(5.85, 2.33, 2.37)

fitnessMat1 = Box(0.63,0.2,0.2,"Blue")
fitnessMat2 = Box(0.63,0.2,0.2,"Black")
fitnessMat3 = Box(0.63,0.2,0.2,"Purple/Pink")
fitnessBankje = Box(1.23,0.32,0.18,"Black/Red")
flessen = Box(0.77,0.395,0.295,"Black")
voetballen = Box(0.6,0.4,0.4,"default")

