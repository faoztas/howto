from markdownx.admin import MarkdownxModelAdmin
from django.contrib import admin
from .models import Person, Post, Question, Answer, Topic, Comment, ContentType
from draceditor.widgets import AdminDraceditorWidget
from django.db import models

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(ContentType)

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }

admin.site.register(Post, PostAdmin)
# Register your models here.
#193441