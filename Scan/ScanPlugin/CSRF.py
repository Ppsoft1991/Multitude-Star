from .. IScanObject import ScanPlugin


class Plugin(ScanPlugin):

    def plugin_info(self):
        info = {
            "name": "CSRF",
            "info": "众星的CSRF模块可以检测敏感信息的CSRF",
            "level": "中危",
            "type": "OWASP Top 10",
            "author": "notyeat",
            "url": "",
            "keyword": "tag:aspx",
            "check_type": "request",

        }
        return info


    def inRequest(self):
        print(2)

    def inResponse(self):
        pass