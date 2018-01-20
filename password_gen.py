import random
from passwordmeter import test

def rnd_position(length):
	random.seed()
	random_choice = random.randint(0, length - 1)
	return random_choice

def password_generate():

	groups_of_chars = ['qwertyuiopasdfghjklzxcvbnm','1234567890', 'QWERTYUIOPASDFGHJKLZXCVBNM', '!?.@#$&']
	password = ''
	for i in range(12):
		index_of_group = rnd_position(100) % 4
		index_of_char = rnd_position(len(groups_of_chars[index_of_group]))
		password += groups_of_chars[index_of_group][index_of_char]

	strength,_ = test(password)
	if strength < 0.5:
		password = password_generate();
	else:
		return password

def main():
	pass_str = password_generate()
	strength,_ = test(pass_str)

	print("\nPassword: ", pass_str)
	print("Strength: ", strength)




 

if __name__ == '__main__':
	main()