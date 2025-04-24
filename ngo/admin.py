from django.contrib import admin

# Register your models here.



from .models import  Work, OurStory, CoreValue, Program, TeamMember, Project, ProjectImage, PressRelease, MediaCoverage, ImageGallery

admin.site.register(Work)
admin.site.register(OurStory)
admin.site.register(CoreValue)
admin.site.register(Program)
admin.site.register(TeamMember)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(PressRelease)
admin.site.register(MediaCoverage)
admin.site.register(ImageGallery)


