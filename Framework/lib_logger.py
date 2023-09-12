import calendar
import logging
import os
import time


from Framework.lib_util import *


class LogGen:

    @staticmethod
    def save_screenshot(driver):
        driver.save_screenshot(".\\Reports\\lastsc.png")

    # @staticmethod
    # def updateLog(typeofLog, actionPerformed, valuesConcatenated, resultsGenerated):
    #     '''add strig to doc string'''
    #     f = open("C:\AutomationFramework\logs.txt", "a+")
    #     ct = datetime.datetime.now()
    #     logString = typeofLog.upper() + " " + actionPerformed + " " + str(valuesConcatenated) + " " + str(
    #         resultsGenerated)
    #     f.write(str(ct) + logString + "\n")
    #     print(ct, typeofLog.upper(), actionPerformed, valuesConcatenated, resultsGenerated)

    @staticmethod
    def loggen():
        # Add comment to log file
        logging.basicConfig(level=logging.INFO,
                            filename=".\\Reports\\Latest_Execution.log",
                            filemode="w",
                            format='%(asctime)s %(levelname)s %(message)s',
                            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


class ReportFolder:
    root_report_path = ReadConfig().getValue('common path', 'report_folder_path')

    def subCreateExecutionResultFolder(self):
        # gmt stores current gmtime
        gmt = time.gmtime()
        # ts stores timestamp
        ts = str(calendar.timegm(gmt))
        curr_execution_folder = self.root_report_path+'//Execution_'+ts
        os.mkdir(curr_execution_folder)
        return curr_execution_folder
