from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created', on_delete=models.CASCADE)
    #указывает пользователя, который добавляет изображение в  закладки. Это поле является внешним ключом и использует связь «one to many"
    title = models.CharField(max_length=200) #название изображения
    slug = models.SlugField(max_length=200, blank=True) #html код будет использовать в теге <img>, как атрибут alt.
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/') #ccылка на оригинальное изображение в папку media
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True) #date of upload image to db.
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True) #связь "many to many" между моделями юзер и фото. список пользователей кому понравилось данное изображение.

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
