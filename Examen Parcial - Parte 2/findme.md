1. Damos a la ocion de lanzar servidor.
2. nos manda a una pagina web "http://saturn.picoctf.net:50523"
3. en la descripcion nos daba un usuario "test" y su contraseña "test!"
4. vemos qu enentramos una pagina, pero no hay nada.
5. abrimos la herramientas de desrrollador de la pagina web "ctl+q"
6. actualizamos la pagina y en la aprte de wnetwork de la terminal vemos que hay un request tipo get
7. la URL se actualiza y entonces retrocedemos al inicio y vemos que en una parte de la direccion el vor de la ID cambia, asi que primero vemos la primer url "http://saturn.picoctf.net:50523/next-page/id=bF90aGVfd2F5XzI1YmJhZTlhfQ=="vemos que el valor que tine es algo de base64
8. entramos a un decodificador online "[Base64 Decode and Encode - Online](https://www.base64decode.org/)" y ponemos le valor de la id "bF90aGVfd2F5XzI1YmJhZTlhfQ" y nos da "l_the_way_25bbae9a}" el final de la bander
9. retrocedemos otra vez la pagina web hacia atras y cambia el valor de ID en la url a este "http://saturn.picoctf.net:50523/next-page/id=cGljb0NURntwcm94aWVzX2Fs==" y en la traduccion de base4 es "picoCTF{proxies_al"
10. juntamos las 2 partes de la bandera y obtemnemos la completa "picoCTF{proxies_all_the_way_25bbae9a}"