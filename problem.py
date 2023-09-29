#24
#find the season by giving date as montha and day
month=input("enter the month:")
day=input("enter the day")

if month in ("january ","feb","mar"):
    season="winter"
elif month in ("april","may","june"):
    season="spring"
elif month in ("july","august","sep"):
    season="summer"
else:
    season="autumn"
if month=="mar" and day >19:
    season="spring"
elif month=="june" and day>20:
    season="summer"
elif month =="sep" and day> 21:
    season="autumn"
elif month =="dec" and day >20:
    season="winter"
print("season is ",season)
