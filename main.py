MyName = ""

def on_forever():
    global MyName
    MyName = "Hello Me"
    basic.show_string(MyName)
basic.forever(on_forever)
