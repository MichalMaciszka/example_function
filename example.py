def example_function(element, example_list = []):
    """
    The function appends an element to a list. If no list is provided, it uses a default list.
    However, the default list is mutable, causing it to retain elements added in previous calls,
    when the 'example list' argument is not explicitly provided.

    The behavior occurs because Python evaluates the default argument only once, when the function is defined,
    not during each call. Consequently, the same list shared across all calls to the function, that do not explicitly specify the 'example_list' argument.
    """
    example_list.append(element)
    print(example_list)
