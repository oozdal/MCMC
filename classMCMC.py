import numpy as np
import pandas as pd
import os
import pyslha

class MCMC():
    def __init__(self,PathToFreeParams):
        self.PathToFreeParams = PathToFreeParams
        self.freeparamsdata = pd.read_csv(self.PathToFreeParams, sep="  ", header=0, engine='python', names= ["ParamName","LowerLimit", "UpperLimit"])

        self.numberofparameters = len(self.freeparamsdata)

        self.params = {}
        for i in range(self.numberofparameters):
            self.params.update({self.freeparamsdata["ParamName"][i] : np.random.uniform(self.freeparamsdata["LowerLimit"][i], self.freeparamsdata["UpperLimit"][i]) }) 

    def CheckFile(self, FullFilePath):
        self.FullFilePath = FullFilePath
        self.SplitFilePath = self.FullFilePath.split("/")
        self.FileName = self.SplitFilePath[-1]

        self.FileElement_list = []
        for i in range(1, len(self.SplitFilePath)-1):
            self.FileElement_list.append("/"+self.SplitFilePath[i])

        self.OnlyFilePath = OnlyFilePath = ""
        for i in range(len(self.FileElement_list)):
            self.OnlyFilePath = self.OnlyFilePath + self.FileElement_list[i]

        return os.path.isfile(self.FullFilePath)    


    def AssignValues(self, LesHouchesFileFullPath, UpdatedLesHouchesFileFullPath):
        self.LesHouchesFileFullPath = LesHouchesFileFullPath
        self.UpdatedLesHouchesFileFullPath = UpdatedLesHouchesFileFullPath

        if self.CheckFile(self.LesHouchesFileFullPath) == True:
            with open(self.LesHouchesFileFullPath, 'r') as file:
                self.filedata = file.read()

            # Replace the target string
            for i in range(self.numberofparameters):
                self.filedata = self.filedata.replace(self.freeparamsdata["ParamName"][i], str("{:.6E}".format(self.params[str(self.freeparamsdata["ParamName"][i])])))

            # Write the file out again
            with open(self.UpdatedLesHouchesFileFullPath, 'w') as updatedfile:
                self.filedata = updatedfile.write(self.filedata)                        
        else:
            print "Error in AssignValues: No LesHouches File is found in the given path!"

    def RunSPheno(self, SPhenoExeFullPath, LesHouchesInputFullPath = None):
        self.SPhenoExeFullPath = SPhenoExeFullPath
        self.LesHouchesInputFullPath =  LesHouchesInputFullPath

        if self.LesHouchesInputFullPath == None and os.path.isfile(self.UpdatedLesHouchesFileFullPath) == True:
            os.system(str(self.SPhenoExeFullPath)+" "+str(self.UpdatedLesHouchesFileFullPath))
        elif self.LesHouchesInputFullPath != None and os.path.isfile(self.LesHouchesInputFullPath) == True:
            os.system(str(self.SPhenoExeFullPath)+" "+str(self.LesHouchesInputFullPath))
        else:
            print "Error in RunSPheno: No LesHouches File is found in the given path!"
    




















 
    

#    def CopySLHAtoCards(self, SLHAPath, CardsPath):
#        shutil.copy2(SLHAPath, CardsPath + "/param_card.dat") # complete target filename given
