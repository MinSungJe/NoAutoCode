import json
import tkinter as tk
from tkinter import messagebox

# 파일 경로
file_path = 'C:/Users/User/AppData/Roaming/Code/User/settings.json'

def current_status():
    with open(file_path, 'r') as file:
        settings_data = json.load(file)
        if "editor.suggest.showConstants" in settings_data:
            status = settings_data["editor.suggest.showConstants"]
        else: status = True
        
    return status

# JSON 파일을 수정하는 함수
def modify_settings():
    global var, discLabel
    cmd = not var.get()  # 사용자 입력에 따라 설정을 끄거나 켭니다

    # 수정할 정보
    data = {
        "editor.suggest.showConstants": False,
        "editor.suggest.showConstructors": False,
        "editor.suggest.showCustomcolors": False,
        "editor.suggest.showDeprecated": False,
        "editor.suggest.showEnumMembers": False,
        "editor.suggest.showEnums": False,
        "editor.suggest.showEvents": False,
        "editor.suggest.showFields": False,
        "editor.suggest.showFiles": False,
        "editor.suggest.showFolders": False,
        "editor.suggest.showFunctions": False,
        "editor.suggest.showInterfaces": False,
        "editor.suggest.showIssues": False,
        "editor.suggest.showKeywords": False,
        "editor.suggest.showMethods": False,
        "editor.suggest.showModules": False,
        "editor.suggest.showOperators": False,
        "editor.suggest.showProperties": False,
        "editor.suggest.showReferences": False,
        "editor.suggest.showSnippets": False,
        "editor.suggest.showStructs": False,
        "editor.suggest.showTypeParameters": False,
        "editor.suggest.showUnits": False,
        "editor.suggest.showUsers": False,
        "editor.suggest.showValues": False,
        "editor.suggest.showVariables": False,
        "editor.suggest.showWords": False,
        "editor.suggest.showClasses": False,
        "editor.suggest.showColors": False,
        "editor.parameterHints.enabled": False,
        "editor.hover.enabled": False
    }
    try:
        with open(file_path, 'r') as file:
            settings_data = json.load(file)

        for k in data.keys():
            if cmd: del settings_data[k]
            else: settings_data[k] = False

        with open(file_path, 'w') as file:
            json.dump(settings_data, file, indent=4)

        result = "(ON) 자동완성, 함수설명 설정을 켰습니다." if cmd else "(OFF) 자동완성, 함수설명 설정을 껐습니다."
        messagebox.showinfo("결과", result)
    except Exception as e:
        messagebox.showerror("오류", f"파일 수정 중 오류 발생: {e}")

    var = tk.BooleanVar(value=current_status())
    discLabel.config(text=f"자동완성 설정 / 함수설명 팝업이 현재 ON 상태입니다." if current_status() else "자동완성 설정 / 함수설명 팝업이 현재 OFF 상태입니다.")


# GUI 생성
root = tk.Tk()
root.title("by. MinSungJe")

var = tk.BooleanVar(value=current_status())

titleLabel = tk.Label(root, text="Visual Studio Code 설정")
discLabel = tk.Label(root, text=f"자동완성 설정 / 함수설명 팝업이 현재 ON 상태입니다." if current_status() else "자동완성 설정 / 함수설명 팝업이 현재 OFF 상태입니다.")

radio_off = tk.Radiobutton(root, text="끈다.", variable=var, value=0)
radio_on = tk.Radiobutton(root, text="킨다.", variable=var, value=1)

modify_button = tk.Button(root, text="설정 변경", command=modify_settings)

titleLabel.pack()
discLabel.pack()
modify_button.pack()

root.mainloop()