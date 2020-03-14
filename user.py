
from werkzeug import generate_password_hash, check_password_hash


class User:
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password_hash = self.save_password(password)


	def check_email(self, email):
		return self.email == email


	def save_password(self, password):
		# TODO
		return generate_password_hash(password)


	def check_password(self, password):

		# TODO
		return check_password_hash(self.password_hash,password)




def main():

	userList = [] #创建用户列表
	print('---------欢迎---------')
	while 1:
		choose = int(input('''
		请选择：
		1.注册
		2.登录
		3.退出
		'''))
		if choose == 1:
			print(' 请输入:')
			name = input('name:')
			email = input('email:')
			password = input('password:')

			#TODO
			newUser = User(name,email,password)
			userList.append(newUser)
			print('注册成功!')


		if choose == 2:

			print(' 请输入:')
			email = input('email:')
			password = input('password:')

			# TODO
			TAG = 0
			for user in userList:
				if(user.check_email(email)):
					TAG =1
					if(user.check_password(password)):
						print('登录成功！')
					else:
						print('密码错误！')
                    break
			if(TAG == 0):
				print('用户名错误！')

		if choose == 3:
			break


if __name__ == '__main__':
	main()
