from django.contrib import admin

# Register your models here.



from .models import  Work, OurStory, CoreValue, Program, TeamMember

admin.site.register(Work)
admin.site.register(OurStory)
admin.site.register(CoreValue)
admin.site.register(Program)
admin.site.register(TeamMember)


