# logging_django

1) Добавить директорию logs/ в корень проекта
2) Добавить файлы log_handlers.py, view_logger.py, log_filters.py, response_log_middleware.py
3) Добавить ResponseLogMiddleware в конец списка миддлварей проекта
4) В settings.py добавить конфигурацию логов из файла settings.py текущего репозитория
5) В словаре LOGGING внутри проекта импортировать нужные классы (указаны комментарии)

Чтобы логгировать данные из view:

def index(request):
  posts = Post.objects.all()
  context = {
    'posts': posts,
    'title': "Главная страница",
   }
   
   log_view('Short warning', context2, 'INFO')
   
   return render(request, 'project/index.html', context=context)
   
  
