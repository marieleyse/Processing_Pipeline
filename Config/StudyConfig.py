__author__ = 'Sulantha'

AllowedStudyList = ['ADNI', 'ADNI_OLD']
AllowedStepsList = ['Sort', 'Move', 'T1Beast', 'T1Process', 'ProcessAV45', 'ProcessFDG', 'ProcessFMRI', 'ProcessDTI']
AllowedVersions = ['1', '2', '3']
AllowedModalityList = ['T1', 'AV45', 'FDG', 'MT1__GradWarp__N3m', 'MT1__N3m']

#This dictionary will have the list of modalities for each study type, where only these type of images be moved and processed.
ProcessingImagingModalities = {'ADNI':('T1', 'AV45', 'FDG', 'MT1_G_N3m', 'MT1_N3m','rsfmri','ext-rsfmri')}

defaultVersioningForStudy = {'ADNI':{'T1':'V1', 'AV45':'V1', 'FDG':'V1', 'MT1_G_N3m':'V1', 'MT1_N3m':'V1',
                                     'rsfmri':'V1','ext-rsfmri':'V1'}}

ADNIDownloadRoot = '/data/backup-data02/ADNI/downloads/New2'
ADNIOLDDownloadRoot = '/data/backup-data02/ADNI/new_raw/EMCI'


studyDatabaseRootDict = {'ADNI': '/data/data03/Database', 'ADNI_OLD': '/data/data03/Database' }
