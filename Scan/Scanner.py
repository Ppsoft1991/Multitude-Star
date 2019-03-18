from .ScanPlugin import CSRF
import sys
import os.path

main_path = sys.path[0]
plugin_path = os.path.join(main_path, 'scan', 'ScanPlugin')


def get_plugin_list():
    if os.path.exists(plugin_path):
        plugin_list = []
        for filename in os.listdir(plugin_path):
            try:
                real_name = filename.split('.')
                if real_name[1] == 'py':
                    if real_name[0][-1] != '_' and real_name[0][0] != '_':
                        plugin_list.append(real_name[0])
            except :
                    pass
        return plugin_list


class Scanner:
    def __init__(self, link, method, certificate, para_type, parameter):
        self.link = link
        self.method = method
        self.certificate = certificate
        self.parameter = parameter
        self.para_type = para_type

        self.Request_function = None
        self.Response_function = None
        for plugin in get_plugin_list():
            one_plugin = __import__(plugin)
            instance = getattr(one_plugin,'Plugin')(link, method, certificate, para_type, parameter)
            reflect = lambda x:getattr(instance, x)
            check_type = reflect('get_info')('check_type')
            if len(check_type) > 1:
                self.Request_function = reflect('inRequest')()
                self.Response_function = reflect('inResponse')()
            elif check_type == 'request':
                self.Request_function = reflect('inRequest')()
            elif check_type == 'response':
                self.Response_function = reflect('inRequest')()
            else:
                self.Request_function = None
                self.Response_function = None

    def inRequest(self):
        if self.Request_function:
            self.Request_function()

    def inResponse(self):
        if self.Response_function:
            self.Response_function()


def csrf(link, method, certificate, para_type, parameter, response):
    return CSRF.CSRF(link, method, certificate, para_type, parameter, response)