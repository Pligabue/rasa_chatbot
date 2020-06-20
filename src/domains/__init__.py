from functools import reduce
from os import listdir, path
from pathlib import Path
import yaml

def run():
    current_dir = Path(__file__).resolve().parent

    yaml_file_list = current_dir.glob("*.yml")

    partial_domains = []
    for file_name in yaml_file_list:
        with open(file_name, "r") as file:
            partial_domains.append(yaml.safe_load(file))

    partial_domains = filter(None, partial_domains)

    initial_domain = {
        "intents": [],
        "entities": [],
        "slots": {},
        "responses": {},
        "forms": [],
        "session_config": {}
    }

    def merge_domains(previous_dom, current_dom):
        for key in current_dom:
            if key in ["intents", "entities", "forms"]:
                previous_dom[key] = list(sorted(set(previous_dom[key] + current_dom[key]), key=str.lower))
            elif key in ["slots", "responses", "session_config"]:
                previous_dom[key] = {**previous_dom[key], **current_dom[key]}
        return previous_dom

    final_domain = reduce(merge_domains, partial_domains, initial_domain)
    
    destination_file = current_dir.parent / "domain.yml"
    with open(destination_file, "w") as file:
        yaml.dump(final_domain, file, allow_unicode=True)

if __name__ == "__main__":
    run()