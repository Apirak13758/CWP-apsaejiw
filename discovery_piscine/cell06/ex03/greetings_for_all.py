def greetings(string = None):
    if string == None:
        print("Hello, noble stranger.")
        return
    if not isinstance(string, str):
        print("Error! It was not a name.")
        return
    print(f"Hello, {string}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)