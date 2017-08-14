from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Marks, Models, Series, Modification
from django.core.mail import send_mail


def main(request):
    page = 'main'
    return render(request, 'index.html', {'page': page})


def catalog(request):
    page = 'catalog'
    marks = Marks.objects.all()
    context = {'page': page, 'marks': marks}
    return render(request, 'catalog.html', context)


def models(request, mark_id):
    models = Models.objects.filter(mark__id=mark_id)
    mark_name = models[0].mark.name
    context = {'models': models, 'mark_name': mark_name}
    return render(request, 'models.html', context)


def series(request, model_id):
    series = Series.objects.filter(model__id=model_id)
    car_model = series[0].mark.id
    mark_name = series[0].mark.name
    context = {'series': series, 'car_model': car_model, 'mark_name': mark_name}
    return render(request, 'series.html', context)


def modifications(request, series_id):
    modification = Modification.objects.filter(series__id=series_id)
    car_series = modification[0].model.id
    mark_name = modification[0].mark.name
    model_name = modification[0].model.name
    context = {'modification': modification, 'car_series': car_series,
               'mark_name': mark_name, 'model_name': model_name}
    return render(request, 'modification.html', context)


def shares(request):
    page = 'shares'
    return render(request, 'shares.html', {'page': page})


def delivery(request):
    page = 'delivery'
    return render(request, 'delivery.html', {'page': page})


def guarantees(request):
    page = 'guarantees'
    return render(request, 'guarantees.html', {'page': page})


def contacts(request):
    page = 'contacts'
    return render(request, 'contacts.html', {'page': page})


def applications_form(request, car_id):
    if request.method == 'POST':
        car_mark = request.POST.get('car_mark')
        car_model = request.POST.get('car_model')
        car_series = request.POST.get('car_series')
        car_modification = request.POST.get('car_modification')
        car_power = request.POST.get('car_power')
        car_year = request.POST.get('car_years_of_issue')
        car_vin = request.POST.get('car_vin')
        details = request.POST.get('requested_details')
        name = request.POST.get('user_name')
        contact = request.POST.get('user_phone_or_email')

        subject = '43 ДЕТАЛИ - запрос с основной формы'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, settings.MAIN_EMAIL]
        contact_message = '''
        Запрос от......... {}
        Тел.(email)....... {}
        Марка............. {}
        Модель............ {}
        Серия............. {}
        Модификация....... {}
        Мощность (л.с.)... {}
        Год выпуска....... {}
        VIN............... {}
        Детали............ {}
        '''.format(name, contact, car_mark, car_model,
                   car_series, car_modification, car_power, car_year,
                   car_vin, details)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        return HttpResponseRedirect('/sent/')
    else:
        application = Modification.objects.get(id=car_id)
        return render(request, 'applications_form.html', {'application': application})


def aside_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('phone')
        car = request.POST.get('car')
        parts = request.POST.get('parts')

        subject = '43 ДЕТАЛИ - запрос с боковой формы'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, settings.MAIN_EMAIL]
        contact_message = '''
                Запрос от......... {}
                Тел.(email)....... {}
                Автомобиль........ {}
                Детали............ {}
                '''.format(name, contact, car, parts)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        return HttpResponseRedirect('/sent/')
    else:
        return render(request, 'index.html')

def sent(request):
    return render(request, 'sent.html')