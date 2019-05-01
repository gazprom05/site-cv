from django.shortcuts import render
from mainapp.models import MenuCategoryTable, EducationTable, CareerTable, AddEducationTable, CertificatesTable
import requests
import json
import time

# Create your views here.
def index(request):
    def get_api():
        get_xml = requests.get(
            'https://www.cbr-xml-daily.ru/daily_json.js')
        if get_xml.status_code == 200:
            print('Все в норме!')
        if get_xml.status_code == 404:
            print('Страница не существует!')

        response = json.loads(get_xml.text)
        usd = response['Valute']['USD']['Value']
        eur = response['Valute']['EUR']['Value']
        date = time.strftime("%d.%m.%y:", time.localtime())
        return usd, eur, date

    usd, eur, date = get_api()


    menucategory_table = MenuCategoryTable.objects.all()
    education_table = EducationTable.objects.all()
    career_table = CareerTable.objects.all()
    addeducation_table = AddEducationTable.objects.all()
    certificates_table = CertificatesTable.objects.all()

    edu_agency = [
        {
            'edu_agency_logo': 'static/img/education/393_logo.jpg',
            'edu_agency_name': 'ГБОУ Лицей №393',
            'edu_agency_years': '2004 - 2008',
        },
        {
            'edu_agency_logo': 'static/img/education/politeh_logo.jpg',
            'edu_agency_name': 'Санкт-Петербургский Государственный Политехнический университет',
            'edu_agency_years': '2008 - 2013',
        },
        {
            'edu_agency_logo': 'static/img/education/geekbrains_logo.jpg',
            'edu_agency_name': 'Образовательный портал Geekbrains',
            'edu_agency_years': '2018 - 2019',
        },
    ]

    career = [
        {
            'company_name': '"Компания Эдвенче"',
            'company_logo': 'static/img/career/logo-aero.png',
            'company_position': 'Конструктор',
            'company_years': '2013 - 2015',
        },
        {
            'company_name': 'Электронная компания "Элкус"',
            'company_logo': 'static/img/career/elkus.jpg',
            'company_position': 'Инженер-конструктор',
            'company_years': '2015 - 2019',
        },
    ]

    add_education = [
        {
            'add_education_text':'SolidCAM — инструмент быстрого и легкого создания управляющих программ для токарных, фрезерных и фрезерно-токарных станков с ЧПУ.',
            'add_education_logo':'static/img/add_edu/solidcam.jpg',
            'add_education_year':'2015',

        },
        {
            'add_education_text': 'SolidWorks Enterprise PDM — корпоративная система управления данными и процессами на различных этапах жизненного цикла изделия.',
            'add_education_logo': 'static/img/add_edu/pdm.jpg',
            'add_education_year': '2016',

        },
    ]

    certificates = [
        {
            'certificate_name': 'Основы программирования',
            'certificate_img': 'static/img/certificates/osnovy_progr.jpg',
        },
        {
            'certificate_name': 'Python. Быстрый старт',
            'certificate_img': 'static/img/certificates/python_quick_start.jpg',
        },
        {
            'certificate_name': 'Основы языка Python',
            'certificate_img': 'static/img/certificates/python_osnovy.jpg',
        },
        {
            'certificate_name': 'HTML/CSS',
            'certificate_img': 'static/img/certificates/html_css.jpg',
        },
        {
            'certificate_name': 'Основы баз данных',
            'certificate_img': 'static/img/certificates/osnovy_db.jpg',
        },
        {
            'certificate_name': 'Django',
            'certificate_img': 'static/img/certificates/django.jpg',
        },
        {
            'certificate_name': 'Алгоритмы и структуры данных на Python',
            'certificate_img': 'static/img/certificates/algorithm.jpg',
        },
    ]

    context = {
        'title': 'смолкин дмитрий',
        'edu_agency': edu_agency,
        'career': career,
        'add_education': add_education,
        'certificates': certificates,
        'menucategory_table': menucategory_table,
        'education_table': education_table,
        'career_table': career_table,
        'addeducation_table': addeducation_table,
        'certificates_table': certificates_table,
        'usd': usd,
        'eur': eur,
        'date': date,
    }
    return render(request, 'mainapp/index.html', context)



def error(request):
    context = {
        'title': 'error',
    }
    return render(request, 'mainapp/error.html', context)