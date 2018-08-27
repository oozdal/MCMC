from classMCMC import *
import os

PathForFreeParams = os.path.join("/Users/oozdal/readclass/", "freeparams.txt")
LesHouchesFileFullPath = os.path.join("/Users/oozdal/readclass/", "LesHouches.in.LRSM")
UpdatedLesHouchesFileFullPath = os.path.join(LesHouchesFileFullPath)+"_updated"
SPhenoExecFullPath = os.path.join("/Users/oozdal/hepwork/SPheno-3.3.8/bin/", "SPhenoLRSM_NonSUSY_CKMRgR_tsbar")
SPhenoOutputName = "Spheno.spc"

###################################################################

OutputNumber = 0 
MaxNumberOfOutput = 100

Monte = MCMC(PathForFreeParams)

while OutputNumber < MaxNumberOfOutput:
    Monte.AssignValues(LesHouchesFileFullPath, UpdatedLesHouchesFileFullPath)
    Monte.RunSPheno(SPhenoExecFullPath)
