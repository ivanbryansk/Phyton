# -*- coding: utf-8 -*-

print("Система расчёта штрафов в Германии")

carSpeed = 121
isTown = False

townSpeed = 100
fineFor1to10 = 10
fineFor11to15 = 20
fineFor16to20 = 30
fineFor21to25 = 70
fineFor26to30 = 80
fineFor31to40 = 120
fineFor41to50 = 160
fineFor51to60 = 240
fineFor61to70 = 440
fineFor70andMore = 600

if isTown:
  townSpeed = 50
  fineFor1to10 = 15
  fineFor11to15 = 25
  fineFor16to20 = 35
  fineFor21to25 = 80
  fineFor26to30 = 100
  fineFor31to40 = 160
  fineFor41to50 = 200
  fineFor51to60 = 280
  fineFor61to70 = 480
  fineFor70andMore = 680

overSpeed = carSpeed - townSpeed

if overSpeed < 1:
  print("Скорость не превышена или превышена незначительно")

elif overSpeed >= 1 and overSpeed <= 10:
  print("Штраф: " + str(fineFor1to10) + " евро")
elif overSpeed >10 and overSpeed <= 15:
  print("Штраф: " + str(fineFor11to15) + " евро")
elif overSpeed >15 and overSpeed <= 20:
  print("Штраф: " + str(fineFor16to20) + " евро")
elif overSpeed >20 and overSpeed <= 25:
  print ("Штраф: " + str(fineFor21to25) + " евро")
elif overSpeed >25 and overSpeed <= 30:
  print("Штраф: " + str(fineFor26to30) + " евро")
elif overSpeed >30 and overSpeed <= 40:
  print("Штраф: " + str(fineFor31to40) + " евро")
elif overSpeed >40 and overSpeed <= 50:
  print("Штраф: " + str(fineFor41to50) + " евро")
elif overSpeed > 50 and overSpeed <= 60:
  print("Штраф: " + str(fineFor51to60) + " евро")
elif overSpeed > 60 and overSpeed <= 70:
  print("Штраф: " + str(fineFor61to70) + " евро")
elif overSpeed > 70:
  print("Штраф: " + str(fineFor70andMore) + " евро")