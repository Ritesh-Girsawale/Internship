from django.db import models

# Create your models here.


class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('moderator', 'Moderator'),  # Add more roles as needed
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, null=False)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Work(models.Model):
    Cat = 'education'
    image = models.ImageField(upload_to='image', default='image/default.jpg')
    info = models.TextField(verbose_name="Details", default="ww")
    info2 = models.TextField(verbose_name="Details", default="ww")    
    title = models.CharField(max_length=200, verbose_name="Title", default="ww")







# Model for "Our Story"
class OurStory(models.Model):
    content = models.TextField()  # Content of the story
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the story was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the story was last updated

    def __str__(self):
        return f"Our Story (Last Updated: {self.updated_at})"

# Model for "Core Values"
class CoreValue(models.Model):
    value = models.CharField(max_length=255)  # A single core value (e.g., Integrity)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the core value was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the core value was last updated

    def __str__(self):
        return self.value

# Model for "Programs"
class Program(models.Model):
    name = models.CharField(max_length=255)  # Name of the program (e.g., Ujjwal Bhavishya)
    description = models.TextField(null=True, blank=True)  # Detailed description of the program (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the program was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the program was last updated

    def __str__(self):
        return self.name

# Model for "Team Members"
class TeamMember(models.Model):
    name = models.CharField(max_length=255)  # Full name of the team member
    role = models.CharField(max_length=255)  # Role or designation of the team member (e.g., Founder)
    image_url = models.URLField(null=True, blank=True)  # URL or path to the team member's photo (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the team member was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the team member was last updated

    def __str__(self):
        return f"{self.name} - {self.role}"

    
class Project(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Upcoming', 'Upcoming'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image_url = models.CharField(max_length=255)  # Or use models.ImageField() if you're using media uploads
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.project.title}"




class PressRelease(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MediaCoverage(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=2083)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='image')
    description = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description or "Gallery Image"
