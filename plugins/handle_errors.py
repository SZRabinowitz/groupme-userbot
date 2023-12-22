import time

def on_error(ws=None, error=None, client=None):
    if not Client:
        print("No Valid Client")
    else:
        if error and ws:
            print("ERROR: " + str(error))
            if "Connection to remote host was lost" in str(error):
                print("Restarting....")
                try:
                    client.stop()
                    client.start()
                except Exception as e:
                    client.start()
                except: 
                    time.sleep(5)
                    on_error(ws=ws, error=error, client=client)
        else:
            try:
                client.stop()
                client.start()
            except Exception as e:
                client.start()
            except: 
                time.sleep(5)
                on_error(client=client)