__author__ = 'wang'
from Recursor.ADNI.ADNIRecursor import ADNIRecursor
from Recursor.DIAN.DIANRecursor import DIANRecursor
from Recursor.ADNI.ADNIRecursorFromOldData import ADNIRecursorFromOldData

"""
A non-specific recursor that calls the right study-specific recursor and informs the root folder location
"""

class Recursor:
    def __init__(self, studyID, root_download):
        self.study = studyID
        self.root_download = root_download
        self.subRecursor = None
        if studyID.lower() == 'adni':
            self.subRecursor = ADNIRecursor(studyID, root_download)
        elif studyID.lower() == 'adni_old':
            self.subRecursor = ADNIRecursorFromOldData(studyID, root_download)
        elif studyID.lower() == 'dian':
            self.subRecursor = DIANRecursor(studyID, root_download)
        else:
            pass

    def recurse(self):
        return self.subRecursor.recurse()
