hrs =  input("Enter Hours:")
rate = input("Enter Rate:")
try:
  hr = float(hrs)
  rt = float(rate)
except:
    print("Please enter numeric input")
    quit()

if hr > 40:
    newrate= rt*1.5 # Rate for work over 40 hours
    total = (hr-40)*newrate # Total Fee for work over 40
    
print((40*rt) + total)
