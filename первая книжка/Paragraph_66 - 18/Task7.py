# -*- coding: cp1251 -*-

'''
     Напишите рекурсивную версию процедуры replaceAll. Сравните две версии.
     Какую из них вы рекомендуете выбрать и почему?
'''


'''
	Функция замены подстроки в строке, где:
	- s - текст в котором нужно заменить подстроку
	- wOld - подстрока которую нужно заменить
	- wNew - подстрока на которую заменяют старую подстроку
'''
def replaceAll(s, wOld, wNew):
	lenOld = len(wOld);
	res = "";
	while len(s) > 0:
		p = s.find(wOld);
		if p < 0:
			return res + s;
		if p > 0:
			res = res + s[:p];

		res = res + wNew;

		if p+lenOld >= len(s):
			s = "";
		else:
			s = s[p+lenOld:];

	return res;

'''
	Функция замены подстроки в строке, где:
	- s - текст в котором нужно заменить подстроку
	- wOld - подстрока которую нужно заменить
	- wNew - подстрока на которую заменяют старую подстроку
'''
def rec_replaceAll(s, wOld, wNew):
    if not s:
        return ''
    elif s[:len(wNew)] == wNew:
        return wOld + rec_replaceAll(s[len(wNew):], wOld, wNew)
    else:
        return s[0] + rec_replaceAll(s[1:], wOld, wNew)




# тут
s = 'string format'
wOld = 'for'
wNew = 'in'

print('no recursion: ', replaceAll(s, wOld, wNew))
print('recursion: ', rec_replaceAll(s, wOld, wNew))

# рекурсивная функция заменяет первую попавшееся подстроку от начала текста, а обычная первую с конца