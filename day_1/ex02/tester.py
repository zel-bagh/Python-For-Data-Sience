from find_ft_type import all_thing_is_obj


def main():
    ft_list = ["Hello", "World!"]
    ft_tuple = ("Hello", "Morocco!")
    ft_set = {"Hello", "simplon!"}
    ft_dict = {"Hello": "1337 Benguerir!"}

    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Hello")
    print(all_thing_is_obj(42))


if __name__ == "__main__":
    main()
