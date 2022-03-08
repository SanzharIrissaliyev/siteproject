from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=300)
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class AboutCount(models.Model):
    title = models.CharField(max_length=300)
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='upload')
    mini_description = models.CharField(max_length=300)
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Count(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    rating = models.IntegerField(default=0, blank=True)
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    pinterest = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='upload')
    date = models.DateTimeField(blank=True)
    view = models.IntegerField(default=0, blank=True)
    comment = models.TextField(blank=True)
    status = models.IntegerField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Information(models.Model):
    title = models.CharField(blank=True, max_length=300)

    # info = models.CharField(blank=True)
    # info_text = models.CharField(blank=True)
    #
    # info3 = models.CharField(blank=True)
    # info3_text = models.CharField(blank=True)
    # info3_description = models.CharField(blank=True)
    #
    # info4 = models.CharField(blank=True)
    # info4_text = models.CharField(blank=True)

    status = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title