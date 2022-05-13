def get_option(option, options, default):
    if option in options:
        return options[option]
    else:
        return default
