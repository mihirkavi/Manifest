class Idea:
    def __init__(self, name, *args, **kwargs):
        print('Idea Object created.')
        self.name = name  # First argument is mandatory and assigned to 'name'
        self.description = args[0] if args else None  # Optional second argument
        self.kwargs = kwargs

