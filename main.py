import random

from termcolor import colored

d = {
  'apple':'りんご',
  'banana':'バナナ',
  'peach':'もも'
}

template = '*'*15 + '\n英単語:{}\n日本語訳を入力してください:\n' + '*'*15

while True:
  # 英単語を表示
  word = random.choice(list(d.keys()))
  print(colored(template.format(word),'yellow'))

  # 自分が日本語を入力する
  answer = input()

  # 自分が入力した日本語と、答えがあっているかを確認する
  if answer == '0':
    print('終了します')
    break
  elif answer == d[word]:
    print(colored('正解', 'green'))
  else:
    print(colored('不正解', 'red'))