1. damos clic a "launches an instance"
2. Se actualiza la descripcion y nos da esta pagina "http://titan.picoctf.net:55852/"
3. abrimos la aplicacion Burp
4. llenamos el formulario de la pagia a donde nos mando
5. Vemos tro campo para llenar, en ese punto prendemos nuestro Burp de la extencion "FoxyProxy"
6. En la aplicacion "Burpsuite" 
	1. nos vamos a la pestaña "proxy"
	2. damos clic en "intercept off" par renderlo
	
7. Regresamoa l navegado web, lenamos la caja de texto con lo que sea y damos clic al boton submit
8. Regresamos a la plicacion Burpsuite
	1. Damos clic derecho abajo en el request y deleccionamos la ocion "send to repeater"
	2. hasta abajo enla solicitud ah una varible llamda "otp" la quitamos, damos a enviar
9. obtenemos la bandera "picoCTF{#0TP_Bypvss_SuCc3$S_c94b61ac}"
10. regresamos al navegador web, apagamos nuestra extencion "FoxyProxy" y ya pegamos la bander en los retos pico ctf.