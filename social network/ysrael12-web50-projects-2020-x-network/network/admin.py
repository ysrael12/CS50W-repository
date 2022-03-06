from django.contrib import admin

# importaçao do models
from .models import User, Follow, Post, Like

# propiedades do model para o  admin

admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Like)