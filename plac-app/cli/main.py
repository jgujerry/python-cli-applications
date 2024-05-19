import os
import shelve
import plac
from safekey.app import SafeKey


class ShelveInterface(object):
    "A minimal interface over a shelve object."
    commands = 'add', 'get', 'list', 'update', 'remove'

    @plac.annotations(configfile=('path name of the shelve', 'option'))
    def __init__(self, configfile):
        self.configfile = configfile or 'conf.shelve'
        self.fname = os.path.expanduser(self.configfile)
        self.__doc__ += ('\nOperating on %s.\nUse help to see '
                         'the available commands.\n' % self.fname)

    def __enter__(self):
        self.sh = shelve.open(self.fname)
        return self

    def __exit__(self, etype, exc, tb):
        self.sh.close()
    
    def add(self, appname, username, password):
        """Add new password"""
        sk = SafeKey()
        print(sk.add_password(appname, username, password))
    
    def get(self, appname):
        """Get the password"""
        sk = SafeKey()
        print(sk.get_password(appname))
    
    def list(self):
        sk = SafeKey()
        print(sk.list_passwords())
    
    def update(self, appname, new_password):
        sk = SafeKey()
        print(sk.update_password(appname, new_password))
    
    def remove(self, appname):
        sk = SafeKey()
        print(sk.remove_password(appname))
    
    def set(self, name, value):
        "set name value"
        yield 'setting %s=%s' % (name, value)
        self.sh[name] = value

    def show(self, *names):
        "show given parameters"
        for name in names:
            yield '%s = %s' % (name, self.sh[name])  # no error checking

    def showall(self):
        "show all parameters"
        for name in self.sh:
            yield '%s = %s' % (name, self.sh[name])


def main():
    plac.Interpreter(plac.call(ShelveInterface)).interact()



if __name__ == '__main__':
    main()
