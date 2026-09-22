def array_of_names(dict):
    names = [key + " " + value for key, value in dict.items()]
    return names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))