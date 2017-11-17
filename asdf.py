import string
import zipfile

chars = string.ascii_lowercase
# chars = 'abcde'


def add_char_to_list(ori_list=None):
    # 0개일때 -> 5번 반복
    # a, b, c, d, e

    # 5개일때 -> 5 * 5번 반복
    # aa, ab, ac, ad, ae
    # ba, bb, bc, bd, be
    # ca, cb, cc, cd, ce
    # da, db, dc, dd, de
    # ea, eb, ec, ed, ee

    # 25개일때 -> 25 * 5번 반복
    # aaa, aab, aac, aad, aae
    # baa, bab, bac, bad, bae

    if not ori_list:
        return list(chars)

    ret = []
    for char in chars:
        for item in ori_list:
            ret.append(char + item)
    return ret


def brute_force(path):
    # password에 a~z까지의 문자로 이루어진 특정 길이의 문자열 전달
    # 만약 3글자라면
    # a, b, c, d, ....z, aa, ab, ac, ad, ...az, aaa, aab, aac.... zzz
    # 검색 완료 후 걸린 시간을 리턴

    # 1개 일때 = n번
    # 1, 2, 3, 4, 5

    # 2개 일때 = n * n번
    #   11, 12, 13, 14, 15,
    #   21, 22, 23, 24, 25,
    #   31, 32, 33, 34, 35.
    #   ... 11~55까지 = n * n번

    # 3개 일때 = n * n * n번
    #       111, 112, 113, 114, 115,
    #       121, 122, 123, 124, 125,
    #       ....111~155까지 = n * n번
    #       211, 212, 213, 214, 215,
    #       ....211~255까지 = n * n번
    #       ....311~555까지 = n * n + 3번
    #                           => n * n * n번
    l = []
    count = 0
    i = 0
    while True:
        i += 1
        print(f'Loop {i}')
        l = add_char_to_list(l)
        for item in l:
            print(f'try: {count}, value: {item}')
            count += 1

            try:
                with zipfile.ZipFile(path) as z:
                    z.setpassword(bytes(item, encoding='ascii'))
                    z.extract('origin.txt')
                return
            except RuntimeError:
                pass

            # if item == password:
            #     print(f'Password is {item}')
            #     return
        # 만들어져야 하는 문자열의 길이는 i
        # 만약 3일 경우, aaa ~ zzz

        # 길이횟수만큼 반복
        # 1번째에 첫 번째 문자를 만듬
        # 2번째에 만든 문자에 문자를 붙임
        # 3번째에 2번째에 만든 문자에 문자를 붙임
        # 이걸 n번만큼 반복

        # i + 1까지 반복하면 3일 경우 x에 1, 2, 3이옴

