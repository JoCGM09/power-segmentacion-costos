import re
import sys
from my_functions import select_instance, exibe_menu, get_powervs, get_volumes, create_excel, getEvents,verifyRegion, verifyDC

if len(sys.argv) !=5:
    print ("Numero de parametros inválidos!!!")
    print (len(sys.argv))
    quit()

if (sys.argv[1] != "IAM") or (sys.argv[2] != "token:") or (sys.argv[3] != "Bearer"):
    print ("Parametros inválidos!!!")
    quit()

token=sys.argv[4]
instances = select_instance()
retorno_menu = exibe_menu('Informe a instancia:',instances,'name','guid','id','region_id')

print("RETORNO MENU")
print(retorno_menu)

while retorno_menu[0] != 0:
    instancia_id = retorno_menu[2]
    instancia_crn = retorno_menu[3]
    print("CRN: "+instancia_crn)
    instancia_name =retorno_menu[1]
    dc_id = verifyDC(retorno_menu[4])
    region_id = verifyRegion(retorno_menu[4])
    
    print(region_id)

    teste = getEvents(instancia_id,instancia_crn, token, region_id, instancia_name)
    virtual_servers = get_powervs(instancia_id, instancia_crn,instancia_name,token,region_id)
    volumes = get_volumes(instancia_id, virtual_servers,instancia_crn,token, instancia_name,region_id)
    excel = create_excel(instancia_name, instancia_id,dc_id)

    retorno_menu = exibe_menu('Informe a instancia:',instances,'name','guid','id','region_id')

print('Obrigado...')

