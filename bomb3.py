import Kitten 

time = 60

def Shot3():
  Kitten.play_sound('gun_awm')
  Kitten.show()
  Kitten.move_to('人机')
  Kitten.set_rotation(Kitten.value_of_object('人机', 'rotation'))
  while True :
    Kitten.move_forward(8)
    if (Kitten.is_touched('Self', '坦克2') or Kitten.is_touched('Self', '坦克1') or Kitten.is_touched('Self', '炮弹1') or Kitten.is_touched('Self', '炮弹2') or Kitten.is_touched('Self', 'edge')) :
      Kitten.hide()
      break
