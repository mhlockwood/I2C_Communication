#Hello, this is the main file

from dataclasses import dataclass
#import smbus2 import SMBus
from time import sleep
import yaml
from yaml.loader import SafeLoader

#read in YAML file
#called directly ~I think~
""""
if __name__ == '__main__':
    stream = open("config.yml", 'r')
"""
with open('config.yml') as f:
    variables = yaml.load(f, Loader=SafeLoader)
    print(variables)

#define variables from YAML file

#define functions




