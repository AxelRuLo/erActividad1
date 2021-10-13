
import re

def comprobarER(oracion):
    valdator = re.compile("[a-z0-9]([a-z0-9]|([._-][a-z0-9]))*[@][a-z]([a-z]|([._-][a-z]))*[.][a-z]*")
    match =valdator.match(oracion)
    try:
        valida = match.group()==oracion
    except (TypeError, AttributeError):
        valida = False
    return  valida
    



