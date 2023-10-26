import pyautogui
import pyperclip
import keyboard
import tkinter as tk
import speech_recognition as sr

# 音声認識器のインスタンスを作成
r = sr.Recognizer()

###tkinter###
# ウィンドウを作成
root = tk.Tk()
root.title("V_typer")

# ラベルを作成してテキストを表示
label1 = tk.Label(root, text="・insertキーで録音開始")
label2 = tk.Label(root, text="・escキーで終了(#w#)v")
label3 = tk.Label(root, text="(ctrl+Vで再度コピペ可能)")
label1.pack()
label2.pack()
label3.pack()
# キャンバスを作成
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()
# 常に最前面へ ウィンドウを固定
root.attributes("-topmost", True)


# 円を描画する関数
def draw_circle():
    canvas.create_oval(10, 10, 90, 90, fill="red")

# 円を非表示にする関数
def hide_circle():
    canvas.delete("all")



# マイクから音声を取得
def voice_recog():
    with sr.Microphone() as source:
        print("話してください")
        audio = r.listen(source)

        try:
            # 音声をテキストに変換
            # text = r.recognize_google(audio, language="en-US")
            text = r.recognize_google(audio, language="ja-JP")
            return text
        except sr.UnknownValueError:
            return "?" #"音声が認識できませんでした。"
        except sr.RequestError as e:
            return "e:" + str(e)#"音声認識サービスでエラーが発生しました。\nエラーメッセージ: " + str(e)

# Insertキーが押されたときに呼び出されるハンドラを定義
def key_event_operator(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "insert":
            # print("Insertキーが押されました")

            draw_circle()
            voice_txt = voice_recog()
            hide_circle()
            print(voice_txt)

            # クリップボードに文字列をコピーします
            pyperclip.copy(voice_txt)

            # 現在のマウスの位置を取得
            x, y = pyautogui.position()
            # マウスを指定された座標に移動してクリックします
            pyautogui.click(x, y)
            # Ctrl+V キーボードショートカットを使用してペーストします
            pyautogui.hotkey("ctrl", "v")
        elif e.name == "esc":
            root.destroy()
            print("esc終了")

def main():

    print("Insertキーで音声入力を開始します！(escで終了)")

    # Insertキーの監視を開始
    keyboard.hook(key_event_operator)

    # Ctrl+C(cmd上で)で終了するまで待機(escでも終了可)
    try:
        root.mainloop()
    except KeyboardInterrupt: # ctrlC押した後ウインドウを選択したら消える
        print("ctrl+c")
    print("プログラムを終了します.")


if __name__ == "__main__":
    main()
