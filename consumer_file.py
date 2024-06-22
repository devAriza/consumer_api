import requests
import json

if __name__ == '__main__':
    url = 'https://repse.presta.ebsonline.mx:7380/Content/images/btn-document-types.png'
    # stream en true deja conexion abierta
    response = requests.get(url, stream=True)

    #descargar imagen
    #wb escribir en forma binaria
    with open('image.png', 'wb') as file:
        #para archivos pesados
        for chunk in response.iter_content(): #iter_content descarga contenido poco a poco
            file.write(chunk)

    response.close() #cerrar conexion

