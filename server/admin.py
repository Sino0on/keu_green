from django.contrib import admin
from django import forms

from .models import *
# Register your models here.

from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Task
        fields = '__all__'


class TaskAdmin(admin.ModelAdmin):
    form = PostAdminForm


class CourseAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Task
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm


class AboutAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = About
        fields = '__all__'


class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm


admin.site.register(Task, TaskAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Fakultet)
admin.site.register(Kafedra)
admin.site.register(Teacher)
admin.site.register(CourseUser)
admin.site.register(Course, CourseAdmin)
admin.site.register(Application)
admin.site.register(Modul)
admin.site.register(About, AboutAdmin)