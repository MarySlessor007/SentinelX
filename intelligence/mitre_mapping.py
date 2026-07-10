MITRE_MAPPING = {

    "SSH Brute Force": {

        "id": "T1110",

        "name": "Brute Force",

        "tactic": "Credential Access"

    }

}


def enrich_alert(alert):

    attack = MITRE_MAPPING.get(
        alert["type"]
    )


    if attack:

        alert["mitre_id"] = attack["id"]

        alert["mitre_name"] = attack["name"]

        alert["tactic"] = attack["tactic"]


    return alert