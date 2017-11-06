#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '学生资料'
   empCount = 1
 
   def __init__(self, name,number,classnumber,gender):
      self.name = name
      self.studentnumber = number
      self.classnumber = classnumber
      self.gender = gender
      Student.empCount += 1
   
   def speakEnglish(self):
     print self.name,"can speak English!!!"
 
   def canWriting(self):
      print self.name,"can Writing!!!"

   def canSwiming(self):
      print self.name,"can Swiming!!!"
