import numpy as np
import pandas as pd
import os
import pyslha
from math import *

class MCMC():
    def __init__(self,PathToFreeParams):
        self.PathToFreeParams = PathToFreeParams
        self.freeparamsdata = pd.read_csv(self.PathToFreeParams, sep=",", header=0, names= ["ParamName","LowerLimit", "UpperLimit"])

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
    
    def GenerateCKMRmatrix(self, InputFileFullPath, OutputFileFullPath , MixingAngle = None):
        self.InputFileFullPath = InputFileFullPath
        self.OutputFileFullPath = OutputFileFullPath
        self.MixingAngle = MixingAngle

        if self.MixingAngle == None:
            
            self.RandomAngle =  np.random.uniform(0,90)

            self.CKMRinput11 = 1.0
            self.CKMRinput12 = 0.0
            self.CKMRinput13 = 0.0
            
            self.CKMRinput21 = 0.0
            self.CKMRinput22 = cos(self.RandomAngle)
            self.CKMRinput23 = sin(self.RandomAngle)

            self.CKMRinput31 = 0.0
            self.CKMRinput32 = sin(self.RandomAngle)
            self.CKMRinput33 = -cos(self.RandomAngle)

        elif self.MixingAngle != None:

            self.CKMRinput11 = 1.0
            self.CKMRinput12 = 0.0
            self.CKMRinput13 = 0.0

            self.CKMRinput21 = 0.0
            self.CKMRinput22 = cos(self.MixingAngle)
            self.CKMRinput23 = sin(self.MixingAngle)

            self.CKMRinput31 = 0.0
            self.CKMRinput32 = sin(self.MixingAngle)
            self.CKMRinput33 = -cos(self.MixingAngle)

        if self.CheckFile(self.InputFileFullPath) == True:
            with open(self.InputFileFullPath, 'r') as CKMRfile:
                self.CKMRdata = CKMRfile.read()        
        
            # Replace the target string
            self.CKMRdata = self.CKMRdata.replace('CKMRinput11', str("{:.6E}".format(self.CKMRinput11)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput12', str("{:.6E}".format(self.CKMRinput12)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput13', str("{:.6E}".format(self.CKMRinput13)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput21', str("{:.6E}".format(self.CKMRinput21)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput22', str("{:.6E}".format(self.CKMRinput22)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput23', str("{:.6E}".format(self.CKMRinput23)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput31', str("{:.6E}".format(self.CKMRinput31)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput32', str("{:.6E}".format(self.CKMRinput32)))
            self.CKMRdata = self.CKMRdata.replace('CKMRinput33', str("{:.6E}".format(self.CKMRinput33)))

            # Write the file out again
            with open(self.OutputFileFullPath, 'w') as updatedCKMRfile:
                self.CKMRdata = updatedCKMRfile.write(self.CKMRdata)


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

    def RunSPheno(self, SPhenoExeFullPath, LesHouchesInputFullPath):
        self.SPhenoExeFullPath = SPhenoExeFullPath
        self.LesHouchesInputFullPath =  LesHouchesInputFullPath

        if os.path.isfile(self.LesHouchesInputFullPath) == True:
            os.system(str(self.SPhenoExeFullPath)+" "+str(self.LesHouchesInputFullPath))
        else:
            print "Error in RunSPheno: No LesHouches File is found in the given path!"
    




















 
    

#    def CopySLHAtoCards(self, SLHAPath, CardsPath):
#        shutil.copy2(SLHAPath, CardsPath + "/param_card.dat") # complete target filename given
