from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def use_subject(self) -> None:
        pass

class RealSubject(Subject):
    def use_subject(self) -> None:
        print('Subject: Real object was used!!')

class ProxySubject(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self.subject = real_subject
    
    def use_subject(self) -> None:
        if self.check_access():
            self.subject.use_subject()
            self.log_access()
        pass

    def check_access(self) -> bool:
        print('Proxy: Check permission before access')
        return True
    
    def log_access(self) -> None:
        print('Proxy: Logging access to real object')