# logging_django

1) Добавить директорию logs/ в корень проекта
2) Добавить файлы log_handlers.py, view_logger.py, log_filters.py, response_log_middleware.py
3) Добавить ResponseLogMiddleware в конец списка миддлварей проекта
4) В settings.py добавить конфигурацию логов из файла settings.py текущего репозитория
5) В словаре LOGGING внутри проекта импортировать нужные классы (указаны комментарии)

Привет как логгировать данные из views см. пример внутри файла views.py 
   
  
