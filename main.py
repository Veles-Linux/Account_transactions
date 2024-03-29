import json
import utils

with open('operations.json') as f:
    templates = json.load(f)

print(utils.output_operations(utils.operations(templates)))
