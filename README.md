Summary
-
pyWebsocket is a Flask app to demonstrate Websocket server & client examples that synchronizes state across clients
Demo Clients : Android (WebSocket) and JS (Open js_client.html with a browser)

Overall flow
Client -> Send message via browser and/or Android-> Python Flask App -> Send the response back to all the connected clients

--------------------------------------------------

Environment
-
Python 3.7.6

Required packages to install:
pip install -r requirements.txt

Additional requirements

ngrok (Included) more info: https://ngrok.com/


To run
- Check that your python version is 3.X
- Install the required packages
- python server.py
- Open another terminal window
- ./ngork http <PYTHON SERVER PORT>
- After ngrok is running properly.  Copy ngrok url to JS and Android client

To use

- Open js_client.html file with multiple tabs or windows on the browsers.
- Click a button, you will see the displayed value is all synced
- With Android app, you can see browser gets updated itself.
- Console for the server will also print the value out.


*There is also a simple version
server_simple_counter.py
js_simple_counter.html 

