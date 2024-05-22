import wave
import struct
from scipy import fromstring,int16
import numpy as np
import os
import math
import speech_recognition as sr
import pandas as pd
import tkinter.filedialog
import urllib.request
import openpyxl

#filenameに読み込むファイル、timeにカットする間隔
def cut_wav(filename,time):  
    # timeの単位は[sec]

    # ファイルを読み出し
    wavf = filename
    wr = wave.open(wavf, 'r')

    # waveファイルが持つ性質を取得
    ch = wr.getnchannels()
    width = wr.getsampwidth()
    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr 
    integer = math.floor(total_time*100) # 小数点以下切り捨て
    t = int(time*100)  # 秒数[sec]
    frames = int(ch * fr * t /100)
    num_cut = int(integer//t)
    # waveの実データを取得し、数値化
    data = wr.readframes(wr.getnframes())
    wr.close()
    X = np.frombuffer(data, dtype=int16)

    for i in range(num_cut + 1):
        # 出力データを生成
        outf = out_dir + '/' + str(i) + '.wav' 
        # 音声をカットした部分は少し巻き戻す
        if i > 0:
            start_cut = int(i*frames) - int(180000)
        else:
            start_cut = int(i*frames)

        end_cut = int(i*frames + frames)
        # print(start_cut)
        # print(end_cut)
        Y = X[start_cut:end_cut]
        outd = struct.pack("h" * len(Y), *Y)

        # 書き出し
        ww = wave.open(outf, 'w')
        ww.setnchannels(ch)
        ww.setsampwidth(width)
        ww.setframerate(fr)
        ww.writeframes(outd)
        ww.close()

    str_out = ""
    list1 = [wavf,"",""]
    df_x = pd.DataFrame([list1])
    df_x.columns = ['No', '音声ファイル', '変換結果']

    for ii in range(num_cut + 1):
        outf = out_dir + '/' + str(ii) + '.wav' 
        str_out = wav_to_text(outf)
        df_x.loc[ii] = [ii,str(ii) + '.wav',str_out]

    # excelへ書き出し
    with pd.ExcelWriter(out_file) as writer:
        df_x.to_excel(writer, sheet_name='結果', index=False)

def wav_to_text(wavfile):
    r = sr.Recognizer()

    with sr.AudioFile(wavfile) as source:
        audio = r.record(source)

    proxy_handler = urllib.request.ProxyHandler({'http': 'http://cproxy.okinawa-ct.ac.jp:8080', 'https': 'http://cproxy.okinawa-ct.ac.jp:8080'})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    wav_to_text = r.recognize_google(audio, language='ja-JP')

    print(wav_to_text)

    return wav_to_text

# 一応既に同じ名前のディレクトリがないか確認。
out_dir = "output"
file = os.path.exists(out_dir)
# print(file)

if file == False:
    #保存先のディレクトリの作成
    os.mkdir(out_dir)

fTyp = [("","*.wav")]
iDir = os.path.abspath(os.path.dirname(__file__))
f_name = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

cut_time = 60
out_file = "output/out.xlsx"
cut_wav(f_name,float(cut_time))

'''
Reference
- [Pythonで音声ファイルを文字起こしする](https://qiita.com/daifuku10/items/62cc3d0075a6cb9389b4)
'''