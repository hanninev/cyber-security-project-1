from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.views.decorators.csrf import csrf_exempt
import sqlite3

def homePageView(request):
	members = Member.objects.all()
	if 'member' in request.session:
		member = Member.objects.filter(id=request.session['member'])
		return render(request, 'pages/index.html', {'member': member[0], 'members': members})
	return render(request, 'pages/index.html', {'members': members})

def loginAction(request): 
	email = request.POST['email']
	password = request.POST['password']

	conn = sqlite3.connect('db.sqlite3')
	cursor = conn.cursor()
	response = cursor.execute("SELECT id FROM register_member WHERE email='%s' and password='%s'" % (email, password)).fetchall()

	id = ''
	if len(response) > 0:
		id = response[0][0]
		member = Member.objects.filter(id=id)

		if member:
			response = render(request, 'pages/member_update_form.html', {'member': member[0]})
			request.session['member'] = member[0].id
			return response
	return redirect('/')

def reqisterAction(request):

	member = Member.objects.create(img_url=request.POST['img_url'], name=request.POST['name'], address=request.POST['address'], email=request.POST['email'], password=request.POST['password'], general=request.POST['general'])
	member.save()

	request.session['member'] = member.id

	return redirect('/')

def editView(request, memberid): 
	member = Member.objects.get(id=memberid)
	return render(request, 'pages/member_update_form.html', {'member': member})

def editAction(request):
	member = Member.objects.filter(id=request.session['member'])[0]
	member.name = request.POST['name']
	member.address = request.POST['address']
	member.email = request.POST['email']
	member.password = request.POST['password']
	member.general = request.POST['general']
	member.img_url = request.POST['img_url']
	member.save()

	return redirect('/')

