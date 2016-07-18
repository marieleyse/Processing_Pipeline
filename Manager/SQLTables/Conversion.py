__author__ = 'sulantha'
from Utils.DbUtils import DbUtils
from Manager.SQL.SQLBuilder import SQLBuilder
from Config import StudyConfig as sc
from Manager.SQLTables.ConversionObject import ConversionObject
class Conversion:
    def __init__(self):
        self.tableName = 'Conversion'
        self.DBClient = DbUtils()
        self.sqlBuilder = SQLBuilder()

    def getObjectFromTuple(self, tuple):
        valuesDict = dict(record_id=tuple[0], study=tuple[1], rid=tuple[2], scan_type=tuple[3],
                          scan_date=tuple[4].strftime("%Y-%m-%d"), scan_time=str(tuple[5]),
                          s_identifier=tuple[6], i_identifier=tuple[7], file_type=tuple[8], raw_folder=tuple[9],
                          converted_folder=tuple[10], version=tuple[11], converted=tuple[12])
        return ConversionObject(valuesDict)

    def insertToTable(self, objList):
        for obj in objList:
            self.DBClient.executeNoResult(
                self.sqlBuilder.getSQL_AddNewEntryToConversionTable(obj.sqlInsert()))

    def get_version(self, sortingObj, versionDict):
        if  sortingObj.study == 'ADNI':
            dl_path = sortingObj.download_folder
            if 'Uniform' in dl_path:
                return 'V2'
            else:
                return versionDict[sc.ProcessingModalityAndPipelineTypePerStudy[sortingObj.study][sortingObj.scan_type]] if sc.ProcessingModalityAndPipelineTypePerStudy[sortingObj.study][sortingObj.scan_type] in versionDict else 'V1'
        else:
            return versionDict[sc.ProcessingModalityAndPipelineTypePerStudy[sortingObj.study][sortingObj.scan_type]] if sc.ProcessingModalityAndPipelineTypePerStudy[sortingObj.study][sortingObj.scan_type] in versionDict else 'V1'


    def insertFromSortingObj(self, sortingObj, versionDict):
        sortingValues = sortingObj.getValuesDict()
        version = self.get_version(sortingObj, versionDict)
        sortingValues['converted_folder'] = '{0}/{1}/{2}/{3}/{4}_{5}_{6}/{7}/converted/final'.format(sc.studyDatabaseRootDict[sortingObj.study],
                                                                        sortingObj.study, sortingObj.scan_type, sortingObj.rid,
                                                                        sortingObj.scan_date, sortingObj.s_identifier, sortingObj.i_identifier, version)
        sortingValues['version'] = version
        sortingValues['converted'] = 0
        self.insertToTable([ConversionObject(sortingValues)])

    def gettoBeConvertedPerStudy(self, study):
        toConvertList = self.DBClient.executeAllResults(
            self.sqlBuilder.getSQL_getToBeConvertedFileFromConversionTable(study))
        return [self.getObjectFromTuple(t) for t in toConvertList]

    def setConvertedTrue(self, convertionObj):
        convertionObj.converted = 1
        self.saveObj(convertionObj)

    def setConvertedFailed(self, convertionObj):
        convertionObj.skip = 1
        self.saveObj(convertionObj)

    def saveObj(self, convertionObj):
        self.DBClient.executeNoResult(self.sqlBuilder.getSQL_saveObjConversionTable(convertionObj))

    def getConvertedListPerStudy(self, study):
        convertedList = self.DBClient.executeAllResults(self.sqlBuilder.getSQL_getAllConvertedFromConvertionTable(study))
        return [self.getObjectFromTuple(t) for t in convertedList]
