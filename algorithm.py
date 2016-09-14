for i in range (2000,5000,5) :
   termStart = i + 2
   termEnd = termStart + 5
   OGDatesArray = []
   for j in range (termStart, termEnd, 1) :
       if j%4==0 :
           OGDatesArray.append(j)
   if len(OGDatesArray) >= 2 :
       print("Term ", termStart, "-", termEnd, " : ")
       for x in arrayOGDates :
           print(x)
