class API(object):
    def __init__(self, auth):
        self._auth = auth

    @property
    def auth(self):
        return self._auth



class Wrapper():
    # allow only one instance of Wrapper
    class __Wrapper(API):

        def __init__(self, auth):
            super().__init__(auth)

        def get_user_data(self, user):
            print(f"{user}'s data")

    def __new__(cls):
        if not hasattr(cls, 'api'):
            auth = 'generated'
            Wrapper.api = cls.__Wrapper(auth)
        return Wrapper.api
