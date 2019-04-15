def is_leaf_year(year):
	return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def is_valid(day, month, year):
	days = [31, 29 if is_leaf_year(year) else 28, 31,
			30, 31, 30, 31,
			30, 31, 30, 31]
	
	return day >= 1 and day <= days[month-1] and month >= 1 and month <= 12 

while(True):
	day,month,year=map(int, input().split())
	if day == 0 and month == 0 and year == 0:
		break
	print("Valid" if is_valid(day,month,year) else "Invalid")
