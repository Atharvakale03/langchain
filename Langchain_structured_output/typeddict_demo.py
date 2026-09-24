from typing import TypedDict

class Person(TypedDict):
 
 name : str
 age : int

new_person: Person = {
 "name": "Alice",
 "age": "30"#typped dict overwrites the type checking int as str where as normal dict would not
}

print(new_person)
