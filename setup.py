from setuptools import find_packages, setup

package_name = 'vel_ctrl'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'pygame'],
    zip_safe=True,
    maintainer='robo',
    maintainer_email='robo@todo.todo',
    description='Control velocities using pygame, ROS2, and Micro-ros',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vel_ctrl_node = vel_ctrl.vel_ctrl_node:main',
        ],
    },
)
