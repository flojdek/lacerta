from django.shortcuts import render_to_response
from django.http import Http404

def index(request, type):
	dict = {"page" : "oferta"}
	if type == "edukacja":
		dict["subpage"] = "edukacja"
		return render_to_response('edukacja.html', dict)
	elif type == "wnioski":
		dict["subpage"] = "wnioski"
		return render_to_response('wnioski.html', dict)
	elif type == "ekspertyzy":
		dict["subpage"] = "ekspertyzy"
		return render_to_response('ekspertyzy.html', dict)
	elif type == "":
		return render_to_response('oferta.html', dict)
	else:
		raise Http404
