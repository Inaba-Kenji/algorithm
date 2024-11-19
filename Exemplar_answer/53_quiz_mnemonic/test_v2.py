"""
Input 568-379-8466 Output [..., 'LOVEPYTHON', ... ]
Input 435-569-6753 Output [..., 'HELLOWORLD', ...]
"""

from typing import List

NUM_ALPHABET_MAPPING = {
    0: '+',
    1: '@',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}

def phone_mnemonic_v2(phone_number: str) -> List[str]:
    # ハイフンを無くしてint型にする
    phone_number = [int(s) for s in phone_number.replace('-', '')]
    candidate = []
    # len()で１にするため['']
    stack = ['']

    # 初期値のlen(stack)は1になるのでループに入る
    while len(stack) != 0:
        alphabets = stack.pop()
        # 長さが同じということは、正解の候補の一つになるため追加の処理を行う
        if len(alphabets) == len(phone_number):
            candidate.append(alphabets)
        else:
            # (1).A,B,Cがstackに追加される
            # (2).末尾のCの組み合わせを追加する（例：CD,CE,CF)
            # (3).その後は,上記の(1)と(2)をlenの長さが同じになるまで繰り返す((例：CFG,CFH,CFI)
            for char in NUM_ALPHABET_MAPPING[phone_number[len(alphabets)]]:
                stack.append(alphabets + char)
    return candidate

# if __name__ == '__main__':
#     for s in phone_mnemonic_v2('234'):
#             print(s)

if __name__ == '__main__':
    for s in phone_mnemonic_v2('435-569-6753'):
        if 'HELLOWORLD' in s:
            print(s)
