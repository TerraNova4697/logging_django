


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': "Главная страница",
    }
    
    log_view('Short warning', context2, 'INFO')
    
    return render(request, 'project/index.html', context=context)