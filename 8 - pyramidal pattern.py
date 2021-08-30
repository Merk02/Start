#Exercise 8:
#Print the following pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5


while True:
  n=int(input('inserisci elementi range: '))
  if n==0:
    break
  def range_(n):
    for i in range(n):
      print(str(i)*i)

  range_(n)
