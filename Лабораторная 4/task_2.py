# TODO решите задачу
import json

def task() -> float:
    with open('input.json') as file:
        data = json.load(file)

    product_sum = sum(item['score'] * item['weight'] for item in data)
    rounded_sum = round(product_sum, 3)

    return rounded_sum


print(task())
