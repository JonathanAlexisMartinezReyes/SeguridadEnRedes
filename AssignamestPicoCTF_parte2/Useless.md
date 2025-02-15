1. leyebdo la descirpcion se ve que teniamos que hacer una coneccion ssh por medio de saturn.
2. le dimos a launch y ya nos dio el puerto al que nos teniamo que conectar en mi caso "63919"
    tambien mi uurio "picoplayer"
    y la contrasña> password
3. primero me conecte con este comando "nc saturn.picoctf.net 63919" y sol se quedaba con la conexion pero no entraba.
4. en seguia lo intente con el usuario como si fuera correo por medio de un ssh
    "ssh picoplayer@saturn.picoctf.net 63919" y no me funcionaba, jastq que busque en internet y me decia que tenia ue poner "-p".
        por lo que alfinal me pude conectar de este modo "ssh picoplayer@saturn.picoctf.net -p 63919"
5. me pregunto que si estab segro de conectarme y puse "yes".
6. como la descripcion decia que hay archivo interesantes en el home lo que hice fue hacer un "ls".
7. me mostraba el archivo useless y procedi a hacer un "cat useless".
8. me mostro un codigo o mas bien una documentacion. asi que procedi a leerlo con el comando "man useless"
9. di puros enter hastq que al final me di la bandera "picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}" y se cierra la conexin.