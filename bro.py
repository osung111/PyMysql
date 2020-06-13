import numpy
from matplotlib import pyplot as plt
import pandas
import pymysql
import sys

class Big:
	def __init__ (self,name) :
		self.name = name	
		print("Create 데이터 생성")
		print("Edit 데이터 수정")
		print("View 데이터 조회")
		print("Del 데이터 삭제")
		print("4:이름으로 연봉 순위")	
		print("Exit 종료")
		print(self.name)
		
	def create(self):
		conn = pymysql.connect(host='localhost',user='root',password='111111','db'=python,charset='utf8')
		cur = conn.cursor()

		print(self.name+"dsa")
		print('이름,나이,주소,이메일,직업,월급')
		self.name = input("이름은?")
		self.age = int(input("나이는?"))
		self.add = input("주소는?")
		self.email = input("이메일?")
		self.job = input("직업?")
		self.money = input("월급?")
		sql ="insert into data(name,age,address,email,job,money) values()"		
		cur.execute(sql)
		conn.commit()
		conn.close()
	
		

		


bro = Big("브로")
bro.create()
	

//누구누구의 테이블 이닛으로 만들기 create table 형식은 그대로

//테이블 블러오기