import numpy


def random_walk(num):
   y=0
   x=0
   for _ in range(num):
      dire=numpy.random.choice(['W','E','N','S'])
      if dire=='N':
          y+=1
      elif dire=="S":
          y-=1
      elif dire=='W':
          x-=1
      else:
          x+=1
   return (x,y)          

def simulate(pat, num):
  z=0
  v=0
  coord_x,coord_y=0,0
  
  for x in pat:
      v=0
      for y in x:
          if y=='#':
              coord_x=v
              coord_y=z
          v+=1    
      z+=1

  
  hori=coord_x
  vert=coord_y
  
  for x in range(num):  
    x,y=random_walk(1)
    hori+=x
    vert+=y
    if hori==-1:
      hori=0
    elif vert==-1:
      vert=0
    if hori>4:
       hori-=1
    elif vert>4:
       vert -=1            
    print(f"The Y axis --> {vert} The X axis --> {hori}")

    pat[vert][hori]='x'
  pat[vert][hori]='#'  
  return pat 

  
     