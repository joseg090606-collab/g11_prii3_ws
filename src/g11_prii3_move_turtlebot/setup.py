import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'g11_prii3_move_turtlebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Registra el paquete en el índice de ament
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # Incluye el archivo package.xml
        ('share/' + package_name, ['package.xml']),
        # Incluye archivos de launch si tuvieras en el paquete
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]'))),
        # Incluye el modelo SDF del cubo obstáculo
        (os.path.join('share', package_name, 'models', 'obstacle_cube'), glob('models/obstacle_cube/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sgomram1',
    maintainer_email='sgomram1@upv.edu.es',
    description='Paquete ROS 2 para trazado de numero 11 con TurtleBot3 en Gazebo',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'draw_number = g11_prii3_move_turtlebot.draw_number_sim:main',
        ],
    },
)