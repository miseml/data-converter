def text_formatter(data):
    if isinstance(data, list):
        for item in data:
            print("Name: {}\nAddress: {}\nPhone Number: {}".format(item.name, item.address, item.phone_number))
    else:
        print("Name: {name}\nAddress: {address}\nPhone Number: {phone_number}".format(**data))
