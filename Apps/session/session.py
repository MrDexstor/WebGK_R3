from Lib.UI import render, Page

def login(request):
    page = Page('Авторизация WGK', '')
    return render(request, page, 'session/login.html', accept_level='guest')