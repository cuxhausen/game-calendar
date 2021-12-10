from django import forms
from django.contrib.admin import widgets

class SomeForm(forms.Form):
    some_field = forms.SplitDateTimeField(label='Some field',
                                          input_date_formats=['%d.%m.%Y'],
                                          input_time_formats=['%H:%M:%S'],
                                          widget=widgets.AdminSplitDateTime())

    class Media:
        css = {
            'all': (
                 '/static/admin/css/widgets.css',
            )
        }
        js = [
            '/admin/jsi18n/',
            '/static/admin/js/core.js',
        ]