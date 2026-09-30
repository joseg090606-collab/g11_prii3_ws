# 🐢 Proyecto RII 3: Sprint 1 - Grupo 11 🐢

¡Hola! Aquí tienes los pasos súper sencillos para descargar nuestro proyecto y ver a la tortuguita dibujar el número 11 solita.

1. Abre tu terminal (Ctrl+ALT+T).
2. Copia este comando, pégalo en la terminal y presiona la tecla Enter para descargar nuestra carpeta:
   `git clone https://github.com/joseg090606-collab/g11_prii3_ws.git`

##Paso 1: Compilar
1. Entra a la carpeta que acabamos de descargar copiando esto y presionando Enter:
   `cd g11_prii3_ws`
2. Ahora vamos a armar el proyecto. Copia esto, pégalo y presiona Enter:
   `colcon build`

##Paso 2: Ejecutar
1. Copia esto y dale a Enter:
   `source install/setup.bash`
2. Lanza el simulador con este último comando y presiona Enter:
   `ros2 launch g11_prii3_turtlesim draw_11.launch.py`

##Se abrirá una ventana azul y verás a la tortuga dibujar un 11
