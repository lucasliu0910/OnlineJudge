id = input()

city = {
      'A':10, #台北市
      'J':18, #新竹縣     
      'S':26, #高雄縣
      'B':11, #台中市     
      'K':19, #苗栗縣     
      'T':27, #屏東縣
      'C':12, #基隆市     
      'L':20, #台中縣    
      'U':28, #花蓮縣
      'D':13, #台南市     
      'M':21, #南投縣     
      'V':29, #台東縣
      'E':14, #高雄市     
      'N':22, #彰化縣     
      'W':32, #金門縣
      'F':15, #台北縣     
      'O':35, #新竹市     
      'X':30, #澎湖縣
      'G':16, #宜蘭縣     
      'P':23, #雲林縣     
      'Y':31, #陽明山
      'H':17, #桃園縣     
      'Q':24, #嘉義縣     
      'Z':33, #連江縣
      'I':34, #嘉義市     
      'R':25 #台南縣
}

city1 = str(city[id[0].upper()])[0]
city2 = str(city[id[0].upper()])[1]

number = id[1:-1]

number = int(number[-1])*1+ \
         int(number[-2])*2+ \
         int(number[-3])*3+ \
         int(number[-4])*4+ \
         int(number[-5])*5+ \
         int(number[-6])*6+ \
         int(number[-7])*7+ \
         int(number[-8])*8

total = int(number)+int(city2)*9+int(city1)+int(id[-1])

if (total%10)==0:
    print("real")
else:
    print("fake")
