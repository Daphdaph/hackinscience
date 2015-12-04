def sort_a_list(list):
    return(sorted(list, reverse=True))


def sort_by_mark(grades):
    return(sorted(grades, reverse=True))


def sort_by_name(my_class):
    from operator import itemgetter
    return(sorted(my_class, key=itemgetter(1)))
