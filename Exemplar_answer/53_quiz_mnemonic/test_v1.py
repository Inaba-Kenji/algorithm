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

def phone_mnemonic_v1(phone_number: str) -> List[str]:
    # ハイフンを無くしてint型にする
    phone_number = [int(s) for s in phone_number.replace('-', '')]
    candidate = []
    tmp = [''] * len(phone_number)

    def find_candidate_alphabet(digit: int=0) -> None:
        if digit == len(phone_number):
            # 基本ケース
            candidate.append(''.join(tmp))
        else:
            # 再帰的ケース　phone_numberが('23')の例
            # tmp[0] = A find_candidate_alphabet(0)の時
            # tmp[1] = D find_candidate_alphabet(1)の時
            # tmp[1] = E find_candidate_alphabet(1)の時
            # tmp[1] = F find_candidate_alphabet(1)の時

            # tmp[0] = B find_candidate_alphabet(0)の時
            # tmp[1] = D find_candidate_alphabet(1)の時
            # tmp[1] = E find_candidate_alphabet(1)の時
            # tmp[1] = F find_candidate_alphabet(1)の時

            # tmp[0] = C find_candidate_alphabet(0)の時
            # tmp[1] = D find_candidate_alphabet(1)の時
            # tmp[1] = E find_candidate_alphabet(1)の時
            # tmp[1] = F find_candidate_alphabet(1)の時

            # 再帰的ケース
            for char in NUM_ALPHABET_MAPPING[phone_number[digit]]:
                tmp[digit] = char
                find_candidate_alphabet(digit+1)

    find_candidate_alphabet()
    return candidate

if __name__ == '__main__':
    for s in phone_mnemonic_v1('568-379-8466'):
        if 'LOVEPYTHON' in s:
            print(s)
