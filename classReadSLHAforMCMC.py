import pyslha
import pandas as pd

class ReadSLHA():
    def __init__(self,SLHApath):
        self.SLHA = pyslha.read(SLHApath, ignoreblocks=['SPINFO'])

    def ReadSLHA_Block(self, BlockName, id1=None, id2=None, id3=None):
        self.BlockName       = BlockName
        self.id1             = id1
        self.id2             = id2
        self.id3             = id3

        self.list_all_blocks = self.SLHA.blocks
        self.pyslha_Block    = self.SLHA.blocks[self.BlockName]

        if self.id1 != None and self.id2 == None and self.id3 == None:
            self.VarValue1   = self.pyslha_Block[self.id1]
            return self.VarValue1

        elif self.id1 != None and self.id2 != None and self.id3 == None:
            self.VarValue2   = self.pyslha_Block[self.id1,self.id2]
            return self.VarValue2

        else:
            self.VarValue3   = self.pyslha_Block[self.id1,self.id2,self.id3]
            return self.VarValue3


    def CheckSMlikeHiggsMass(self):
        self.SMlikeHiggsMass = self.ReadSLHA_Block("MASS", 25 )

        if self.SMlikeHiggsMass >= 122. and self.SMlikeHiggsMass <= 128.:
            self.LogicSMlikeHiggsMass = True
        else:
            self.LogicSMlikeHiggsMass = False

        return self.LogicSMlikeHiggsMass    

















