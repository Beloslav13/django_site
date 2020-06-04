try:
    from blogengine.signals.handlers import posts
except AttributeError as e:
    # initial migrations hack
    print(e.args)