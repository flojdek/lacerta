from django.shortcuts import render_to_response
from django.http import Http404

def index(request, type):
	if type == "edukacja":
		return render_to_response('edukacja.html')
	elif type == "wnioski":
		return render_to_response('wnioski.html')
	elif type == "ekspertyzy":
		return render_to_response('ekspertyzy.html')
	elif type == "":
		return render_to_response('oferta.html')
	else:
		raise Http404
