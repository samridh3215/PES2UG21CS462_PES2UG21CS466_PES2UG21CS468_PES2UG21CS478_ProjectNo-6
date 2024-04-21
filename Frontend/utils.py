import subprocess
import json, os
def get_service_port(svc):
    try:
        output = subprocess.check_output(["kubectl", "get", "service", svc, "-o=jsonpath='{.spec.ports[*].nodePort}'"]).decode("utf-8")
        return int(output.replace("'", ""))
    except subprocess.CalledProcessError as e:
        print("Error running kubectl command:", e)
        return None

test = '[{"name": "Oneplus Nord Buds 2", "item_id": 1, "quantity": 21, "price": "2450.00"}, {"name": "IPhone", "item_id": 3, "quantity": 97, "price": "59999.00"}, {"name": "PS5", "item_id": 4, "quantity": 2, "price": "400.00"}]'
def parse_order_json_response(jsonStr):
    dic =  json.loads(jsonStr)
    for i in dic:
        i['add_cart'] = f"http://{os.environ.get('MINIKUBE_IP')}:{get_service_port('order')}/api/add_to_cart/{i['item_id']}"
    return dic
# print(parse_order_json_response(test))

def parse_cart_json_response(jsonStr):
    dic =  json.loads(jsonStr)['cart_items']
    print(dic)
    for i in dic:
        i['remove_cart'] = f"http://{os.environ.get('MINIKUBE_IP')}:{get_service_port('order')}/api/remove_from_cart/{i['item_id']}"
    return dic

# parse_cart_json_response('{"cart_items": [{"name": "Oneplus Nord Buds 2", "item_id": 1, "quantity": 2, "price": "2450.00"}, {"name": "IPhone", "item_id": 3, "quantity": 3, "price": "59999.00"}], "total_price": "184897.00"}')