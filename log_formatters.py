import logging


class MyFormatter(logging.Formatter):
    def format(self, record):
        record.unique_id = record.args['unique_id']

        return super().format(record)
