from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class LevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            level = str(request.POST.get("level"))
            if level == "Ниже Junior":
                return HttpResponseBadRequest(
                    "Пожалуйста, улучшите свои навыки и подайте заявку позже."
                )
            elif level == "Junior":
                request.salary = "700$"
            elif level == "Middle":
                request.salary = "1000$"
            elif level == "Senior":
                request.salary = "2000$"
            else:
                return HttpResponseBadRequest(
                    "Указанный уровень нам не понятен. К сожалению, вы нам не подходите."
                )
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "salary", "Зарплата не определена")
