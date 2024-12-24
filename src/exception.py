import sys

def error_message_detail(error, error_details: sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] Line Number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno, str(error)        
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detial:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail (error= error_message, error_details= error_detial)
        
    def __str__(self):
        return self.error_message
