1. Vamos  al pagina web "http://saturn.picoctf.net:61430/"
2. abrimos el archivo HTML "ctl+u" no hya nada
3. encendemos el Burp
4. Brimos la aplicacion Burpsuite y hacmoe sun proxi, damos clic en los botones de l apgina web y mada 1 POST
5. mandamos un request 
6.  vemos que hay un ID, lo cambiamos por 0, y nos dice que es invaldo
7. en las pistas mecnionaba algo de XXE, asi que buscaos XXE playload "https://github.com/riyazwalikar/xxe-talk-null/blob/master/xxe.md"
8. pegamos esto en el request en donde dice el xml "<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]>" Y EN EL ID MANDAMOS "&test"
9. Damos en la pestaña respnse y nos da la bandera ¨picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf}¨