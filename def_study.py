#기본문
def kim():
    print('김정남')

#호출
kim()

#def의 주석, 그런데 int, str, bool 같은 것만 넣어야 한다. 진짜 주석은 아닌듯~
#참조 https://blog.hannal.com/2015/03/keyword-only-arguments_and_annotations_for_python3/
def moon() -> int:
    print('문재인')

#호출
moon()

def args_func(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

args_func('hello', 'world', '!')
args_func('!', arg3='hello', arg2='world')
args_func('world', arg3='!', arg2='hello')
args_func('hello', '!', arg3='world')

def args2_func(arg1, *, arg2, arg3): #함수에 * 표가 있으면 뒤에는 위치인자 arg3='!' 이런식으로 앞에 arg3= 를 꼭 써야 한다.
    print(arg1, arg2, arg3)

args2_func('hello', 'world', '!') #요렇게 하면 에러가 난다. 즉, 위치인자를 꼭 넣어줘야 한다
args2_func('!', arg3='hello', arg2='world')
args2_func('world', arg3='!', arg2='hello')
args2_func('hello', '!', arg3='world')
