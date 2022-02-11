import yaml


robots_yaml = """
- 'roomba'
- 'husky'
- 'yaskawa'
"""
names = yaml.safe_load(robots_yaml)

with open('names.yaml', 'w') as file:
    yaml.dump(names, file)

load_yaml = open('names.yaml').read()

print(load_yaml)