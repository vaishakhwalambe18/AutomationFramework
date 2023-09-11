import logging
import datetime;
import sys


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
                            filename=".\\Reports\\aLogs.log",
                            filemode="w",
                            format='%(asctime)s %(levelname)s %(message)s',
                            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
