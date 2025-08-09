def month_to_season(number_month):
 if number_month == 1 or number_month == 2 or number_month == 12:
   return ("зима")
 elif number_month == 3 or number_month == 4 or number_month == 5:
  return("весна")
 elif number_month == 6 or number_month == 7 or number_month == 8:
  return("лето")
 elif number_month == 9 or number_month == 10 or number_month == 11:
  return("осень")
print(month_to_season(int(input("введите номер месяца:"))))