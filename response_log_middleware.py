
import logging
import uuid

logger = logging.getLogger('http_logger')


class ResponseLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        unique_id = str(uuid.uuid4())
        logger.info(f'Request headers: {request.headers}', {'unique_id': unique_id})

        response = self.get_response(request)

        if 400 <= response.status_code < 500:
            logger.warning(f'Response headers: {response.headers}', {'unique_id': unique_id})
            logger.warning(f'Response status_code: {response.status_code}', {'unique_id': unique_id})
            logger.warning(f'Response reason_phrase: {response.reason_phrase}', {'unique_id': unique_id})
        elif response.status_code >= 500:
            logger.error(f'Response headers: {response.headers}', {'unique_id': unique_id})
            logger.error(f'Response status_code: {response.status_code}', {'unique_id': unique_id})
            logger.error(f'Response reason_phrase: {response.reason_phrase}', {'unique_id': unique_id})
        else:
            logger.info(f'Response headers: {response.headers}', {'unique_id': unique_id})
            logger.info(f'Response status_code: {response.status_code}', {'unique_id': unique_id})
            logger.info(f'Response reason_phrase: {response.reason_phrase}', {'unique_id': unique_id})

        return response

