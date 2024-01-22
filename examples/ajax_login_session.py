#!/usr/bin/python3
from ajax_manager import AjaxManager

# Crea un'istanza di AjaxManager con le tue credenziali e chiavi API
ajax = AjaxManager(username="tuo_username", password="tua_password", xapikey="tua_chiave_api")

# Esegui il login per ottenere un token di sessione
ajax.login()

# Puoi quindi utilizzare altre funzionalità come ad esempio:
# - Armare l'allarme
# - Disarmare l'allarme
# - Controllare lo stato dell'allarme

# Esempio di armo dell'allarme (sostituisci con la tua implementazione)
# ajax.arm_alarm()

# Esempio di disarmo dell'allarme (sostituisci con la tua implementazione)
# ajax.disarm_alarm()

# Esempio di controllo dello stato dell'allarme (sostituisci con la tua implementazione)
# status = ajax.check_alarm_status()

# Stampa lo stato dell'allarme (sostituisci con la tua implementazione)
# print("Stato dell'allarme:", status)
