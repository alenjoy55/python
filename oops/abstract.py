from abc import ABC,abstractmethod
class syn(ABC):
    @abstractmethod
    def reg(self):
        pass
    def python(self):
        print('python')
    def php(self):
        print('php')

class staff(syn):
    def reg(self):
        print('staff dtls')
    def notes(self):
        print('notes')

class std(syn):
    def reg(self):
        print('std dtls')
    def id_card(self):
        print('id card')

# staff1=staff()
# staff1.reg()

# std1=std()
# std1.reg()
# std1.id_card()