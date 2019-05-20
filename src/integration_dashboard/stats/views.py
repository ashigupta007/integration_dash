from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from .models import DailyCrashReport
import datetime
import sqlite3
import json
# from .read_curr_db.py import get_db_status

# Create your views here.

def home_view(request):
	return render(request, "index.html",{})
def stats_view(request):
	num_lines=0
	with open('/Users/ashish/documents/projects/integration_dashboard/src/integration_dashboard/static/log_file.log', 'r') as f:
		for line in f:
			num_lines += 1
	if num_lines <= 5:
		system_status = 'Healthy'
	elif num_lines >= 6:
		system_status = 'Down'
	elif num_lines >20:
		system_status = 'Critical'
	dateEpoch = datetime.datetime.now()
	currDate= dateEpoch.strftime("%d:%m:%Y")
	crashData = DailyCrashReport.objects.all()
	crash_per_day =[]
	crash_dates =[]
	for items in crashData:
		crash_per_day.append(items.noofcrashes)
		crash_dates.append(items.reportdate)
	return render(request, "stats.html", {'crashes': num_lines, 'system_status': system_status, 'crash_data': crash_per_day, 'crash_dates' : crash_dates})
def raw_file_view(request):
	conn=sqlite3.connect('/Users/ashish/documents/projects/integration_dashboard/src/integration_dashboard/ControlTable.db')
	c = conn.cursor()
	x=c.execute ('SELECT * FROM  controlSheet')
	rows = json.dumps(c.fetchall())

	return render(request, "raw_file_view.html", {'table_data' : rows})