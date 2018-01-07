from django.shortcuts import render

LIST = (
    {'title': 'Item One', 'itemIsChecked': False},
    {'title': 'Item Two', 'itemIsChecked': False},
    {'title': 'Item Three', 'itemIsChecked': False},
    {'title': 'Item Four', 'itemIsChecked': False},
    {'title': 'Item Five', 'itemIsChecked': False},
)


def home(request):
    list = LIST
    return render(request, 'mylist/home.html', {'list': list})
