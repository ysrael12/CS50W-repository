from django.contrib import admin

# lembrar da anotaçao notion 1
from .models import User, Email

admin.site.register(User)
admin.site.register(Email)