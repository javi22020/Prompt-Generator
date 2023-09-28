import random as rn
import yaml

# Add your own adjectives, objects and styles to the yaml file!

def random_prompt(numadjectives, numstyles):
    with open("words.yaml", "r") as file:
        data = yaml.safe_load(file)
    adjectives = data["adjectives"]
    objects = data["objects"]
    styles = data["styles"]
    listadj = rn.sample(adjectives, numadjectives)
    adj = ', '.join(listadj)
    obj = rn.choice(objects)
    prompt = adj + ' ' + obj
    liststyles = rn.sample(styles, numstyles)
    sty = ', '.join(liststyles)
    prompt = prompt + ', ' + sty
    return prompt
