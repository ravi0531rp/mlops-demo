import sys
import logger
import logging


def error_message_detail(error, error_detail: sys) -> str:
    """Return the error message in detail

    Args:
        error (_type_): _description_
        error_detail (sys): _description_

    Returns:
        str: _description_
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Error occured in Python script named [{file_name}] line number [{line_no}] error message [{str(error)}]"
    return error_message


class CustomException(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, error, error_detail: sys) -> None:
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Divide by Zero..")
        raise CustomException(e, sys)
