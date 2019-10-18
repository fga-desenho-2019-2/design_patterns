from art import *
from subjects import *

def call_subject(subject: Subject) -> None:
    subject.use_subject()

if __name__ == '__main__':
    art_1 = text2art('Hello Proxy!')
    print(art_1)

    print('Client: Calling subject out of proxy')
    real_subject = RealSubject()
    call_subject(real_subject)

    print('Client: calling subject from proxy')
    proxy = ProxySubject(real_subject)
    call_subject(proxy)