class common(object):
    """docstring for common."""
    def __init__(self):
        super(common, self).__init__()

    def search_array(self, array, search):
        try:
            array_index = array.index(search)
            return array[array_index + 1]
        except Exception as e:
            print('Property ' +search+' not found in ' + str(array))
            return 'No such command'
