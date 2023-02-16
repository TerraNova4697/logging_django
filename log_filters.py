import logging


class ErrorOnlyFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname == 'ERROR'


class WarningOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'WARNING'


class InfoOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'INFO'


class DebugOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'DEBUG'
