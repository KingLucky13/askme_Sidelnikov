from django.contrib import admin

from app.models import Profile, Tag, Question, Answer

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
