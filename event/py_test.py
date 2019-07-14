

""" selected = {'hall': {'id':'svg_1' , 'price': '1000'}"""


def add(hall, event):

    selected = {}

    if len(hall) > 1:

        for id in hall:
            selected[id] = {'id': id, 'price': 1000}

    return selected
