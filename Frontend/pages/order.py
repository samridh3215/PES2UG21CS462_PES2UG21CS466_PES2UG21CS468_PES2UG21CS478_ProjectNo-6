from utils import get_service_port
import streamlit as st
import requests
import json
from utils import parse_order_json_response
import os
from dotenv import load_dotenv
load_dotenv()
############# 

ORDER_PORT = get_service_port("order")
request_url=f"http://{os.environ.get('MINIKUBE_IP')}:{ORDER_PORT}/api/items/"
# st.write("Requesting URL: "+request_url)
if st.button("View Cart", key="cart_view"):
    st.switch_page("pages/cart.py")
# st.markdown(f"[View Cart](http://{os.environ.get('MINIKUBE_IP')}:{ORDER_PORT}/api/view_cart/)")
st.title("Items")
st.divider()
res = requests.get(url=request_url)
dic = parse_order_json_response(res.text)
for i in dic:
    st.markdown(f"# {i['name']}")
    st.markdown(f"##### Quantitty: {i['quantity']}")
    st.markdown(f"### Price: {i['price']}")
    if(st.button("Add to cart", key=f"{i['item_id']}")):
        resp = requests.get(url=f"{i['add_cart']}")
        if resp.status_code == 200:
            st.success("Added")
        
    # st.markdown(f"[AddToCart]({i['add_cart']})")



