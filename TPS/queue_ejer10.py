from queue_ import Queue
from random import randint
from stack import Stack
from datetime import datetime
'''
queue_letters= Queue()

for i in range(15):
    queue_letters.arrive(chr(randint(65,90)))

queue_letters.show()
print()

for i in range(queue_letters.size()):
    value = queue_letters.attention()
    if value in ["A","E", "I", "O", "U"]:
        pass
    else:
        queue_letters.arrive(value)

queue_letters.show()
print()

aux_q= Queue()

for i in range(queue_letters.size()):
    queue_letters

''' 
queue_notification = Queue()

queue_notification.arrive({'hora': '11:30', 'aplicacion': 'Facebook', 'mensaje': 'nuevo like en tu publicación'})
queue_notification.arrive({'hora': '11:45', 'aplicacion': 'Twitter', 'mensaje': 'aprendiendo python hoy'})
queue_notification.arrive({'hora': '12:00', 'aplicacion': 'Instagram', 'mensaje': 'nuevo seguidor'})
queue_notification.arrive({'hora': '14:30', 'aplicacion': 'Twitter', 'mensaje': 'python es el lenguaje del futuro'})
queue_notification.arrive({'hora': '15:55', 'aplicacion': 'Facebook', 'mensaje': 'recordatorio de evento'})
queue_notification.arrive({'hora': '16:00', 'aplicacion': 'Twitter', 'mensaje': 'taller de programación'})
queue_notification.arrive({'hora': '10:00', 'aplicacion': 'Facebook', 'mensaje': 'mira lo que compartieron'})

def notification_Facebook(q):
    for i in range(q.size()):
        value= q.attention()
        if value['aplicacion'] != 'Facebook':
            q.arrive(value)
            
# notification_Facebook(queue_notification)
# queue_notification.show()

def mensaje_python(q):
    for i in range(q.size()):
        value = q.move_to_end()
        if value['aplicacion'] == 'Twitter' and 'python' in value['mensaje']:
            print(value)

# mensaje_python(queue_notification)


def filtrar_notificaciones_por_hora(queue_notification):
    
    notification_stack = Stack()
    
    hora_inicio = datetime.strptime('11:43', '%H:%M').time()
    hora_fin = datetime.strptime('15:57', '%H:%M').time()
    
    for i in range (queue_notification.size()):
        value = queue_notification.move_to_end()
        hora_value = datetime.strptime(value['hora'], '%H:%M').time()
        if hora_inicio <= hora_value <= hora_fin:
            notification_stack.push(value)
    print(f"\nNotificaciones entre 11:43 y 15:57: {notification_stack.size()}")

filtrar_notificaciones_por_hora(queue_notification)
