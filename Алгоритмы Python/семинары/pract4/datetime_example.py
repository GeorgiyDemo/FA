import datetime

date = datetime.datetime.now().date().strftime("%d.%m.%Y")
FIRST_DATE = date+" 08:15"
SECOND = "30"
print(datetime.datetime.now().date())
FIRST_OBJ = datetime.datetime.strptime(FIRST_DATE, "%d.%m.%Y %H:%M")
print(FIRST_OBJ)
RESULT = FIRST_OBJ + datetime.timedelta(0,0,0,0,3) # days, seconds, then other fields.
print(RESULT)


#SECOND_OBJ = datetime.datetime.strptime(SECOND, "%M")
#print(SECOND_OBJ)

