from utils import get_service_port
import streamlit as st
import requests
import json
from utils import get_service_port, parse_cart_json_response
import os
from dotenv import load_dotenv
load_dotenv()


st.title("Cart")
ORDER_PORT = get_service_port("order")
CART_URL = f"http://{os.environ.get('MINIKUBE_IP')}:{ORDER_PORT}/api/view_cart/"
CHECKOUT_URL  = f"http://{os.environ.get('MINIKUBE_IP')}:{ORDER_PORT}/api/checkout/"
res = requests.get(url=CART_URL)

dic = parse_cart_json_response(res.text)
for i in dic:
    st.markdown(f"# {i['name']}")
    st.markdown(f"##### Quantitty: {i['quantity']}")
    st.markdown(f"##### Price: {i['price']}")
    if(st.button("Remove from cart", key=f"{i['item_id']}")):
        resp = requests.get(url=f"{i['remove_cart']}")
        if resp.status_code == 200:
            st.success("Removed")

st.divider()
# st.write(unsafe_allow_html='<form><script src="https://checkout.razorpay.com/v1/payment-button.js" data-payment_button_id="pl_NsPk0U0a5F861T" async> </script> </form>')
st.markdown("[Checkout](https://rzp.io/i/13ZkJmQH)")    