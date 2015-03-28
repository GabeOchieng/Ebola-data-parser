import sys
import csv

#Calculates the days that have passed since 2014-08-29, the first recorded ebola outbreak in Guinea
def calculate_days(date_str):
	# print 'this is date_str: ', date_str, ' in datecalculation and it\'s a ', type(date_str)
	date = date_str.split('-',2);
	# print 'the date has been split to:', date
	year = int(date[0])
	month = int(date [1])
	day = int(date[2])
	# print 'the date has been converted to integers, and it is:', year, month, day
	# starttime = '2014-08-29'
	time = countback(year, month, day)
	return time
	# print 'Time of this statistic since Ebola outbreak:',time

#counts back the days from the entered parameters until 2014/08/29
#This is used to accurately find the elapsed time, accounting for differences in
#days in different months.
def countback(year, month, day):
	ended = False
	time = 0
	while (not ended):
		if (year==2014):
			if(month==8):
				if(day==29):
					ended = True
					break
		# print 'This is the current loop in countback:', year, month, day
		if(day>1):
			day-=1
		else:
			if (month>1):
				month-=1
			else:
				year -=1
				month = 12
				day = dayinmonth(month)
			day = dayinmonth(month)
		time+=1
	return time


#Returns the days in a given month. The month parameter must be
#an integer, and the 0 in single digit months is optional. (e.g
# for april, enter '08' or '8' without the quotes. For december,
# enter '12' without the quores)
def dayinmonth(month):
	if(month==1):
		return 31
	elif(month==2):
		return 28
	elif(month==3):
		return 31
	elif(month==4):
		return 30
	elif(month==5):
		return 31
	elif(month==6):
		return 30
	elif(month==7):
		return 31
	elif(month==8):
		return 31
	elif(month==9):
		return 30
	elif(month==10):
		return 31
	elif(month==11):
		return 30
	elif(month==12):
		return 31

#Returns the user's choice of a country. The strings that are returned
#should be identical to those in the file the data is extracted from.
def country_choice():
	print 'country_choice() now operating'
	country_num=0
	if(country_num >=1 and country_num<=9):
		print 'True'
	else:
		print 'False'
	while(not (country_num >=1 and country_num<=9)):
		print 'Please enter the number of the country you would like to extract data from'
		print '1. Liberia'
		print '2. Guinea'
		print '3. Sierra Leon'
		print '4. Nigeria'
		print '5. USA'
		print '6. Senegal'
		print '7. Spain'
		print '8. UK'
		print '9. Mali'
		country_num = input('Enter one number here: ')

		if(country_num==1):
			return 'Liberia'
		elif(country_num==2):
			return 'Guinea'
		elif(country_num==3):
			return 'Sierra Leone'
		elif(country_num==4):
			return 'Nigeria'
		elif(country_num==5):
			return 'United States of America'
		elif(country_num==6):
			return 'Senegal'
		elif(country_num==7):
			return 'Spain'
		elif(country_num==8):
			return 'United Kingdom'
		elif(country_num==9):
			return 'Mali'
		else:
			print 'That is not an acceptable number. Please enter a number corresponding to a country.'


#Returns the user's choice of a statistic. The strings that are returned
#should be identical to those in the file the data is extracted from.
def statistic_choice():
	usrinput=0
	while(not(usrinput >=1 and usrinput <=7)):
		print 'Please enter the number of the statistic you would like to extract data from'
		print '1. Cumulative number of confirmed, probable and suspected Ebola cases'
		print '2. Cumulative number of confirmed Ebola cases'
		print '3. Cumulative number of probable Ebola cases'
		print '4. Cumulative number of suspected Ebola cases'
		print '5. Cumulative number of confirmed, probable and suspected Ebola deaths'
		print '6. Cumulative number of confirmed Ebola deaths'
		print '7. Cumulative number of probable Ebola deaths'
		usrinput = input('Enter one number here: ')

		if(usrinput==1):
			return 'Cumulative number of confirmed, probable and suspected Ebola cases'
		elif(usrinput==2):
			return 'Cumulative number of confirmed Ebola cases'
		elif(usrinput==3):
			return 'Cumulative number of probable Ebola cases'
		elif(usrinput==4):
			return 'Cumulative number of suspected Ebola cases'
		elif(usrinput==5):
			return 'Cumulative number of confirmed, probable and suspected Ebola deaths'
		elif(usrinput==6):
			return 'Cumulative number of confirmed Ebola deaths'
		elif(usrinput==7):
			return 'Cumulative number of probable Ebola deaths'
		else:
			print 'That is not a valid entry. Please choose one of the following correct entries'

#The 2 lines bellow can be uncommented to allow for custom file choice
# file_to_read_name = input('Please Enter the file name in which the data is located')
# file_to_read = open(file_to_read_name)
#The line below must be commented out if the filename is going to be customely chosen
file_to_read = open('ebola-data-db-format.csv')

country_to_look_for = country_choice()
statistic_to_look_for = statistic_choice()

country_entries_num = 0

country_entries = []

try:
	reader = csv.reader(file_to_read)
	for row in reader:
		entries = []
		entries += row
		if country_to_look_for in row:
			if 'Cumulative number of confirmed Ebola cases' in row:
				country_entries.append(entries)
				country_entries_num+=1
		
			# print row
			# print '########################'
			# print guinea_entries
			# print '@@@@@@@@@@@@@@@@@@@@@@@@'
		# print row
finally:
	file_to_read.close()


#prints the entries for guinea
print 'there are ', str(country_entries_num), ' entries for ', country_to_look_for
for n in country_entries:
	# print '[\''+n[2]+'\'' + ', \''+n[3]+'\']'
	print n

filename = 'OUTPUT '+country_to_look_for+'-'+statistic_to_look_for
with open(filename, 'wb') as testingdata:
	# datawriter = writer(testingdata)
	# testingdata.write('date, number of confirmed deaths\n')
	for n in country_entries:
		testingdata.write(str(calculate_days(n[2])) + ' ' + n[3] + '\n')
		# print n[2]
		# print  'this is n[2]', n[2], ' in csvreader.py and it is a ', type(n[2])
		# print datecalculation.calculate_days(n[2])



