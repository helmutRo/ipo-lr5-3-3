with open("text.txt", 'r') as file: #открывает файл
  x = file.read().split() #читает файл и разбирает строку на колво подстрок
print(f"колво слов в файле: {len(x)}") #вывводит строку с колвом
