import requests
import json

__all__ = ['create_an_imposter', 'delete_an_imposter']
mbServer = 'http://localhost:2525/imposters'
header = {"Content-Type": "application/json"}


def get_all_imposters():
    resp = requests.get(mbServer)
    return resp.json().get('imposters', None)


def create_an_imposter(imposter_path):
    with open(imposter_path, 'r') as file:
        payload = json.load(file)
        resp = requests.post(
            mbServer,
            headers=header,
            json=payload
        )
        if resp.status_code not in [200, 201]:
            raise "Create imposter failed"


def delete_an_imposter(port):
    # Should check if port has already existed
    all_imposters = get_all_imposters()
    if all_imposters:
        current_ports = list(map(lambda i: i["port"], all_imposters))

        if port in current_ports:
            # Make delete
            resp = requests.delete(
                f"{mbServer}/{port}"
            )
            if resp.status_code != 200:
                raise f"Delete imposter failed: {resp.text}"

# create_an_imposter('./imposters/user.ejs')
create_an_imposter('./proxy-config.json')
# delete_an_imposter(8089)