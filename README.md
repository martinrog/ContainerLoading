# ContainerLoading
Container loading project

This project contains a program that simplifies the process of shipping goods. This is done by
displaying a visualization of the loading proces. This is very important because, the costs of
overseas shipping are often very high, so the container must be loaded optimally. Also a price
is automatically given per product that will cover the cost of the shipping.

To get the desired output, only the “main” file has to be runned and then fill in the quantities.
The output of the program provides all the information needed. To see the visualization, paste 
the URL next to “image_complete” into the search bar of your browser. To see an intermediate 
step, paste the URL next to "image_sbs" into the search bar of your browser.

Measurements: Metric (meters)

--------------------------------------------------------------------------------------------------

To add new products you have add a few things to two different files, all explained below:

Main file:
(At "newProduct" fill in your own product name)

Add the product to the quantity input, using the following syntax (EXAMPLE):
newProductQ = int(input("How many newProducts would you like to ship: "))

Add a new object to the objectslist (starting from line 23), using the following syntax:
newProduct = Box(0.5,0.5,0.5,"default")

Add a total volume variable in the "fitCheck" function, using the following syntax:
totalVolumeNewProduct = newProduct.get_volume()*newProductQ
+
Add the new variable to to if-statement in line 38.

Add a share variable in the "calculateCostShare" function, using the following syntax:
newProductShare = (newProduct.get_volume()/container.get_volumeC())*100
+
Add a print statement in this function:
 "A box newProduct will have a share of: ",round(newProductShare,3),"% what comes to ",((costs/100)*newProductShare),"EUROS per product.\n"
 
These were the additions in the main file.

ContainerAPi:

In the variable "data", at the header "items", add the following line of code:
(At "newProduct" fill in your own product name which you just made in the main file)

{"w": newProduct.getBreedte(), "h": newProduct.getHoogte(), "d": newProduct.getLengte(), "q": newProductQ, "vr": 1, "wg": 0, "id": "newProduct"}

END

If you followed the steps correctly, your item has been added to the container list.
