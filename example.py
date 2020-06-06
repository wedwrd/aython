from aython import aython
from http.server import HTTPServer

def intent_handler(): # set up what to do with the intents recieved
    if aython.alexa.intent_name == "Hello":
        auth_code= aython.alexa.auth_code() # if an auth code is sent get it
        aython.alexa.reply_message = alexa.build_speech_response("World") # replys with World

def main():
    port = 5000
    aython.alexa.intent_function = intent_handler # assighns the intent handler
    server = HTTPServer(("localhost", port),aython.alexa) # creates the server
    print(f"Server started at localhost:{port}")
    server.serve_forever() # starts the server

if __name__=="__main__":
    main()
