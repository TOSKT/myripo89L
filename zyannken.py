"""
MIT License

Copyright (c) 2018 TOSKT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import tkinter as tk
import random

root = tk.Tk()
count_w = 0
count_lo = 0
count_dlo = 0

def NPC_turn1():
        global count_w,count_lo,count_dlo
        n = tk.Label(text='',fg='white',bg='black')
        p = tk.Label(text='',fg='white',bg='black')
        re = tk.Label(text='',fg='white',bg='black')   
        p['text'] = 'あなたはグー'
        p.place(x=100,y=110)
        list = ['グー','チョキ','パー'] 
        if random.choice(list) == 'パー':
                n['text']='わたしはパーです'
                n.place(x=100,y=130)
                re['text']='あなたの負けです'
                re.place(x=150,y=170)
                count_lo += 1
                c_lo = tk.Label(text='あなたの負け数カウント　　　'+str(count_lo),fg='white',bg='black')
                c_lo.place(x=100,y=300)

        elif  random.choice(list) == 'チョキ':
                n['text']='わたしはチョキです'
                n.place(x=100,y=130)
                re['text']='あなたの勝ちです'
                re.place(x=150,y=170)
                count_w += 1
                c_win = tk.Label(text='あなたの勝ち数カウント　　　'+str(count_w),fg='white',bg='black')
                c_win.place(x=100,y=300)

        else:
                n['text']='わたしはグーです'
                n.place(x=100,y=130)
                re['text']='引き分けです'
                re.place(x=150,y=170)
                count_dlo += 1
                c_dlo = tk.Label(text='あなたの引き分け数カウント　　　'+str(count_dlo),fg='white',bg='black')
                c_dlo.place(x=100,y=370)

def NPC_turn2():
        global count_w,count_lo,count_dlo
        n = tk.Label(text='',fg='white',bg='black')
        p = tk.Label(text='',fg='white',bg='black')
        re = tk.Label(text='',fg='white',bg='black')
        p['text'] = 'あなたはチョキ'
        p.place(x=100,y=110)
        list = ['グー','チョキ','パー'] 
        if random.choice(list) == 'パー':
                n['text']='わたしはパーです'
                n.place(x=100,y=130)
                re['text']='あなたの勝ちです'
                re.place(x=150,y=170)
                count_w += 1
                c_win = tk.Label(text='あなたの勝ち数カウント　　　'+str(count_w),fg='white',bg='black')
                c_win.place(x=100,y=300)

        elif  random.choice(list) == 'チョキ':
                n['text']='わたしはチョキです'
                n.place(x=100,y=130)
                re['text']='引き分けです'
                re.place(x=150,y=170)
                count_dlo += 1
                c_dlo = tk.Label(text='あなたの引き分け数カウント　　　'+str(count_dlo),fg='white',bg='black')
                c_dlo.place(x=100,y=370)

        else:
                n['text']='わたしはグーです'
                n.place(x=100,y=130)
                re['text']='あなたの負けです'
                re.place(x=150,y=170)    
                count_lo += 1
                c_lo = tk.Label(text='あなたの負け数カウント　　　'+str(count_lo),fg='white',bg='black')
                c_lo.place(x=100,y=330)
                
def NPC_turn3():
        global count_w,count_lo,count_dlo 
        n = tk.Label(text='',fg='white',bg='black')
        p = tk.Label(text='',fg='white',bg='black')
        re = tk.Label(text='',fg='white',bg='black')
        p['text'] = 'あなたはパー'
        p.place(x=100,y=110)
        list = ['グー','チョキ','パー'] 
        if random.choice(list) == 'パー':
                n['text']='わたしはパーです'
                n.place(x=100,y=130)
                re['text']='引き分けです'
                re.place(x=150,y=170)
                count_dlo += 1
                c_dlo = tk.Label(text='あなたの引き分け数カウント　　　'+str(count_dlo),fg='white',bg='black')
                c_dlo.place(x=100,y=370)
                

        elif  random.choice(list) == 'チョキ':
                n['text']='わたしはチョキです'
                n.place(x=100,y=130)
                re['text']='あなたの負けです'
                re.place(x=150,y=170)
                count_lo += 1
                c_lo = tk.Label(text='あなたの負け数カウント　　　'+str(count_lo),fg='white',bg='black')
                c_lo.place(x=100,y=330)

        else:
                n['text']='わたしはグーです'
                n.place(x=100,y=130)
                re['text']='あなたの勝ちです'
                re.place(x=150,y=170)
                count_w += 1
                c_win = tk.Label(text='あなたの勝ち数カウント　　　'+str(count_w),fg='white',bg='black')
                c_win.place(x=100,y=300)                 

root.geometry('880x560')
root.title('じゃんけんゲーム')
font = 'メイリオ'

canvas = tk.Canvas(bg='black',width=880,height=560)
canvas.place(x=0,y=0)

playgame = tk.Label(text = 'ゲーム開始',fg='white',bg='black')
playgame.place(x=100,y=40)
what = tk.Label(text='何を出しますか？',fg='white',bg='black')
what.place(x=100,y=60)

button = tk.Button(text='グー',command = NPC_turn1)
button.place(x=100,y=80)

button = tk.Button(text='チョキ',command = NPC_turn2)
button.place(x=160,y=80)

button = tk.Button(text='パー',command = NPC_turn3)
button.place(x=220,y=80)

root.mainloop()