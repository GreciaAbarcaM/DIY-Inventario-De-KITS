# Pasos para programar la ESP32-CAM y hacer que se conecte a la aplicación de Telegram.

Lo primero que debes hacer es descargar el programa con el que vas a programar el microcontrolaro, ese programa se llama "ESP32 FLASH DOWNLOAD TOOLS".

Lo encontraras en la parte de herramientas de descarga Flash
![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/afb7863e-5f95-464b-b84c-a25efee755d0)
- [ ESP32 FLASH DOWNLOAD TOOLS ](https://www.espressif.com/en/support/download/other-tools)

Una ves descargado procedes a instalarlo en el disco C de tu computadora o en donde tengas espacio.

Ya instalado procedemos a abrir el programa, este se encontrara en la dirección donde lo instalaste, buscalo y ejecutalo como administrador.
![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/a9762a46-b518-44cf-b0e3-53cc4e609fcb)

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/6592b865-c0a2-4be5-8cdc-b9736505d945)

El programa se mostrara con su logo principal, con ello sabras que si estas abriendo el programa.
![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/6aeed1f7-cdc8-457d-b879-1f95050e6024)

Una vez abierto, veras que lo primero que aparecera sera una terminal, seguida de ela veras un recuadro el cual te dara la opcion de seleccionar el tipo de microcontrolador con el que vas a trabajar.

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/65e372da-a229-49cb-a1f3-f3be8737b8c4)

Tu seleccionaras la opción de ESP32

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/e0fdd3f9-08a7-4345-b8e2-2832b0216095)

Echo esto, selecciona la opción "OK". Se abrira un panel con diferentes seldas, las cuales van a requerir que insertes los codigos binarios con los que vas a programar la ESP32-CAM.

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/7974276d-d7e9-4642-832b-d7a91ba4268e)

Los codigos binarios los encontraras en un archivo .zip en el repositorio o en la siguiente liga, de ahi podras descargarlos.

- [ Códigos binarios ](https://drive.google.com/file/d/1RPjUQXg_04nWLqCY7mIbu_l8wDB-TKUb/view)

Una ves que los hayas descargado, es preferible que muevas la carpeta a la misma en donde descargaste el programa, para que sepas donde se encuentras y no pierdas los pasos a seguir.

El siguiente paso es introducir los codigos binarios al programa:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/ef99e44b-886a-4e36-a28e-aba8083528b9)

Para hacer eso selecciona la selda que vas a llenar, en este caso es la primera. 
Te vas dirigir a la casilla que cuenta con tres puntos "..." 

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/448e32d1-8497-425e-8776-4b5afd45bf01)

Te vas a dirigir a la carpeta en donde descargaste los codigos binarios, al abrir el documento te encontraras con los siguientes archivos.

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/e01b4e24-dd64-4e5b-9e06-d022b1557980)

Vamos a ocupar 3 de los archviso que estan ahi, el primero que vas a seleccionar es este:
- 0x1000.bootloader
![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/0f0e00d1-a085-45f0-8137-7c080a9e1c65)

Veras como la selda se pondra en color verde, esto significa que lo ha seleccionado correctamente, ahora vas a poner el valor del archivo bootloader, y lo pondras en la casilla que esta despues del @:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/61d7ec86-2582-43c3-b59f-43b29c5c9ee1)

Veras como se pondra en color verde esa casilla tambien, ahora seleccionaras los siguientes 2 arvhivos y los pondras en orden descendente, además, tambien agregaras el valor de estos:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/956cd956-2597-404d-a380-f1ba784c8ac3)

Ahora conecta la ESP32-CAM  al puerto USB, pasaremos a programarla. La forma en como debes de conectar la ESP32-CAM para programarla es la siguiente.

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/c1d3d1f7-9578-413c-b22a-18020c52248b)

Ahora seleccionaras el puerto y los baulios con los que programaremos la ESP32. En este caso sera el COM que te designe tu computadora y los baulios seran de 921600.

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/e3a80f07-c84a-4e83-9fd9-3369259db2dd)

Echo este procederas a Ejecutar la opcion de programación, la cual inicia dando START en el programa. Veras como empieza a procesar los codigos, a mitas de la opcion te pondra una nota, la cual requiere que presiones el boton de reset de la ESP32-CAM para que se cargue todo correctamente.
Finalizado esto, el programa te dira "FINISH"

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/bdf8c783-0d4c-41dc-b143-15843cb3d097)

Con esto aseguramos que el codigo esta arriba, ahora lo que procede es dirigirte a darte un IDBOT DE TELEGRAM con el que la ESP32-CAM va a interactuar.
Para esto necesitas entar a TELEGRAM Y BUSCAR:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/9a0eab5d-bc8f-4d1a-a527-6ac925f0c6e9)

En este chat encontraremos la opción de crear un nuevo ID:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/70788783-f669-4371-8fb2-5228dacf0834)

Introduciras un comando el cual sera /start, y luego /newbot:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/b412b869-1c2a-46f6-95ca-e3a3d731de82)

Te pedira que le asignes un nombre a tu bot, y despues te pedira que le asignes otro nombre con una terminacion _bot.

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/d6e3dfe5-7828-4b5a-a923-9b69e87020e0)

Hecho esto el IDBOT te dara tu propio ID el cual utilizaremos para enlazar la ESP con TELEGRAM.

Ahora vuelve al menu principal de TELEGRAM y busca:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/83f87eb5-7017-43b0-a2b2-24dc7e67ef2c)

Este te asignara un segundo ID que ocuparemos.
Le mandaras un comando llamado /start, y luego otro /getid:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/9171dcee-7790-4065-83c1-9d6623953eb5)

Teniendo estos ID, procederas a energizar la ESP32.
Ahora accede a tu menu de tu telefono en la configuración de WIFI, Y busca la señal "DOORBELLCAM".

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/44e2b6bc-d686-4dfa-a02c-5bdc196c1db4)

Conectate a esa red, su contraseña sera "12345678", esto con el fin de evitar que más usuarios interactuen con esa red.
Ahora accederas al siguiente URL
- [ Página de enlazamiento de la ESP32-CAM con TELEGRAM ](192.168.4.1)
Te debe de aparecer una pagina como esta:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/c3d05d60-0909-429a-91e2-b13b74ddb5a8)

Ahí pondras tu Señal de WIFI, TU CONTRASEÑA Y LAS ID QUE OBTUVISTE ANTERIORMENTE DE TELEGRAM.
LA PRIMER ID QUE PONDRAS ES LA QUE TE DIO EL BOTFATHER (la ID más larga) Y LUEGO LA ID DEL IDBOT (la ID más corta).
![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/77e1d399-aaa7-47e5-b32d-5efd00291d2a)

Hecho esto, selecciona la opcion "SUBMIT" para cargar la información y espera unos segundos, veras como la ESP32 SE CONECTA A LA SEÑAL WIFI, ya que veras parpadear el led unas 5 veces.

Ahora dirigete a telegram y busca tu bot con el nombre que le allas asignado:

![image](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/c73a7966-d486-4783-a8a2-c9c9f1f69e3d)

Ya solo queda que le asignes el comando /start para que te desplace el menu de opciones que tienes, las cuales seran tomar foto con el comando /photo, y prender o apagar el flas con el comando /flash.

![fc295ecc-8d22-41e8-bc6b-5e09e01162e8](https://github.com/GreciaAbarcaM/DIY-Inventario-De-KITS/assets/135075213/ff39b396-da67-49e7-8863-e39ce807494c)

Felicidades, has programado tu ESP32 Y AHORA PUEDE INTERACCIONAR CON LA APLICACIÓN DE TELEGRAM.



