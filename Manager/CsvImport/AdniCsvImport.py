__author__ = 'wang'

from Manager.CsvImport.csvToDatabase import csvToDatabase
from Utils.DbUtils import DbUtils
import glob
import os

class AdniCsvImport:
    def __init__(self, inputFolder):
        # Initiate Database Client
        self.DbClient = DbUtils(database='Study_Data.ADNI')

        # For each csv file, import it into the SQL database
        for file in glob.glob(inputFolder + '/*.csv'):
            sqlLocation = os.path.basename(file).replace('.csv', '')
            with open(file, 'r') as csvFile:
                csvToDatabase(self.DbClient, csvFile, sqlLocation)

        #  Close the connection to the database
        self.DbClient.close()