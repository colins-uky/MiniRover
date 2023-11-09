import yaml
import os
from ament_index_python.packages import get_package_share_directory


def return_config():
    cfg = None

    filepath = get_package_share_directory("minibot").replace("/install/minibot/share/minibot", "")
    
    new_path = os.path.join(filepath, "src", "minibot", "config.yaml")

    with open(new_path, 'r') as file:
        cfg = yaml.load(file, Loader=yaml.SafeLoader)

    return cfg


x = return_config()
print(x)