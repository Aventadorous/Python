months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }



def season_events(number_of_month):
   if number_of_month > 12 or number_of_month < 0:
        print('Please write your CORRECT month')
        return
   if number_of_month in range(3, 6):
    print(f'You were born in {months[number_of_month]}. Birds sag beautiful songs')
   elif number_of_month in range(6, 9):
    print(f'You were born in {months[number_of_month]}. The sun shone brighter than ever')
   elif number_of_month in range(9, 12):
    print(f'You were born in {months[number_of_month]}. The harvest was incredible')
   else:
    print(f'You were born in {months[number_of_month]}. White snow fell outside the window')

number_of_month = int(input('Your month'))
season_events(number_of_month)
