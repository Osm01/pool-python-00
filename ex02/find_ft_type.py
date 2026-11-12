
def all_thing_is_obj(object: any) -> int:
    container = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict"}
    if type(object) in container:
        print(f"{container[type(object)]} : {type(object)}")
    elif type(object) is str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42
