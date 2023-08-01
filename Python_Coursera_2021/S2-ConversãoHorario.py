segundos = input("Por favor, entre com o número de segundos que deseja converter:")
segund_total = int(segundos)

dias_total = segund_total // 86400
dias_sobra = segund_total % 86400
horas_total = dias_sobra // 3600
horas_sobra = dias_sobra % 3600
minutos_total = horas_sobra // 60
segundos_total = horas_sobra % 60

print(dias_total,"dias,", horas_total, "horas,", minutos_total,"minutos e", segundos_total, "segundos.")
