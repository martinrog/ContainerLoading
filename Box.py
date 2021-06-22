class Box:

    def __init__(self,lengte,breedte,hoogte,type):

        self.lengte = lengte
        self.breedte = breedte
        self.hoogte = hoogte
        self.type = type

    def getLengte(self):
        return self.lengte

    def getBreedte(self):
        return self.breedte

    def getHoogte(self):
        return self.hoogte

    def get_volume(self):
        return self.lengte * self.breedte * self.hoogte