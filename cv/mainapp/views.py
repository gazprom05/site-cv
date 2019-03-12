from django.shortcuts import render


# Create your views here.
def index(request):
    edu_agency = [
        {
            'edu_agency_picture': 'img/education/393_logo.png',
            'edu_agency_name': 'ГБОУ Лицей №393',
            'edu_agency_years': '2004 - 2008',
        },
        {
            'edu_agency_picture': 'img / education / politeh_logo.jpg',
            'edu_agency_name': 'Санкт-Петербургский Государственный Политехнический университет',
            'edu_agency_years': '2008 - 2013',
        },
        {
            'edu_agency_picture': 'img/education/geekbrains_logo.jpg',
            'edu_agency_name': 'Образовательный портал Geekbrains',
            'edu_agency_years': '2018 - 2019',
        },
    ]

    context = {
        'title': 'смолкин дмитрий',
        'edu_agency': edu_agency,
    }
    return render(request, 'mainapp/index.html', context)


def error(request):
    context = {
        'title': 'error',
    }
    return render(request, 'mainapp/error.html', context)
