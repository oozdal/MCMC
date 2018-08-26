from classMCMC import *

PathForFreeParams = "/Users/oozdal/readclass/freeparams.txt"
LesHouchesFilePath = "/Users/oozdal/readclass/LesHouches.in.LRSM"

###################################################################

Monte = MCMC(PathForFreeParams)

if Monte.CheckLesHouches(LesHouchesFilePath) == True:
    Monte.AssignValues()
