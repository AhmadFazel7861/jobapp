
from django.contrib import admin

from app.models import Author, JobPost, Location, Skills

class JobAmin(admin.ModelAdmin):
    list_display = ('title','date','salary','location','author')
    list_filter = ('date','salary','expiry','location','author','skills')
    search_fields = ['title']
    search_help_text = "Write in your query and hit enter"
    # fields = (('title','description'),'expiry')
    # exclude = ('title',)
    fieldsets = (
        ('Basic information', {
            "fields": ('title', 'description')
        }),
        ('More information', {
        'classes':('collapse',),
            "fields": (('salary', 'expiry'),'location','author','skills','slug', 'type')
        }),
    )
    # (name, field_option)
# Register your models here.
admin.site.register(JobPost,JobAmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
