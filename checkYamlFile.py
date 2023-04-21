import yaml

with open('docker-compose.yml','r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exec:
        print(exec)
