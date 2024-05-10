personal_info = ["John", "Doe", 30]

def print_p_info(institution, *args):
    print(args)
    print( f"Name: {args[0]} {args[1]}, Age: {args[2]}, Institution: {institution}" )


personal_info_dict = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}

def print_p_info_dict(institution, **kwargs):
    print(kwargs)
    print( f"Name: {kwargs['first_name']} {kwargs['last_name']}, Age: {kwargs['age']}, Institution: {institution}" )


# ---------------------------------------------------------

def student_registration(first_name, last_name, age):
    print( f"Student: {first_name} {last_name}, Age: {age}" )

student_registration(**personal_info_dict)
