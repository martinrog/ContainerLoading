class Costs:

    def __init__(self,shippingPrice):

        self.shippingCosts = float(input("What are the estimated total costs of the shipment? EUROS: "))

    def getPrice(self):
        return self.shippingCosts

    def calculatePrice(self):
        pass
