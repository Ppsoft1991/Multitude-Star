from Scan import Scanner
import sys
import os


def CheckDomain(domain):
    pass


def Spider(domain):
    pass


def Scan(link, method, certificate):
    pass

def main():
    link = 'http://www.baidu.com'
    method = 'GET'
    certificate = 'Cookie'
    para_type = 'basic'
    parameter = 'userid'
    response = None
    csrfr = Scanner.csrf(link, method, certificate, para_type, parameter, response)
    print(csrfr.get_info('info'))


if __name__ == '__main__':
    reflect = __import__('reflect')
    A = getattr(reflect, 'A')('zhangsan')
    say = getattr(A, 'say')()
    print(say)

    #main()