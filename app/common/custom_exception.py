import sys

class CustomException(Exception):
    def __init__(self,message: str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, exec_tb = sys.exc_info()
        file_name = exec_tb.tb_frame.f_code.co_filename if exec_tb else "Unknown File"
        line_number = exec_tb.tb_lineno if exec_tb else "Unknown line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"
    
    def __str__(self):
        return self.error_message