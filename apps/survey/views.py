from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, 'survey/index.html')

def process(request):
	if "count" not in request.session:
		request.session["count"] = 1

	request.session['first_name'] = request.POST['first_name']	
	request.session['last_name'] = request.POST['last_name']
	request.session['location'] = request.POST['location']	
	request.session['language'] = request.POST['language']
	request.session['comments'] = request.POST['comments']			
	request.session["count"] += 1
	return redirect('/results')

def results(request):
	return render(request, 'survey/results.html') 


