import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'g11_prii3_nav_turtlebot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]'))),
        (os.path.join('share', package_name, 'maps'), glob('maps/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sgomram1',
    maintainer_email='sgomram1@upv.edu.es',
    description='Paquete ROS 2 para navegacion autonoma con TurtleBot3 (Sprint 3)',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'predefined_navigation = g11_prii3_nav_turtlebot.navegacion_predefinida_turtlebot:main',
            'aruco_detector = g11_prii3_nav_turtlebot.aruco_detector:main',
            'autonomous_navigation = g11_prii3_nav_turtlebot.navegacion_autonoma:main',
        ],
    },
)