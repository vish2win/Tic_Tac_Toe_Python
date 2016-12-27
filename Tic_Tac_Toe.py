print('Enter your name User1')
print('Enter your name User2')
User1=input('')
User2=input('')
while True:
  print('Hello '+User1 +'\n Please select the warrior you want \n X \t \t O \n')
  warrior1=input('')
  if len(warrior1)==1:
    if(warrior1=='X'):
      warrior2='O'
      print(User1+ ',Your warrior is ' + warrior1 +'\n'+User2 +',Your warrior is '+ warrior2)
      break
    elif(warrior1=='O'):
      warrior2='X'
      print(User1 +',Your warrior is ' + warrior1 +'\n'+User2+',Your warrior is '+ warrior2)
      break
    else:
      print(User1+",Please Enter the correct input")
    
    
print('\n Who will start the game?')
if(User1==input('')):
  print(User1+' Starts and makes the first move')
else:
  print(User2+' Starts and makes the first move')
  
print('\n Lets start the game')
