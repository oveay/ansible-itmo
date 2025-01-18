
import re
import json
import sys

def parse_vault_init_output(vault_output):
    unseal_key_pattern = r'Unseal Key \d+: ([\w+/=]+)'
    root_token_pattern = r'Initial Root Token: ([\w.]+)'

    unseal_keys = re.findall(unseal_key_pattern, vault_output)
    root_token_match = re.search(root_token_pattern, vault_output)
    root_token = root_token_match.group(1) if root_token_match else None

    parsed_data = {
        "unseal_key_1": unseal_keys[0],
        "unseal_key_2": unseal_keys[1],
        "unseal_key_3": unseal_keys[2],
        "unseal_key_4": unseal_keys[3],
        "unseal_key_5": unseal_keys[4],
        "initial_root_token": root_token
    }

    return parsed_data

filename = sys.argv[1] 
with open(filename, 'r') as f:
    data = f.read()

print(json.dumps(parse_vault_init_output(data)))