#!/usr/bin/env python


class BaseExtension:
    name = ''
    basePath = 'extensions/'
    def __init__(self):
        self.name = ''



    def excute(form_dict):
        return    

    def check(self, form_dict):
        return True

    def formatFileName(self, fileName):
        while (fileName.find('/') != -1) :
            fileName = fileName[fileName.find('/') + 1 :].strip()
        return fileName