from django.contrib import admin

from accounts.models import CustomUser
# from quizzes.models import *

# class UserAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name', 'group', 'rating_place')

@admin.register(CustomUser)
class User(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        'phone_number',
        'group',
        'email',
        'rating_place',
        'overall_points',
    )

    list_filter = [
        'first_name',
        'last_name',
        'phone_number'
    ]
