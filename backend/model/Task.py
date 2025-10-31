class Task:

    def __init__(self,id : int,name : str,description : str):
        self.id = id
        self.name = name
        self.description = description
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getId(self):
        return self.id
    
    def setName(self,name : str):
        self.name = name
    
    def setDescription(self, description : str):
        self.description = description
    
    def setId(self, id : int):
        self.id = id

