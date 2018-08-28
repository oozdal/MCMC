from classMCMC import *
from classReadSLHAforMCMC import *
import os

PathForFreeParams = os.path.join("/Users/oozdal/readclass/", "freeparams.txt")
LesHouchesFileFullPath = os.path.join("/Users/oozdal/readclass/", "LesHouches.in.LRSM")
UpdatedLesHouchesFileFullPath = os.path.join(LesHouchesFileFullPath)+"_updated"
SPhenoExecFullPath = os.path.join("/Users/oozdal/hepwork/SPheno-3.3.8/bin/", "SPhenoLRSM_NonSUSY_CKMRgR_tsbar")
SPhenoOutputName = os.path.join("/Users/oozdal/readclass", "SPheno.spc.LRSM_NonSUSY_CKMRgR_tsbar")
SPhenoOutputDestination = os.path.join("/Users/oozdal/readclass/LRSM_MCMC", "LRSM_")

###################################################################

OutputNumber = 1
MaxNumberOfOutput = 20

Monte = MCMC(PathForFreeParams)

while OutputNumber < MaxNumberOfOutput:
#    Monte.AssignValues(LesHouchesFileFullPath, UpdatedLesHouchesFileFullPath)
    Monte.GenerateCKMRmatrix(LesHouchesFileFullPath,UpdatedLesHouchesFileFullPath)
    Monte.RunSPheno(SPhenoExecFullPath, UpdatedLesHouchesFileFullPath)
    if os.path.isfile(SPhenoOutputName) ==  True:
        newSLHA = ReadSLHA(SPhenoOutputName)
        if newSLHA.CheckSMlikeHiggsMass() == True:
            if newSLHA.CheckBphysics() == True:
                SPhenoOutputTag = SPhenoOutputDestination + str(OutputNumber)
                os.rename(SPhenoOutputName,SPhenoOutputTag)
                OutputNumber = OutputNumber + 1
                print "New solution is found!"
            else:
                os.remove(SPhenoOutputName)
                print "B-physics is not satisfied!"
                continue
        else:
            print "SM-like Higgs Mass is not satisfied!"
            continue
    else:
        print "Error: No SLHA Output is found."
        continue
