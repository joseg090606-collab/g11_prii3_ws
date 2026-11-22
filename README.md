# 🐢 Proyecto RII 3: Sprint 1 - Grupo 11 🐢

Hola, Aquí tienes los pasos súper sencillos para descargar nuestro proyecto y ver a la tortuguita dibujar el número 11 solita.

1. Abre tu terminal (`Ctrl+ALT+T`).
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
##Para ver el codigo de control el siguiente comando dentro de la carpeta descargada
   `nano ~/g11_prii3_ws/src/g11_prii3_turtlesim/g11_prii3_turtlesim/control_node.py`



# 🐢 Proyecto RII 3: Sprint 2 - Grupo 11 🐢

Hola, aquí tienes los pasos súper sencillos para descargar nuestro proyecto y ver al TurtleBot3 dibujar el número 11 en Gazebo y RViz2, además de probar el servicio de control y la detención por Lidar.   

1. Abre tu terminal (`Ctrl+ALT+T`).
2. Copia este comando, pégalo en la terminal y presiona Enter para descargar nuestra carpeta:
   `git clone https://github.com/joseg090606-collab/g11_prii3_ws.git`

##Paso 1: Compilar
1. Entra a la carpeta que acabamos de descargar copiando esto y presionando Enter:
   `cd g11_prii3_ws`
2. Ahora vamos a armar el proyecto. Copia esto, pégalo y presiona Enter:
   `colcon build --packages-select g11_prii3_move_turtlebot`

#Paso 2: Ejecutar la Simulación
1. Lanza Gazebo con el TurtleBot3. Copia lo siguiente y presiona ENTER, comando a comando:
   `source install/setup.bash` // 
   `export TURTLEBOT3_MODEL=burger` // 
   `ros2 launch turtlebot3_gazebo empty_world.launch.py use_sim_time:=true`
2. Abre una terminal 2, entra en la misma carpeta siguiendo el primer paso de la compilacion y spawnea un cubo obstaculo copiando este comando y presiona ENTER:
   `ros2 run gazebo_ros spawn_entity.py   -file src/g11_prii3_move_turtlebot/obstaculo/cubo.sdf   -entity cubo_obstaculo   -x 0.5 -y 0.0 -z 0.1`
   Asi veras como en Gazebo habra aparecido un cubo el cual podras mover
3. Abre una terminal 3, entra en la misma carpeta siguiendo el primer paso de la compilacion y ejecuta el nodo trazador del numero 11. Copia y pega esto y presiona ENTER, comando a comando:
   `source install/setup.bash` // 
   `ros2 run g11_prii3_move_turtlebot draw_number --ros-args -p use_sim_time:=true`

#Paso 3: Probar Callbacks
1. Abre una terminal 4, entra en la misma carpeta siguiendo el primer paso de la compilacion y prueba los servicios de pausa y reanudacion:

   -Pausar la marcha:
      `ros2 service call /control_draw std_srvs/srv/SetBool "{data: false}"`

   -Reanudar la marcha:
      `ros2 service call /control_draw std_srvs/srv/SetBool "{data: true}"`



# 🐢 Proyecto RII 3: Sprint 3 - Grupo 11 🐢

Hola, aquí tienes los pasos sencillos para descargar nuestro proyecto, lanzar el entorno simulado del laboratorio F1L3 en Gazebo y cargar nuestro mapa para navegar con Nav2 y RViz2 (ESTA LINEA CAMBIARLA LUEGO)

1. Abre tu terminal (`Ctrl+ALT+T`).
2. Copia este comando, pégalo en la terminal y presiona Enter para descargar nuestro repositorio:
   `git clone https://github.com/joseg090606-collab/g11_prii3_ws.git`

##Paso 1: Compilar y Configurar el Entorno
1. Entra a la carpeta que acabamos de descargar copiando esto y presionando Enter:
   `cd g11_prii3_ws`
2. Ahora vamos a compilar los paquetes del proyecto. Copia esto, pégalo y presiona Enter:
   `colcon build`
3. Guarda el entorno y el modelo de TurtleBot3 en tu sistema para no tener que repetirlos en cada terminal nueva (solo se hace una vez):
   `echo "source ~/g11_prii3_ws/install/setup.bash" >> ~/.bashrc` // 
   `echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc` // 
   `source ~/.bashrc`

##Paso 2: Ejecutar la Simulación y Cargar el Mapa
1. Terminal 1 (Gazebo): Lanza el mundo simulado del laboratorio F1L3 con el TurtleBot3. Copia lo siguiente y presiona ENTER, comando a comando:
   `ros2 launch f1l3_gazebo f1l3_world.launch.py`
2. Terminal 2 (Nav2 y Mapa): Abre una segunda terminal, entra en la carpeta g11_prii3_ws y carga nuestro mapa guardado ejecutando comando a comando:
   `ros2 launch nav2_bringup bringup_launch.py map:=$(pwd)/src/g11_prii3_nav_turtlebot/maps/map.yaml use_sim_time:=true`
3. Terminal 3 (RViz2): Abre una tercera terminal, entra en g11_prii3_ws y abre RViz2 con la vista por defecto de Nav2 ejecutando comando a comando:
   `ros2 run rviz2 rviz2 -d $(ros2 pkg prefix nav2_bringup)/share/nav2_bringup/rviz/nav2_default_view.rviz`

##Paso 3: Localizar el Robot en RViz2
Antes de enviar cualquier objetivo de navegación, indica a Nav2 dónde se encuentra el robot en el mapa:
1. En la barra superior de RViz2, haz clic en 2D Pose Estimate.
2. Pincha sobre el mapa en la posición inicial del pasillo donde aparece el robot en Gazebo y arrastra la flecha verde apuntando hacia su frente.
3. Comprueba que el escáner láser (puntos de color) coincide con las paredes del mapa.

##Paso 4: Ejecutar la Navegación Autónoma (con Launch)
1. Terminal 4: Arranca simultáneamente el detector de ArUco y la máquina de estados de navegación autónoma:
   `ros2 launch g11_prii3_nav_turtlebot navegacion_turtlebot.launch.py`

##PASO OPCIONAL
Si en tu instalación de Gazebo no se carga la textura del marcador ArUco (viéndose como un cuadrado gris liso en la cámara), puedes simular la detección del ArUco 5 desde una terminal en cuanto el robot llegue y se detenga frente a la puerta:
1. Terminal 5 (opcional):
   `ros2 topic pub --once /aruco_topic std_msgs/msg/String "{data: '5'}"`
Al ejecutar este comando, la Terminal 4 confirmará la lectura mostrando las coordenadas de la puerta y el robot continuará hacia el interior del laboratorio.

##EJECUCION DE NODOS POR SEPARADO (PRUEBAS INDIVIDUALES):
Si deseas probar cada nodo individualmente en lugar de usar el archivo .launch.py:
*Navegación predefinida directa al laboratorio (sin ArUco):
   `ros2 run g11_prii3_nav_turtlebot predefined_navigation`
*Solo nodo detector de ArUco:
   `ros2 run g11_prii3_nav_turtlebot aruco_detector`
*Solo nodo de navegación autónoma:
   `ros2 run g11_prii3_nav_turtlebot autonomous_navigation`
