import network
import time

def conectar(red, contra):
    global mired
    
    mired = network.WLAN(network.STA_IF)
    
    if not mired.isconnected():
        mired.active(True)
        mired.connect(red, contra)
        print(f'conectando a la red {red} ...')
        timeout = time.time()
        
        while not mired.isconnected():
            if (time.ticks_diff(time.time(), timeout) > 10):
                return False
            
    return True

if conectar('NetworkName','Password'):
    print('Conexion exitosa!')
    print(f'Datos de la red  (ip/netmask/gw/dns): {mired.ifconfig()}') 
    
