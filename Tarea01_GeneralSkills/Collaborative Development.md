1. Deargamos el archivo "wget https://artifacts.picoctf.net/c_titan/71/challenge.zip"
2. hacemos un unzip y nos extrae un carpeta llamada "drop-in"
3. entramos a la carpeta drop-in y vemos que hay un archivo python "flag.py"
4. Leemos las pistas del reto y nos da la sugerencia de ver cuantas ramas hay "git branch -a" y vemos que hay como "3 ramas"
5. Entramos a cada una de las ramas para ver que hay "git checkout feature/part-1".
6. ahora ejecutamos el archivo .py para ver que pusieron en esa rama a ese archivo "python flag.py"
7. Vemos que nos imprime una parte de la bandera "picoCTF{t3@mw0rk_", lo que da a entender que n cada rama hya una parte de la bandera.
8. hacemos lo el paso 5 y 6 con la rama 2 y 3.
9. Juntamos las 3 partes de la bandera "picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_4c24302f}" 