class Box:
    """Box class with four entities that describes the data of the products"""

    def __init__(self,lengte,breedte,hoogte,type):

        self.lengte = lengte
        self.breedte = breedte
        self.hoogte = hoogte
        self.type = type

    """Functions to get the measurements and to calculate the volume"""
    def getLengte(self):
        return self.lengte

    def getBreedte(self):
        return self.breedte

    def getHoogte(self):
        return self.hoogte

    def get_volume(self):
        return self.lengte * self.breedte * self.hoogte