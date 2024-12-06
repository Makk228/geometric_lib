import circle
import square
import rectangle
import triangle


figs = ['circle', 'square','rectangle','triangle']
funcs = ['perimeter', 'area']
sizes = {
        'per-circle':1,
        'per-square':1,
        'per-rectangle':2,
        'per-triangle':3,

        'area-circle':1,
        'area-square':1,
        'area-rectangle':2,
        'area-triangle':3
}

def calc(fig, func, size):
	if any(isinstance(s,str) for s in size):
		return
	elif all(int(s)>=0 for s in size):
		assert fig in figs
		assert func in funcs

		result = eval(f'{fig}.{func}(*{size})')
		return result
	else:
		print("argument error, argument must be positive int")
		
if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	result = calc(fig, func, size)



