foot = float(input())*30
inch = float(input())*(30/12)

print("แปลงค่าความยาว เท่ากับ",int((foot+inch)//100),"เมตร",(foot+inch)%100,"เซนติเมตร")