#!/usr/bin/python
# -*- coding: utf-8 -*-
class codemapping:
    def __init__(self):
        mapping={}
        mapping['f0']="一般学习模式"
        mapping['f1']="空调学习模式"
        mapping['f2']="退出学习模式"
        mapping['00']="成功"
        mapping['ff']="失败"
        self.mapping=mapping
    def codetomsg(self,code):
        if code in self.mapping:
            return self.mapping[code]
        else:
            return 'unknown'
        pass
    def msgtocode(self,txt):
        pass

