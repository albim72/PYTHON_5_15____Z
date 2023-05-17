from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State','new running sleeping restart zombie')

class User:
    pass

class Process:
    pass

class File:
    pass


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self,restart=True):
        pass

class FileServer(Server):

    def __init__(self):
        self.name = "FileServer"
        self.state = State.new

    def boot(self):
        print(f'Booting {self}')
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        self.state = State.restart if restart else State.zombie

    def create_file(self,user,name,permissions):
        print(f"próba utworzenia pliku {name} dla użytkownika {user} z uprawnieniami: {permissions}.")


class ProcessServer(Server):

    def __init__(self):
        self.name = "ProcessServer"
        self.state = State.new

    def boot(self):
        print(f'Booting {self}')
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        self.state = State.restart if restart else State.zombie

    def create_process(self,user,name):
        print(f"próba utworzenia procesu {name} dla użytkownika {user}.")

class WindowsServer:
    pass

class NetworkServer:
    pass

class OperatingSystem:
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs,self.ps)]

    def create_file(self,user,name,permissions):
        return self.fs.create_file(user,name,permissions)

    def create_process(self,user,name):
        return self.ps.create_process(user,name)

def main():
    os = OperatingSystem()
    os.start()
    os.create_file('nowy','hello','-rw-r-r')
    os.create_process('big','ls/tmp')

if __name__ == '__main__':
    main()
