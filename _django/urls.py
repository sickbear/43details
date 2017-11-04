from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from shop_app.views import (main, catalog, models, series,
                            modifications, shares, aside_form,
                            delivery, guarantees, contacts,
                            applications_form, sent)

urlpatterns = [
    url(r'^secret_admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^catalog/$', catalog, name='catalog'),
    url(r'^models/(\d+)/$', models, name='models'),
    url(r'^series/(\d+)/$', series, name='series'),
    url(r'^modifications/(\d+)/$', modifications, name='modifications'),
    url(r'^shares/$', shares, name='shares'),
    url(r'^delivery/$', delivery, name='delivery'),
    url(r'^guarantees/$', guarantees, name='guarantees'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^applications_form/(\d+)/$', applications_form, name='applications_form'),
    url(r'^aside_form/', aside_form, name='aside_form'),
    url(r'^sent/$', sent, name='sent'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)