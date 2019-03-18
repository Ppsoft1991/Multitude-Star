class IActiveScan:

    def __init__(self, link, method, certificate, para_type, parameter):
        self.link = link
        self.method = method
        self.certificate = certificate
        self.parameter = parameter
        self.para_type = para_type

    def checkVulnerable(self):
        """
        漏洞存在检测
        :return:
        """
        pass


class IPassiveScan:
    pass


class ScanPlugin:

    def __init__(self, link, method, certificate, para_type, parameter, response):
        self.link = link
        self.method = method
        self.certificate = certificate
        self.parameter = parameter
        self.para_type = para_type
        self.response = response

    def plugin_info(self):
        info = {
            "name": "CSRF",
            "info": "template模块",
            "level": "中危",
            "type": "OWASP Top 10",
            "author": "notyeat",
            "url": "",
            "keyword": "tag:aspx",
            "check_type": "request",

        }
        return info

    def get_info(self, get):
        info = self.plugin_info()
        return info[get]

    def inRequest(self):
        pass

    def inResponse(self):
        pass
