1. Al seleccionar la descipcion del problema, se decargaron 2 archivos (ltdis.sh y static)
2.  los inspeccionamos con el comando cat primero el archivo lstdis.sh
3. Nos imprime en la consola informacion sobre como algo llamado "objdump" y casi al final dice ago de "echo "Usage: ltdis.sh <program-file>""
4.  Asi que regresando a lo que no imprime en consola, empezamos siguiendo estos pasos:
    #This usage of "objdump" disassembles all (-D) of the first file given by 
    #invoker, but only prints out the ".text" section (-j .text) (only section
    #that matters in almost any compiled program...

5. Elscrip nos crea un segundo archivo llamado static,ltdis.x86.txt el cual se utilizara como argumento, el archivo static.
6. pocedemos ajecutar el comando "strings static | grep pico"