class Container:
    """Container class with three entities that describes the measurents of the container"""

    def __init__(self, lengteC, breedteC, hoogteC):
        self.lengteC = lengteC
        self.breedteC = breedteC
        self.hoogteC = hoogteC


    """Functions to get the measurements and to calculate the volume"""
    def getLengteC(self):
        return self.lengteC

    def getBreedteC(self):
        return self.breedteC

    def getHoogteC(self):
        return self.hoogteC

    def get_volumeC(self):
        return self.lengteC * self.breedteC * self.hoogteC

