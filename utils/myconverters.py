"""名字 转换器"""
import re


class UsernameConverter:
    regex = '[a-zA-Z0-9_-]{5,20}'

    def to_python(self, value):
        print(value)

        return value

    def to_url(self, value):
        print("to_url>>>")
        return value




"""手机号 转换器"""
class PhoneConverter:
    regex = "1[345789]\d{9}"

    def to_python(self, value):
        print(value)
        return value

    def to_url(self, value):
        return value

