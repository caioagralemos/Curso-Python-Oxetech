def convert_time(horas, minutos):
    if horas > 24 or horas < 0 or minutos > 60 or minutos < 0:
        return 'Esse horário é inválido.'
    if minutos < 10: 
        minutos = f'0{minutos}'

    if horas <= 12:
        return f'São {horas}:{minutos}AM'
    elif horas > 12 and horas < 24:
        return f'São {horas-12}:{minutos}PM'
    elif horas == 24 and minutos == 00:
        return f'São 00:00AM'
    
print(convert_time(13,7))