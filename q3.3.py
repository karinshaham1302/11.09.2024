# start

pie: int = 3.14
pie: float = float(input('how much the pie worth?'))
count: int = 1

while pie != 3.14 and count <= 3:
    count += 1
    pie = float(input('how much the pie worth?'))

if count <= 3:
    print('you are correct')
else:
    print('pie is 3.14')

# stop
