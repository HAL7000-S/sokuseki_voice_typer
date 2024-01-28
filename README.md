# sokuseki_voice_typer

即席音声入力pythonファイルです。

・（おそらく使わないであろう）insertキーで録音開始

・静寂が訪れたら録音終了

・escキーでソフト終了

・ctrl+Vで再度コピペ可能

## 使ったもの
```
import pyautogui
import pyperclip
import keyboard
import tkinter as tk
import speech_recognition as sr
```
