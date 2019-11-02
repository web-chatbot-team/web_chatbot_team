# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\..\..\AppData\Local\Temp'))
	print(os.getcwd())
except:
	pass
# %%

import random


enter_process = ['안녕하세요, 즐거운 식사를 돕는 오늘의 메뉴입니다. 빠르게 주문하고 여유롭게 식사하세요.',
'눈코 뜰 새 없이 바쁜 일과를 보내고 어느새 식사시간이 찾아왔네요. 수고한 여러분을 위해 맛있는 식사 주문 도와 드리는 오늘의 메뉴입니다.',
'안녕하세요, 재충전을 위한 식사 주문을 돕는 오늘의 메뉴입니다. 아무리 바쁘셔도 맛있는 한 끼로 여유를 챙기세요!',
'오늘 마음 어떠신가요? 힘들 때는 나를 위한 맛있는 식사로 기분 업! 어떠세요? 말만 하시면 오늘의 메뉴가 다 주문 해 드리니 걱정 마세요']
print(random.choice(enter_process))

execpt_process = ['아직 공부중이라 모르는 말들이 있어요. 내일은 더 성숙해서 올게요. 제가 알아들을 수 있게 메뉴 이름이나 주문 등 간단하게 말씀 부탁드려요.',
'아직 초보라서 공부중입니다. 모르는 말은 더 배워올게요. 제가 알아들을 수 있게 "주문" "메뉴 이름"처럼 간단하게 말씀 해 주세요.',
'아직 모르는 것들이 많은 초보입니다. 어려운 말은 열심히 공부해서 올게요. 제가 알아들을 수 있게 메뉴 이름이나 주문처럼 간단하게 말씀 해 주시면 감사합니다!']
print(random.choice(execpt_process))

end_process = ['주문 해 주셔서 감사합니다. 남은 하루가 지금보다 더 행복하시길 바라요. 즐거운 식사를 돕는 오늘의 메뉴였습니다.',
'맛있고 향기로운 식사 시간 되세요. 내일도 또 오늘의 메뉴에 들러서 주문해주세요. 감사합니다.',
'저와 함께 한 시간이 즐거우셨으면 좋겠네요. 행복한 식사를 돕는 오늘의 메뉴입니다. 즐거운 하루 보내시고 또 들러주세요.']
print(random.choice(end_process))
# %%



# %%



# %%


