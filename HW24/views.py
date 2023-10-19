# Импортируем необходимые классы
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Item  # Убедитесь, что импортировали свою модель

def item_list(request):
    # Получаем все объекты (предметы)
    object_list = Item.objects.all()

    # Создаем объект Paginator, в этом примере мы показываем 10 объектов на странице
    paginator = Paginator(object_list, 10)

    # Получаем номер страницы из запроса GET
    page = request.GET.get('page')

    try:
        # Пытаемся получить объекты для запрошенной страницы
        items = paginator.page(page)
    except PageNotAnInteger:
        # Если номер страницы не является целым числом, показываем первую страницу
        items = paginator.page(1)
    except EmptyPage:
        # Если номер страницы больше максимального количества страниц, показываем последнюю
        items = paginator.page(paginator.num_pages)

    # Передаем страницу с объектами в контекст шаблона
    context = {'items': items}

    # Рендерим шаблон с переданным контекстом
    return render(request, 'HW24/item_list.html', context)
