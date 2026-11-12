

def NULL_not_found(object: any) -> int:
    t_obj = type(object)
    if object is None:
        print(f"Nothing : None {t_obj}")
        return 0
    if t_obj is int and object == 0:
        print(f"Zero : 0 {t_obj}")
        return 0
    if t_obj is bool and object is False:
        print(f"Fake : False {t_obj}")
        return 0
    if t_obj is str and object == "":
        print(f"Empty : {t_obj}")
        return 0
    if t_obj is float and object != object:
        print(f"Garlic : nan {t_obj}")
        return 0
    print("Type not Found")
    return 1
