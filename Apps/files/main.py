from Lib.UI import render, redirect, Page
from .forms import UploadFileForm
from Core.config import FS_DIR


def board(request):
    page = Page('Файлы', 'Файлы', 'Менеджер загруженых файлов')
    page.returnUrl('/GK/menu/tools/')
    return render(request, page, 'files/main.html')


def handle_uploaded_file(f, filename):
    with open(FS_DIR/filename, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST)
        if True:
            handle_uploaded_file(request.FILES["file"], request.POST['title'])
            #Сохранить запись 
            return redirect("/GK/files/")
    else:
        form = UploadFileForm()
        page = Page('Загрузка файла', 'Загрузка файла', 'Выгрузка файла на сервер WGK')
        page.returnUrl('/GK/files/')
    return render(request, page,  "files/upload.html", {"form": form})