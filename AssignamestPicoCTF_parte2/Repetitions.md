1. al leer el la descripcion habia una parte nos dece que tenemos que decargar un archivo.
2. Y era un archivo encriptado, y al leer la pista decia "que le decodeo multiple siempre es mejor".
3.  ejecutamos el comando "ls".
4. nos cambiamos al directorio "Downloads"
5. ejecutamos el comando "ls" y automaticamente me lo completa "ls -l"
6.  vemos que ahi esta el archivo de codeado, asi que ejecutamos el comando cat "cat enc_flag".
7. pues al ver que el archivo encodeado, lo que hice mejor fue buscar en la web una oagina par desinciptar archivos "https://gchq.github.io/CyberChef/"
8. Tampoco funciono, asi que busque un codigo para desencriptar un codigo, y encontre el siguiente:
    import base64 as b
    with open("enc_flag", "r") as file:
        cipher = file.readlines()
        cipher = "".join([i.strip() for i in cipher])
        plain = b.b64decode(cipher).decode("utf-8")
        while "picoCTF" not in plain:
            plain = b.b64decode(plain).decode("utf-8")
        print(plain)
9. Simplemente le puse la ruta donde tenia el archivo yo decargado "C:/Users/jonat/Downloads/enc_flag"
10. Obtenemos la bandera "picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_9b59b35c}"
