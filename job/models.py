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

class SotsCandidate(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated'),
    ]
    first_name = models.CharField(max_length=100)  # Store first names up to 100 characters
    candidate_id = models.CharField(max_length=50, unique=True)
    roles = models.TextField()# Unique ID for each candidate
    status = models.CharField(max_length=10, null=True, blank=True,choices=STATUS_CHOICES)# active/inactive for each candidate
    display_summary = models.TextField(max_length=250)  # Short summary of 250 characters
    years_of_experience = models.PositiveIntegerField()  # Non-negative integer for years of experience
    current_location = models.CharField(max_length=100)  # Store current location up to 100 characters
    work_mode = models.CharField(max_length=50)  # Type of work (e.g., full-time, part-time)
    work_type = models.CharField(max_length=50)  # Additional type field
    hard_skills = models.TextField()  # Store hard skills in a long text field
    soft_skills = models.TextField()  # Store soft skills in a long text field
    tools = models.TextField()  # Tools the candidate is familiar with
    tag = models.TextField()  # Tools the candidate is familiar with
    experience_summary = models.TextField()  # Detailed experience summary
    educational_summary = models.TextField()  # Educational background summary
    certifications = models.TextField()  # List of certifications
    additional_note = models.TextField(blank=True, null=True)  # Optional additional notes

    def __str__(self):
        return f'{self.first_name} ({self.candidate_id})'

