from django.db import models


class User(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    candidate_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    experience_summary = models.TextField(null=True, blank=True)
    responsibilities_summary = models.TextField(null=True, blank=True)
    current_role = models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    work_mode = models.CharField(max_length=50, null=True, blank=True)
    work_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    user = models.ForeignKey(User, related_name='roles', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Certification(models.Model):
    user = models.ForeignKey(User, related_name='certifications', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class HardSkill(models.Model):
    user = models.ForeignKey(User, related_name='hard_skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    user = models.ForeignKey(User, related_name='soft_skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class ToolAndTechnology(models.Model):
    user = models.ForeignKey(User, related_name='tools_and_technologies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    user = models.ForeignKey(User, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    completion_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.university}"



