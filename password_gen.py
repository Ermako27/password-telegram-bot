import random
from passwordmeter import test # проверка мощности пароля

def rnd_position(length):
	random.seed()
	random_choice = random.randint(0, length - 1)
	return random_choice

def password_generate(): # генерация случайного пароля

	i = j = 0
	groups_of_chars = ['qwertyuiopasdfghjklzxcvbnm','1234567890', 'QWERTYUIOPASDFGHJKLZXCVBNM', '!?.@#$&']
	password_chars = ['' for i in range(12)]

    # цикл обеспечивает наличие хотя бы 1 символа из каждой группы
    # пока не будут заполнены 4 пустые позиции 
    # (не for, так как может выпасть индекс уже занятой позиции, и элемент не будет добавлен)
	while i != 4:
		one_position = rnd_position(12) # случайно выбирается место для элемента
		index_of_char = rnd_position(len(groups_of_chars[i])) # номер символа в группе симоволов
		if password_chars[one_position] == '': # если позиция в пароле еще пуста
			password_chars[one_position] = groups_of_chars[i][index_of_char]
			i += 1

	while j != 8:
		one_position = rnd_position(12)
		index_of_group = rnd_position(4) # номер группы, из которой выбирается символ
		index_of_char = rnd_position(len(groups_of_chars[index_of_group]))
		if password_chars[one_position] == '':
			password_chars[one_position] = groups_of_chars[index_of_group][index_of_char]
			j += 1


	password = ''.join(password_chars) # сборка пароля в виде строки из массива символов

	return password

def main():
	pass_str = password_generate()
	strength,_ = test(pass_str)

	print("\nPassword: ", pass_str)
	print("Strength: ", strength)




 

if __name__ == '__main__':
	main()
	#password_generate()