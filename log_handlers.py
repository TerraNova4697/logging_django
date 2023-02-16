import os.path
from datetime import date
import logging


class NotifyHandler(logging.Handler):

    def emit(self, record):
        level = record.levelname
        asctime = record.asctime
        message = record.getMessage()
        exc_text = record.exc_text if record.exc_text else ''
        message_text = f'{level} {asctime} {message}\n{exc_text}'
        # TODO: Отправить данные в бота


class InfoHandler(logging.FileHandler):

    def __init__(self, filename, log_type):

        dt = date.today()
        directory_path = os.path.join(filename, dt.strftime(f'{log_type}/%Y/%m/%d/'))

        directory_exists = os.path.exists(directory_path)
        if not directory_exists:
            os.makedirs(directory_path)

        filename = os.path.join(directory_path, f'{log_type}.log')

        super().__init__(filename, encoding='utf8')


