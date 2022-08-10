from django.contrib import admin

from .models import *


class AnswerInLine(admin.TabularInline):
    model = Answer
    min_num = 4
    max_num = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine,]


admin.site.register(Group)
admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)
