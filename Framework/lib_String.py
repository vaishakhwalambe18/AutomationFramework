from Framework.lib_logger import LogGen
class lib_String:
    @staticmethod
    def kyRemoveLineBreak(input_string):
        output_string = input_string.replace('\n', '').replace('\r', '')
        LogGen.updateLog("INFO", "kyRemoveLineBreak", "", output_string)
        return output_string

    def kySearchString(input_string,sub_string):
        result = input_string.find(sub_string)
        if result == -1:
            output_string = False
        else:
            output_string = True
        LogGen.updateLog("INFO", "kySearchString", input_string+" subString: "+ sub_string, output_string)
        return output_string