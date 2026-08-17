import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'archo_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', 'archo_bringup', 'launch'), glob('launch/*')),
        (os.path.join('share', 'archo_bringup', 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luka',
    maintainer_email='ostojic.luka36@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'simple_node = archo_bringup.simple_node:main',
            'battery_monitor = archo_bringup.battery_monitor:main',
            'dashboard = archo_bringup.dashboard:main',
            'motor_controller = archo_bringup.motor_controller:main',
        ],
    },
)
