def html_formatter(data):
    if isinstance(data, list):
        for item in data:
            print("<h1>{}</h1><p>Address: {}</p><p>Phone Number: {}</p>".format(item.name, item.address, item.phone_number))
    else:
        print("<h1>{name}</h1><p>Address: {address}</p><p>Phone Number: {phone_number}</p>".format(**data))
