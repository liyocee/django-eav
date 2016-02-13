from django.contrib import admin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
from .models import Library, Book


class BookAdminForm(BaseDynamicEntityForm):
    # create  custom form to show eav eav attributes when adding a book
    model = Book


class BookAdmin(BaseEntityAdmin):
    form = BookAdminForm

admin.site.register(Library)
admin.site.register(Book, BookAdmin)
