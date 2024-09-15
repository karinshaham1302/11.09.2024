# start

count: int = 1
age: int = int(input('what is your age?'))
beer: int = int(input('how many beer you had?'))

while age <= 18 and beer < 10:
    print('illegal age')
    beer = int(input('how many beer you had?'))
    count += 1
    for beer in range(1, 10 + 1, 1):
        print('beer')

if beer == 10:
    print('are you sure you want another on?')
else:
    print('you had enough')

# stop
#אני יודעת שלא הצלחתי לפתור, השארתי שתראה את הכיוון, ניסיתי לשלב עם while ו- for..



