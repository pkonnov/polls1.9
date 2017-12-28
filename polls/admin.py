from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline): #покажите 3 формы для добавления вариантов ответа
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Информация о дате', {'fields': ['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)