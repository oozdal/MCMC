import numpy as np
import pandas as pd
import os

class MCMC():
    def __init__(self,PathToFreeParams):
        self.PathToFreeParams = PathToFreeParams
        self.freeparamsdata = pd.read_csv(self.PathToFreeParams, sep="  ", header=0, engine='python', names= ["ParamName","LowerLimit", "UpperLimit"])

        self.numberofparameters = len(self.freeparamsdata)

        self.params = {}
        for i in range(self.numberofparameters):
            self.params.update({self.freeparamsdata["ParamName"][i] : np.random.uniform(self.freeparamsdata["LowerLimit"][i], self.freeparamsdata["UpperLimit"][i]) }) 

    def CheckLesHouches(self,LesHouchesFullPath):
        self.LesHouchesFullPath = LesHouchesFullPath
        self.SplitFilePath = self.LesHouchesFullPath.split("/") 
        self.LesHouchesFileName = self.SplitFilePath[-1]
        
        self.FileElement_list = []
        for i in range(1, len(self.SplitFilePath)-1):
            self.FileElement_list.append("/"+self.SplitFilePath[i])

        self.LesHouchesOnlyPath = ""
        for i in range(len(self.FileElement_list)):
            self.LesHouchesOnlyPath = self.LesHouchesOnlyPath + self.FileElement_list[i]

        return os.path.isfile(self.LesHouchesFullPath)

    def AssignValues(self):
        with open(self.LesHouchesFullPath, 'r') as file:
            self.filedata = file.read()

        # Replace the target string
        for i in range(self.numberofparameters):
            self.filedata = self.filedata.replace(self.freeparamsdata["ParamName"][i], str("{:.6E}".format(self.params[str(self.freeparamsdata["ParamName"][i])])))

        # Write the file out again
        with open(self.LesHouchesFullPath+"_updated", 'w') as updatedfile:
            self.filedata = updatedfile.write(self.filedata)

#    def CopySLHAtoCards(self, SLHAPath, CardsPath):
#        shutil.copy2(SLHAPath, CardsPath + "/param_card.dat") # complete target filename given
