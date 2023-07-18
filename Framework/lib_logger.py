import logging
import datetime;
import sys



class LogGen:

    @staticmethod
    def loggen():
        '''Add commment to log file'''
        logging.basicConfig(filename="C:\AutomationFramework\Logsautomation.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    @staticmethod
    def updateLog(typeofLog,actionPerformed,valuesConcatenated,resultsGenerated):
        '''add strig to doc string'''
        f = open("C:\AutomationFramework\logs.txt", "a+")
        ct = datetime.datetime.now()
        logString = typeofLog.upper()+" "+actionPerformed+" "+str(valuesConcatenated)+" "+str(resultsGenerated)
        f.write(str(ct)+logString+"\n")
        print(ct,typeofLog.upper(),actionPerformed,valuesConcatenated,resultsGenerated)