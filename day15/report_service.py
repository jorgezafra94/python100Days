"""
this service will be in charge of:
* creating report about amounts of resources
"""


def report(resources, profit):
    for k, v in resources.items():
        message = f'{k}: {v}ml'
        if k == 'coffee':
            message = message.replace("ml", "g")
        print(message)

    print(f"profit: ${profit}")
