from django.db import models

# Create your models here.

class Project_Details(models.Model):
    project_name = models.CharField(max_length=255)
    project_fname = models.CharField(max_length=255, null=True, blank=True)
    project_lname = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255)
    date = models.DateField()
    overview = models.CharField(max_length=1000)
    main_image = models.CharField(max_length=10000)
    concept = models.TextField()
    project_type = models.CharField(max_length=255)
    development = models.TextField()
    project_github = models.URLField()

    def __str__(self):
        return self.project_name

