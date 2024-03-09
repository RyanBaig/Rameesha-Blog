from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    first_head = models.CharField(default='', max_length=500)
    first_head_content = models.TextField(default='', max_length=5000)

    second_head = models.CharField(default='', max_length=500)
    second_head_content = models.TextField(default="", max_length=5000)

    third_head = models.CharField(default='', max_length=500)
    third_head_content = models.TextField(default="", max_length=5000)

    fourth_head = models.CharField(default="", max_length=500, blank=True)
    fourth_head_content = models.TextField(default="", max_length=5000, blank=True)

    fifth_head = models.CharField(default="", max_length=500, blank=True)
    fifth_head_content = models.TextField(default="", max_length=5000, blank=True)

    sixth_head = models.CharField(default="", max_length=500, blank=True)
    sixth_head_content = models.TextField(default="", max_length=5000, blank=True)

    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return self.title
