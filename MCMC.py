from classMCMC import *
from classReadSLHAforMCMC import *
import os

PathForFreeParams = os.path.join("/Users/oozdal/readclass/", "freeparams.txt")
LesHouchesFileFullPath = os.path.join("/Users/oozdal/readclass/", "LesHouches.in.LRSM")
UpdatedLesHouchesFileFullPath = os.path.join(LesHouchesFileFullPath)+"_updated"
SPhenoExecFullPath = os.path.join("/Users/oozdal/hepwork/SPheno-3.3.8/bin/", "SPhenoLRSM_NonSUSY_CKMRgRfree")
SPhenoOutputName = os.path.join("/Users/oozdal/readclass", "SPheno.spc.LRSM_NonSUSY_CKMRgRfree")

###################################################################

OutputNumber = 0 
MaxNumberOfOutput = 100

Monte = MCMC(PathForFreeParams)

#while OutputNumber < MaxNumberOfOutput:
Monte.AssignValues(LesHouchesFileFullPath, UpdatedLesHouchesFileFullPath)
Monte.RunSPheno(SPhenoExecFullPath)
if os.path.isfile(SPhenoOutputName) ==  True:
    newSLHA = ReadSLHA(SPhenoOutputName)
    if newSLHA.CheckSMlikeHiggsMass() == True:
        print "we did it"
    else:
        print "nanay"
