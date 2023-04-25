import Kitten 

time = 60
self.生命值 = 5

def when_start():
  if (random.randint(0, 1) == 0) :
    Kitten.face_to('坦克1')
  else :
    Kitten.face_to('坦克2')
  while True :
    Kitten.wait_for_sec(random.randint(2, 5))
    Shot3()
  while True :
    Kitten.show()
    Kitten.wait_for_sec(random.randint(1, 4))
    Kitten.add_rotation(random.randint(30, 180))
    Kitten.move_forward(random.randint(8, 64))
    Kitten.bounce_on_edge()
  while True :
    if (self.生命值 == 0) :
      Kitten.hide()
    else :
      Kitten.show()


def when():
  while True:
    if (Kitten.is_touched('Self', '炮弹1') or Kitten.is_touched('Self', '炮弹2')):
      生命值 = 生命值 - 1
