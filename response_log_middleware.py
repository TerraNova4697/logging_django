
import logging

logger = logging.getLogger('main')


class ResponseLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if 400 <= response.status_code < 500:
            logger.warning(f'Response headers: {response.headers}')
            logger.warning(f'Response status_code: {response.status_code}')
            logger.warning(f'Response reason_phrase: {response.reason_phrase}')
        elif response.status_code >= 500:
            logger.error(f'Response headers: {response.headers}')
            logger.error(f'Response status_code: {response.status_code}')
            logger.error(f'Response reason_phrase: {response.reason_phrase}')
        else:
            logger.info(f'Response headers: {response.headers}')
            logger.info(f'Response status_code: {response.status_code}')
            logger.info(f'Response reason_phrase: {response.reason_phrase}')

        return response
