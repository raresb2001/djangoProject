from django.db import models

# Create your models here.

class Trainer(models.Model):
    # (first_name-> charfield(20), last_name -> chardfield(20),
    # course -> charfield(40), email-> emailfield(40), department -> charfield, active -> boolean(default=True),
    # created_at -> datetimefield, updated_at - > datetimefield).
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to="trainer_profiles/", null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def delete(self, *args, **kwargs):
        self.active = False
        return super(Trainer,self).save(*args, **kwargs)