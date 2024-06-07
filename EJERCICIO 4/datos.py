from estadia import Estadia
from datetime import datetime


estadias = [Estadia(datetime.today, 'EFF694', datetime.time(7,00)),
            Estadia(datetime.today,'ABC123', datetime.time(6,50))
]

estadias[0].registrar_salida()