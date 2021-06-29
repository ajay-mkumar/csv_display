from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Profile
import io,csv
# Create your views here.

def profile_upload(request):

	if request.method == 'GET':
		context={
		'profiles':Profile.objects.all()
		}
		return render (request,'home.html')
	
	csvfile = request.FILES['file']


	file_data = csvfile.read().decode("utf-8")	

	io_string = io.StringIO(file_data)
	next(io_string)

	for column in csv.reader(io_string, delimiter=','):
		_, created = Profile.objects.update_or_create(
			name_of_the_board = column[0],
			allcategory_boys = column[1],
			allcategory_girls = column[2],
			allcategory_total = column[3],
			allcategory_passed_boys = column[4],
			allcategory_passed_girls = column[5],
			allcategory_passed_total = column[6],
			schedulecaste_boys = column[7],
			schedulecaste_girls = column[8],
			schedulecaste_total = column[9],
			schedulecaste_passed_boys = column[10],
			schedulecaste_passed_girls = column[11],
			schedulecaste_passed_total = column[12],
			scheduletribe_boys =column[13],
			scheduletribe_girls = column[14],
			scheduletribe_total = column[15],
			scheduletribe_passed_boys = column[16],
			scheduletribe_passed_girls = column[17],
			scheduletribe_passed_total = column[18],
			)

	context={
	'profiles':Profile.objects.all()
	}
	return render (request,'home.html',context)



