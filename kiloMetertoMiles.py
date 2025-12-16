try:
  kilometer = float(input("Enter distance in kilometer: "))
  miles = kilometer * 0.621371

except ValueError:
  print("Invalid input: Enter numeric values")
except TypeError:
  print("Invalid dataType")
except Exception:
  print("Unexpected Error Occurs")
else:
  print("Miles ==>",miles)
