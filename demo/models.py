from django.db import models

# Create your models here.
class Profile(models.Model):
	name_of_the_board = models.CharField(max_length=150)
	allcategory_boys = models.CharField(max_length=150)
	allcategory_girls = models.CharField(max_length=150)
	allcategory_total = models.CharField(max_length=150)
	allcategory_passed_boys = models.CharField(max_length=150)
	allcategory_passed_girls = models.CharField(max_length=150)
	allcategory_passed_total = models.CharField(max_length=150)
	schedulecaste_boys = models.CharField(max_length=150)
	schedulecaste_girls = models.CharField(max_length=150)
	schedulecaste_total = models.CharField(max_length=150)
	schedulecaste_passed_boys = models.CharField(max_length=150)
	schedulecaste_passed_girls = models.CharField(max_length=150)
	schedulecaste_passed_total = models.CharField(max_length=150)
	scheduletribe_boys = models.CharField(max_length=150)
	scheduletribe_girls = models.CharField(max_length=150)
	scheduletribe_total = models.CharField(max_length=150)
	scheduletribe_passed_boys = models.CharField(max_length=150)
	scheduletribe_passed_girls = models.CharField(max_length=150)
	scheduletribe_passed_total = models.CharField(max_length=150)


 
    

	
		