import logging

from django.core import serializers
from django.db.models import QuerySet, Model
from math import ceil

import json

logger = logging.getLogger('main')


# message: Сообщение об ошибке. То, что передается в logger. Напр.: logger.warning(msg=message).
# context: Context dictionary.
# level: Уровень ошибки, который передается в logger.
def log_view(message: str, context: dict, level='INFO', ) -> None:
    try:
        json_object = context_serializer(context)
        json_length = len(json_object)
        times = ceil(json_length / 300)
        logger.log(logging.getLevelName(level), msg=message)
        for i in range(0, times):
            print(i)
            start = 300 * i
            end = start + 301
            logger.log(logging.getLevelName(level), msg=json_object[start:end])
    except TypeError as e:
        logger.error(e.__traceback__)


def context_serializer(context: dict) -> str:
    context_to_str = context.copy()
    JSONSerializer = serializers.get_serializer('json')
    json_serializer = JSONSerializer()
    for k, v in context_to_str.items():
        if isinstance(v, QuerySet):
            context_to_str[k] = json_serializer.serialize(v)
        elif isinstance(v, Model):
            context_to_str[k] = json_serializer.serialize([v, ])

    json_object = json.dumps(context_to_str, ensure_ascii=False)
    return json_object