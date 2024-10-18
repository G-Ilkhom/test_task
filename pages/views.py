from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.decorators import api_view
from pages.models import Page
from pages.services import parse_page


@api_view(["POST"])
def create_page(request):
    url = request.data.get("url")
    if not url:
        return JsonResponse({"Error": "URL-адрес обязателен"}, status=400)

    title, subtitle, content, links = parse_page(url)

    page = Page.objects.create(
        url=url, title=title, subtitle=subtitle, content=content, links=links
    )

    return JsonResponse({"id": page.id}, status=201)


@api_view(["GET"])
def get_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        response_data = {
            "h1": page.title,
            "h2": page.subtitle,
            "h3": page.content,
            "a": page.links,
        }
        return JsonResponse(response_data)
    except ObjectDoesNotExist:
        return JsonResponse({"Error": "Страница не найдена"}, status=404)


@api_view(["GET"])
def list_page(request):
    order = request.GET.get("order", None)

    if order:
        if order not in ["h1", "h2", "h3", "-h1", "-h2", "-h3"]:
            return JsonResponse({"Error": "Неверный параметр заказа"}, status=400)

        if order.startswith("-"):
            order_by = order[1:]
            pages = Page.objects.all().order_by(f"-{order_by}")
        else:
            pages = Page.objects.all().order_by(order)
    else:
        pages = Page.objects.all().order_by("created_at")

    response_data = [
        {
            "id": page.id,
            "url": page.url,
            "h1": page.title,
            "h2": page.subtitle,
            "h3": page.content,
            "a": page.links,
        }
        for page in pages
    ]

    return JsonResponse(response_data, safe=False)
