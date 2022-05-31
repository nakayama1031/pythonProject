import csv
import string

import pandas as pd
from termcolor import colored

global shop
global fieldnames


class LoboterMessage():

    def __init__(self, name):
        self.name = name

    def firstMessage():
        fastMessgae = """\
        =============================
        こんにちわ。私はロボ子です。あなたのお名前を教えてください。
        =============================
        """

        print(colored(fastMessgae, 'green'))

    def say_something(self, maxShop):
        recommendationShop = (f"""
        =================================z==============
        {self.name} さん
        私のお勧めのお店は{maxShop} です。
        このレストランはお好きですか？(yes/or/no)
        ===============================================
        """)
        print(colored(recommendationShop, 'green'))

    def last__message(self):
        lastMessage = (f"""
        ===============================================
        {self.name} さん。有難うございました。
        良い一日を。さようなら。
        ===============================================
        """)

        print(colored(lastMessage, 'green'))


def say_name():
    name = input()

    if not name:
        LoboterMessage.firstMessage()

    while True:

        name = input()
        count = 0

        if name:

            while count <= 1:

                if count == 0:

                    with open('ranking.csv', 'r', encoding="utf-8") as csv_file:
                        reader = csv.DictReader(csv_file)

                        for row in reader:
                            if row['shop']:
                                df = pd.read_csv('ranking.csv')
                                maxShop = df.iat[df['shopCount'].idxmax(), 0]

                                # print(maxShop)

                                LoboterMessage(name)
                                LoboterMessage.say_something(name, maxShop)

                                break

                    with open('ranking.csv', 'r', encoding="utf-8") as csv_file:
                        reader = csv.DictReader(csv_file)
                        for row in reader:
                            if row['shop']:

                                judgement = input()

                                if judgement == 'yes':
                                    shopCount = int(row['shopCount'])

                                    shopCount += 1

                                    df = pd.read_csv('ranking.csv')
                                    test = df[df['shop'] == maxShop]

                                    if not test.empty:
                                        addCount = 1
                                        df = pd.read_csv('ranking.csv')
                                        test = df[df['shop'] == maxShop]
                                        total = test['shopCount'] + addCount

                                        maxShop = string.capwords(maxShop)
                                        df.at[df['shop'] == maxShop, 'shopCount'] = total
                                        df.to_csv("ranking.csv", index=False)

                                    else:
                                        with open('ranking.csv', 'w', newline="", encoding="utf-8") as csv_file:
                                            fieldnames = ['shop', 'shopCount']
                                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                            writer.writeheader()
                                            row['shop'] = string.capwords(row['shop'])
                                            writer.writerow({'shop': row['shop'], 'shopCount': shopCount})

                                    lastMessage = (f"""
                                    ===============================================
                                    {name} さん。有難うございました。
                                    良い一日を。さようなら。
                                    ===============================================
                                    """)

                                    print(colored(lastMessage, 'green'))

                                    return

                                else:

                                    df = pd.read_csv('ranking.csv')
                                    rows = df.sort_values('shopCount', ascending=False)
                                    idx = len(rows)

                                    i = 1
                                    # print(idx -1)

                                    while i < idx:

                                        rowsShop = rows.loc[rows.index[i], "shop"]
                                        recommendationShop = (f"""
                                        ===============================================
                                        {name} さん
                                        私のお勧めのお店は{rowsShop} です。
                                        このレストランはお好きですか？(yes/or/no)
                                        ===============================================
                                        """)

                                        print(colored(recommendationShop, 'green'))

                                        judgement = input()

                                        if judgement == 'yes':
                                            testCount = rows.loc[rows.index[i], "shopCount"]
                                            total = int(testCount) + 1
                                            rowsShop = string.capwords(rowsShop)
                                            df.at[df['shop'] == rowsShop, 'shopCount'] = total
                                            df.to_csv("ranking.csv", index=False)

                                            lastMessage = (f"""
                                            ===============================================
                                            {name} さん。有難うございました。
                                            良い一日を。さようなら。
                                            ===============================================
                                            """)

                                            print(colored(lastMessage, 'green'))

                                            return

                                        else:
                                            i = i + 1

                                    whereShop = (f"""
                                    ===============================================
                                    {name} さん。どこのレストランが好きですか？ 
                                    ===============================================
                                    """)

                                    print(colored(whereShop, 'green'))

                                    shop = input()

                                    lastMessage = (f"""
                                    ===============================================
                                    {name} さん。有難うございました。
                                    良い一日を。さようなら。
                                    ===============================================
                                    """)

                                    print(colored(lastMessage, 'green'))

                                    addCount = 1

                                    df = pd.read_csv('ranking.csv')
                                    test = df[df['shop'] == shop]
                                    if test.empty:
                                        with open('ranking.csv', 'a', newline="", encoding="utf-8") as csv_file:
                                            fieldnames = ['shop', 'shopCount']
                                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                            # writer.writeheader()

                                            shop = string.capwords(shop)

                                            writer.writerow({'shop': shop, 'shopCount': addCount})

                                    else:

                                        df = pd.read_csv('ranking.csv')
                                        test = df[df['shop'] == shop]
                                        total = test['shopCount'] + addCount

                                        df.at[df['shop'] == shop, 'shopCount'] = total
                                        df.to_csv("ranking.csv", index=False)
                                        print(df)

                                        count = 0

                                    return

                    secondMessage = (f"""
                    ===============================================
                    はじめまして。{name} さん。お好きなレストランを教えて頂けませんか？ 
                    ===============================================
                    """)

                    print(colored(secondMessage, 'green'))

                    count += 1

                if count == 1:
                    shop = input()
                    shop = string.capwords(shop)

                    lastMessage = (f"""
                    ===============================================
                    {name} さん。有難うございました。
                    良い一日を。さようなら。
                    ===============================================
                    """)

                    print(colored(lastMessage, 'green'))

                    shopCount = 1

                    with open('ranking.csv', 'w', newline="", encoding="utf-8") as csv_file:
                        fieldnames = ['shop', 'shopCount']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow({'shop': shop, 'shopCount': shopCount})
                    count = 0

                break
