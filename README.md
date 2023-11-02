# 🤬 NoAutoCode !!!
## 😊 Introduction
- VScode에서 **코드의 자동완성 기능**과 **함수설명 팝업** 설정을 키거나 끌 수 있는 프로그램입니다. 
- Python으로 작성되었으며 tkinter를 사용해 GUI를 구성했습니다.
## 💡 Usage
- 코딩테스트에서 VSCode를 이용할 때 자동완성 관련 설정을 꺼야하는 경우
- VSCode에서 외부 IDE 연습을 이유로 자동완성이 없는 환경을 구현하고 싶은 경우
## 📄 Code
- Python으로 작성되었습니다.
```
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
        "editor.parameterHints.enabled": False
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
```
