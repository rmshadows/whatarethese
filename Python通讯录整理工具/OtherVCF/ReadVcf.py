# https://cloud.tencent.com/developer/article/1593403
import sys
import os
import subprocess

class Record(object):
    '''
    One line information in vcf file
    '''
    def __init__(self, line):
        info = line.split("\t")
        self.line = line
        self.CHROM =  info[0] 
        self.POS = info[1]
        self.ID = info[2]
        self.REF = info[3]
        self.ALT = info[4]
        self.QUAL = info[5]
        self.FILTER = info[6]
        self.INFO = [{pair_lst[0]: pair_lst[1] if len(pair_lst)> 1 else ""} for pair_lst in [pair.split("=") for pair in info[7].split(";")]]
        self.FORMAT = info[8].split(":")
        self.sample_num = len(info) -7
        self.GT = []
        for i in range(2):
           GT_value = info[8 + i +1].split(":") 
           GT_dict = {}
           for g in range(len(GT_value)):
               GT_dict[self.FORMAT[g]] = GT_value[g] 
           self.GT.append(GT_dict) 
      

class VCF(object):
    '''
    VCF class, read VCF, write VCF, get VCF information
    '''
    def __init__(self, uncompress_vcf):
        self.header = []
        self.reader = open(uncompress_vcf, 'r')
        self.line = self.reader.readline().strip()
        while self.line.startswith('#'):
            self.header.append(self.line)
            self.line = self.reader.readline().strip()
        self.record = Record(self.line) 
    def __iter__(self): 
        return self 
    def __next__(self): 
        self.line = self.reader.readline().strip()
        if self.line != "":
            self.record = Record(self.line) 
            return self.record
        else:
            self.reader.close()
            raise StopIteration()
    def reader_close(self):
        self.reader.close()   
