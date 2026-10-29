# 🐢 Proyecto RII 3: Sprint 1 - Grupo 11 🐢

Hola, Aquí tienes los pasos súper sencillos para descargar nuestro proyecto y ver a la tortuguita dibujar el número 11 solita.

1. Abre tu terminal (Ctrl+ALT+T).
2. Copia este comando, pégalo en la terminal y presiona la tecla Enter para descargar nuestra carpeta:
   -`git clone https://github.com/joseg090606-collab/g11_prii3_ws.git`

##Paso 1: Compilar
1. Entra a la carpeta que acabamos de descargar copiando esto y presionando Enter:
   -`cd g11_prii3_ws`
2. Ahora vamos a armar el proyecto. Copia esto, pégalo y presiona Enter:
   -`colcon build`

##Paso 2: Ejecutar
1. Copia esto y dale a Enter:
   -`source install/setup.bash`
2. Lanza el simulador con este último comando y presiona Enter:
   -`ros2 launch g11_prii3_turtlesim draw_11.launch.py`

##Se abrirá una ventana azul y verás a la tortuga dibujar un 11
##Para ver el codigo de control el siguiente comando dentro de la carpeta descargada
   -`nano ~/g11_prii3_ws/src/g11_prii3_turtlesim/g11_prii3_turtlesim/control_node.py`



# 🐢 Proyecto RII 3: Sprint 2- Grupo 11 🐢

Hola, aquí tienes los pasos súper sencillos para descargar nuestro proyecto y ver al TurtleBot3 dibujar el número 11 en Gazebo y RViz2, además de probar el servicio de control y la detención por Lidar.   

1. Abre tu terminal (Ctrl+ALT+T).
2. Copia este comando, pégalo en la terminal y presiona Enter para descargar nuestra carpeta:
   -`git clone https://github.com/joseg090606-collab/g11_prii3_ws.git`

##Paso 1: Compilar
1. Entra a la carpeta que acabamos de descargar copiando esto y presionando Enter:
   -`cd g11_prii3_ws`
2. Ahora vamos a armar el proyecto. Copia esto, pégalo y presiona Enter:
   -`colcon build --packages-select g11_prii3_move_turtlebot`

#Paso 2: Ejecutar la Simulación
1. Lanza Gazebo con el TurtleBot3. Copia lo siguiente y presiona ENTER, comando a comando:
   -`source install/setup.bash`
   -`export TURTLEBOT3_MODEL=burger`
   -`ros2 launch turtlebot3_gazebo empty_world.launch.py use_sim_time:=true`
2. Abre una terminal 2, entra en la misma carpeta siguiendo el primer paso de la compilacion y spawnea un cubo obstaculo copiando este comando y presiona ENTER:
   -`ros2 run gazebo_ros spawn_entity.py \
   -file src/g11_prii3_move_turtlebot/obstaculo/cubo.sdf \
   -entity cubo_obstaculo \
   -x 0.5 -y 0.0 -z 0.1`
   Asi veras como en Gazebo habra aparecido un cubo el cual podras mover
3. Abre una terminal 3, entra en la misma carpeta siguiendo el primer paso de la compilacion y ejecuta el nodo trazador del numero 11. Copia y pega esto y presiona ENTER, comando a comando:
   -`source install/setup.bash`
   -`ros2 run g11_prii3_move_turtlebot draw_number --ros-args -p use_sim_time:=true`

#Paso 3: Probar Callbacks
1. Abre una terminal 4, entra en la misma carpeta siguiendo el primer paso de la compilacion y prueba los servicios de pausa y reanudacion:

   -Pausar la marcha:
      -`ros2 service call /control_draw std_srvs/srv/SetBool "{data: false}"`

   -Reanudar la marcha:
      -`ros2 service call /control_draw std_srvs/srv/SetBool "{data: true}"`
