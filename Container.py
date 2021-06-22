class Container:
    def __init__(self, lengteC, breedteC, hoogteC):

        self.lengteC = lengteC
        self.breedteC = breedteC
        self.hoogteC = hoogteC

    def getLengteC(self):
        return self.lengteC

    def getBreedteC(self):
        return self.breedteC

    def getHoogteC(self):
        return self.hoogteC

    def get_volumeC(self):
        return self.lengteC * self.breedteC * self.hoogteC

