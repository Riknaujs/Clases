mycolor = input("Enter Color")
match mycolor.lower():
   case 'blue':
      print('Blue sea')
   case 'green':
      print('Green valley')
   case 'yellow':
      print('Yellow sun')
   case _:
      print('could not guess')