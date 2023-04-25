import Kitten 

time = 60

def when_get_signal(signal):
  if signal == 'V1':
    Kitten.change_shape('V1')

def when_start():
  while True :
    time = time - 1
    Kitten.wait_for_sec(1)


def when_press_key(keycode):
  if keycode == 32:
    Kitten.restart_project()



def when():
  while True:
    if (time == 0):
      Kitten.stop_project()

def when_get_signal(signal):
  if signal == 'V2':
    Kitten.change_shape('V2')

def when():
  while True:
    if (Kitten.value_of_object('Self', 'style_index') == 2 and Kitten.is_key_pressed(32)):
      Kitten.change_shape('坦克大战-背景')
      def call_events_of(name_ = '坦克1'):
        Kitten.show()


      call_events_of()
      def call_events_of(name_ = '坦克2'):
        Kitten.show()


      call_events_of()
      Kitten.send_signal('Restart')

def when():
  while True:
    if (Kitten.value_of_object('Self', 'style_index') == 3 and Kitten.is_key_up(32)):
      Kitten.change_shape('坦克大战-背景')
      def call_events_of(name_ = '坦克1'):
        Kitten.show()


      call_events_of()
      def call_events_of(name_ = '坦克2'):
        Kitten.show()


      call_events_of()
      Kitten.send_signal('Restart')
