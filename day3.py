from datetime import datetime
input_date = "01-03-2025"
var_date = datetime.strptime(input_date,"%d-%m-%Y")

month_number = var_date.month
month_code = f"M{month_number}"

Week_number = var_date.isocalendar()[1]
week_code = f"W{Week_number}"


print("Month code:", month_code)
print("Week code:", week_code)

#2nd method

if input_date == "01-01-2025":
    month_code = "M1"
elif input_date == "01-02-2025":
    month_code = "M2"
elif input_date == "01-03-2025":
     month_code = "M3"
elif input_date == "01-04-2025":
     month_code = "M4"
else:
     Month_code = "Unknown month code"

#weeks

if input_date == "01-01-2025":
    week_code = "W1"
elif input_date == "01-02-2025":
    week_code = "W5"
elif input_date == "01-03-2025":
     week_code = "W9"
elif input_date == "01-04-2025":
     week_code = "W17"
else:
     week_code = "Unknown month code"



print("month code:", month_code)
print("week code:", week_code)