from setuptools import setup
from glob import glob
import os

package_name = 'minibot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '**'))),
        (os.path.join('share', package_name, 'description'), glob(os.path.join('description', 'robot.urdf.xacro'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='colin',
    maintainer_email='colin.schuh@uky.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ball_node = minibot.distance_to_ball:main',
            'qr_detector = minibot.qr_detector:main',
            'imu_echo = minibot.imu_echo:main',
        ],
    },
)
