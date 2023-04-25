import Kitten 

time = 60

def Shot1():
  Kitten.play_sound('gun_kar98k')
  Kitten.show()
  Kitten.move_to('坦克1')
  Kitten.set_rotation(Kitten.value_of_object('坦克1', 'rotation'))
  while True :
    Kitten.move_forward(8)
    if (Kitten.is_touched('Self', '坦克2') or Kitten.is_touched('Self', '人机') or Kitten.is_touched('Self', '炮弹2') or Kitten.is_touched('Self', '炮弹3') or Kitten.is_touched('Self', 'edge')) :
      Kitten.hide()
      break

def when_get_signal(signal):
  if signal == 'V2':
    Kitten.stop_code('self_others')

def when_get_signal(signal):
  if signal == 'Restart':
    Kitten.restart_project()
