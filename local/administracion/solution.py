from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from my_app.forms import CustomForm


class FakeModel(object):
    class _meta:
        app_label = 'my_app'  # This is the app that the form will exist under
        model_name = 'custom-form'  # This is what will be used in the link url
        verbose_name_plural = 'Custom AdminForm'  # This is the name used in the link text
        object_name = 'ObjectName'

        swapped = False
        abstract = False


class MyCustomAdminForm(admin.ModelAdmin):
    """
    This is a funky way to register a regular view with the Django Admin.
    """

    def has_add_permission(*args, **kwargs):
        return False

    def has_change_permission(*args, **kwargs):
        return True

    def has_delete_permission(*args, **kwargs):
        return False

    def changelist_view(self, request):
        context = {'title': 'My Custom AdminForm'}
        if request.method == 'POST':
            form = CustomForm(request.POST)
            if form.is_valid():
                # Do your magic with the completed form data.

                # Let the user know that form was submitted.
                messages.success(request, 'Congrats, form submitted!')
                return HttpResponseRedirect('')
            else:
                messages.error(
                    request, 'Please correct the error below'
                )

        else:
            form = CustomForm()

        context['form'] = form
        return render(request, 'admin/change_form.html', context)


admin.site.register([FakeModel], MyCustomAdminForm)

from django import forms


class CustomForm(forms.Form):