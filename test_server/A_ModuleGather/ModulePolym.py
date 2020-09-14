'''
python多态
python是没有特定的语法去实现多态的，但是可以自定义方法
总体：同一个接口多种形态


'''


class Animal:
	def __init__(self, name):
		self.name = name

	def talk(self):
		print('动物类')

	@staticmethod # 静态方法
	def animal_talk(obj):
		obj.talk()

	@staticmethod
	def animal_motion(obj):
		obj.motion()


class Cat(Animal):	
	def talk(self):
		print(self.name)

	def motion(self):
		print('Cat_motion:', self.name)


class Dog(Animal):
	def talk(self):
		print(self.name)

	def motion(self):
		print('Dog_motion:', self.name)


# 正常调用
# a = Animal
# c = Cat(a)
# c.talk()
#
# c = Dog(a)
# c.talk()


# 未实现(未解)
# animals = [Cat('Missy'),Dog('Lassie')]
#
# for i in animals:
# 	i.name +':'+ i.talk()

# 多态调用
c = Cat('Meow!')
d = Dog('Woof Woof!')

Animal.animal_talk(c)
Animal.animal_motion(d)
Animal.animal_motion(c)
