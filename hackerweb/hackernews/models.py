from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length = 300)
	link = models.CharField(max_length = 300)

	def __str__(self):
		return u'%s' % self.title
