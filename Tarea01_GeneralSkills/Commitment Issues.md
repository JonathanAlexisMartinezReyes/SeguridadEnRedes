1. descargamos el archivo "https://artifacts.picoctf.net/c_titan/138/challenge.zip"
2. entramos al directorio drop-in
3. haceo sun "ls" y vemos qu ehay un archivo message.txt, hacemos un "cat message.txt" y nos imprime en la consola "TOP SECRET"
4. hacemos un "git log" para ver los utmo scambios, y vemos que hay comits. checaremos cada uno de lso comits.
5. vemos que hay 2 commits, en el segundo dice "create flag".
6. nos cambiamos a la rama donde esta ese commit, pero en ves de poner el nombre de una rama, ponemos el nombre del comit "git checkout b562f0b425907789d112fe279e67592dc6be93"
7. hacemos un "cat" y nos da la bandera "picoCTF{s@n1t1z3_c785c319}"