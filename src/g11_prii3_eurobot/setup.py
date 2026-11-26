from setuptools import find_packages, setup

package_name = 'g11_prii3_eurobot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lubuh',
    maintainer_email='sgomram1@upv.edu.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'navegacion_odom = g11_prii3_eurobot.navegacion_odom:main',
            'overhead_aruco_detector = g11_prii3_eurobot.overhead_aruco_detector:main',
        ],
    },
)
