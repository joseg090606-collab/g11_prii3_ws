# 🐢 Proyecto RII 3: Sprint 1 - Grupo 11 🐢

Hola, Aquí tienes los pasos súper sencillos para descargar nuestro proyecto y ver a la tortuguita dibujar el número 11 solita.

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
##Para ver el codigo de control el siguiente comando dentro de la carpeta descargada
   `nano ~/g11_prii3_ws/src/g11_prii3_turtlesim/g11_prii3_turtlesim/control_node.py`



# 🐢 Proyecto RII 3: Sprint 2- Grupo 11 🐢

Hola, aquí tienes los pasos súper sencillos para descargar nuestro proyecto y ver al TurtleBot3 dibujar el número 11 en Gazebo y RViz2, además de probar el servicio de control y la detención por Lidar.   

1. Abre tu terminal (Ctrl+ALT+T).
2. Copia este comando, pégalo en la terminal y presiona Enter para descargar nuestra carpeta:
   `git clone https://github.com/joseg090606-collab/g11_prii3_ws.git`

##Paso 1: Compilar
1. Entra a la carpeta que acabamos de descargar copiando esto y presionando Enter:
   `cd g11_prii3_ws`
2. Ahora vamos a armar el proyecto. Copia esto, pégalo y presiona Enter:
   `colcon build --packages-select g11_prii3_move_turtlebot`

#Paso 2: Ejecutar la Simulación
1. Carga el entorno y define el modelo del robot:
   source install/setup.bashexport TURTLEBOT3_MODEL=burger
2. 

crear un cubo con nano ~/cubo.sdf
pegar el siguiente: 
<sdf version="1.6">
  <model name="cubo">
    <static>false</static>
    <link name="link">
      <pose>0 0 0 0 0 0</pose>
      <collision name="collision">
        <geometry>
          <box>
            <size>0.5 0.5 0.5</size>
          </box>
        </geometry>
      </collision>
      <visual name="visual">
        <geometry>
          <box>
            <size>0.5 0.5 0.5</size>
          </box>
        </geometry>
      </visual>
    </link>
  </model>
</sdf>

///////////////
crear el obstaculo: 
ros2 service call /spawn_entity gazebo_msgs/srv/SpawnEntity "{name: 'cubo', xml: '$(cat ~/cubo.sdf)', robot_namespace: '', initial_pose: {position: {x: 1.2, y: 0.0, z: 0.25}}, reference_frame: 'world'}"
