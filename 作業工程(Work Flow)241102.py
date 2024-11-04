import tkinter as tk
from tkinter import ttk
import subprocess
import os
import webbrowser

# File paths and URLs
file_paths = {
    #勉強
    "JASS6 PDF": "C:/path/to/your/file.pdf",
    "Techme_JASS6 Day1": "https://teachme.jp/142142/manuals/23536448",
    "Techme_JASS6 Day2": "https://teachme.jp/142142/manuals/23635777",
    "Techme_JASS6 Day3": "https://teachme.jp/142142/manuals/23720089",
    "Techme_JASS6 Day4": "https://teachme.jp/142142/manuals/23756591",
    "Techme_JASS6 Day5": "https://teachme.jp/142142/manuals/24000708",
    "Techme_JASS6 Day6": "https://teachme.jp/142142/manuals/24060904",
    "Techme_JASS6 Day7": "https://teachme.jp/142142/manuals/24079504",
    "Techme_JASS6 Day8": "https://teachme.jp/142142/manuals/24100953",
    "Techme_JASS6 Day9": "https://teachme.jp/142142/manuals/24112773",
    "Techme_JASS6 Day10": "https://teachme.jp/142142/manuals/24121402",
    "Techme_JASS6 Day11": "https://teachme.jp/142142/manuals/24162786",
    "Techme_JASS6 Day12": "https://teachme.jp/142142/manuals/24180751",
    "Techme_JASS6 Day13": "https://teachme.jp/142142/manuals/24188109",
    "Techme_JASS6 Day14": "https://teachme.jp/142142/manuals/24470138",

    "Techme_構造図と一般図の見方": "https://teachme.jp/142142/manuals/28323975",

    #資料
    "Techme_工程表": "https://teachme.jp/142142/manuals/29517472",
    "PDF_工程表": r"\\LS220DC16\share\24-1022_日高市下高萩新田倉庫計画新築工事\04...工程表\241016_日高物流鉄骨製作工程表.pdf",

    "Techme_キックオフ資料": "https://teachme.jp/142142/manuals/29517472",
    "Excel_キックオフ資料": r"\\LS220DC16\share\24-1022_日高市下高萩新田倉庫計画新築工事\04...工程表\241022_日高キックオフ資料.xlsx",

    "Techme_質疑書":  "https://" ,
    "Excel_製作要領書": "",

    "Techme_製作要領書": "https://" ,
    "Excel_製作要領書": "",

    "Techme_頂きたい資料": "https://" ,
    "Excel_頂きたい資料": "",

    "Techme_製品図進捗状況": "https://teachme.jp/142142/manuals/23685210",
    "Excel_製品図進捗状況": "",

    "Techme_現寸発注予定表": "https://teachme.jp/142142/manuals/23734728",
    "Excel_現寸発注予定表": "",
    
     #設計図・見積書
    "Techme_意匠図": "https://teachme.jp",
    "PDF_意匠図": r"\\LS220DC16\share\24-1022_日高市下高萩新田倉庫計画新築工事\01...設計図\01...意匠図\意匠図一式0903.pdf",

    "Techme_構造図": "https://teachme.jp",
    "PDF_構造図": r"\\LS220DC16\share\24-1022_日高市下高萩新田倉庫計画新築工事\01...設計図\02...構造図\構造図一式0903.pdf",

    "Techme_見積書": "https://teachme.jp",
    "Excel_見積書": r"\\LS220DC16\share\24-1022_日高市下高萩新田倉庫計画新築工事\03...見積り\K273 (仮称)日高市下高萩新田物流倉庫新築工事.xls",


    "Techme_Trimble Connect 2024": "https://teachme.jp/142142/manuals/29595479",

    #モデル
    "Excel_Model Sharing": r"X:\Other_list\Model_sharing_member_list.xlsx",
    
    
}

# Variable to keep track of the active button
active_button = None

# Function to highlight button on click
def highlight_button(button):
    global active_button
    if active_button:
        active_button.config(bg="SystemButtonFace")  # Reset previous button color
    button.config(bg="skyblue")  # Highlight clicked button
    active_button = button

# Function to open files or URLs
def open_file(file_key, button=None):
    if button:
        highlight_button(button)
    file_path = file_paths.get(file_key)
    if file_path:
        try:
            if file_path.startswith("http"):
                # URLをブラウザで開く
                webbrowser.open(file_path)
            elif os.path.exists(file_path):
                # ローカルファイルを開く（Windowsの場合）
                os.startfile(file_path)
            else:
                # ファイルが見つからない場合のエラーメッセージ（エンコードエラー回避のため修正）
                print(f"指定されたファイルが見つかりません: {file_path.encode('utf-8', errors='replace').decode('utf-8')}")
        except UnicodeEncodeError:
            # エンコードエラーが発生した場合のエラーメッセージ
            print(f"エンコードエラーが発生しました: {file_path.encode('utf-8', errors='replace').decode('utf-8')}")
        except Exception as e:
            # 他の例外をキャッチして表示
            print(f"エラーが発生しました: {str(e)}")


# Function to toggle checkbox
def toggle_checkbox(label):
    label.config(text="✓" if label.cget("text") == "□" else "□")

# Create main window
root = tk.Tk()
root.title("作業工程(Work Flow)")
root.geometry("800x800")

# Notebook (Tab Menu) setup
notebook = ttk.Notebook(root)
tabs = ["勉強", "作業工程", "資料", "設計図・見積書", "モデル", "一般図", "単品図", "製品図", "発注"]
frames = {tab: ttk.Frame(notebook) for tab in tabs}
for tab, frame in frames.items():
    notebook.add(frame, text=tab)

notebook.pack(padx=10, pady=10, fill='x')

# Function to create a row of buttons with an optional label and checkbox
def create_column_buttons(parent, button_data, row, label_text=None, checkbox_positions=None):
    if label_text:
        label = tk.Label(parent, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky="e")

    for col, (text, file_key) in enumerate(button_data):
        if checkbox_positions and checkbox_positions[col]:
            # Checkbox-style label placed where specified
            checkbox_label = tk.Label(parent, text="□", font=("Arial", 12))
            checkbox_label.grid(row=row, column=col*2 + 1, padx=5, pady=5, sticky="w")
            checkbox_label.bind("<Button-1>", lambda e, lbl=checkbox_label: toggle_checkbox(lbl))

        # Button
        button = tk.Button(parent, text=text)
        button.config(command=lambda b=button, k=file_key: open_file(k, b))
        button.grid(row=row, column=col*2 + 2, padx=5, pady=5, sticky="w")

# Populate "作業工程" tab with buttons
作業工程_frame = frames["勉強"]

#勉強Frame1_JASS6
previous_comment_frame = ttk.LabelFrame(作業工程_frame, text="JASS6")
previous_comment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Define button data for each row as (button_text, file_key)
create_column_buttons(
    previous_comment_frame,
    [
        ("JASS6", "Techme_JASS6 PDF"),  
    ],
    row=0
)
create_column_buttons(
    previous_comment_frame,
    [
        ("Day01", "Techme_JASS6 Day1"),
        ("Day02", "Techme_JASS6 Day2"),
        ("Day03", "Techme_JASS6 Day3"),
        ("Day04", "Techme_JASS6 Day4"),
        ("Day05", "Techme_JASS6 Day5"),
         
    ],
    row=1
)
create_column_buttons(
    previous_comment_frame,
    [  
        ("Day06", "Techme_JASS6 Day6"),
        ("Day07", "Techme_JASS6 Day7"),
        ("Day08", "Techme_JASS6 Day8"),
        ("Day09", "Techme_JASS6 Day9"),
        ("Day10", "Techme_JASS6 Day10")
    ],
    row=2
)    
create_column_buttons(
    previous_comment_frame,
    [  
        ("Day11", "Techme_JASS6 Day11"),
        ("Day12", "Techme_JASS6 Day12"),
        ("Day13", "Techme_JASS6 Day13"),
        ("Day14", "Techme_JASS6 Day14")  
    ],
    row=3
)
create_column_buttons(
    previous_comment_frame,
    [  
        ("Quiz", "Techme_JASS6 Quiz"),
        ("Test", "Techme_JASS6 Test")
 
    ],
    row=4
) 

#勉強Frame2_見方
previous_comment_frame = ttk.LabelFrame(作業工程_frame, text="見方")
previous_comment_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
create_column_buttons(
    previous_comment_frame,
    [("構造図と一般図の見方", "Techme_構造図と一般図の見方")],
    row=1
)

# Populate "資料" tab with buttons
作業工程_frame = frames["資料"]
資料_comment_frame = ttk.LabelFrame(作業工程_frame, text="資料")
資料_comment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Add multiple buttons to each row in "資料"
create_column_buttons(
    資料_comment_frame,
    [("工程表（スケジュール表）【がんすけ】", "Techme_工程表"), ("PDF", "PDF_工程表")
     ],
    row=0,label_text="①",checkbox_positions=[True, False]
)
create_column_buttons(
    資料_comment_frame,
    [("キックオフ資料", "Techme_キックオフ資料"), ("Excel", "Excel_キックオフ資料"),],
    row=1,label_text="②",checkbox_positions=[True, False]
)
create_column_buttons(
    資料_comment_frame,
    [("質疑書", "Techme_質疑書"), ("Excel", "Excel_質疑書"),],
    row=2,label_text="③",checkbox_positions=[True, False]
)
create_column_buttons(
    資料_comment_frame,
    [("製作要領書", "Techme_製作要領書"), ("Excel", "Excel_製作要領書"),],
    row=3,label_text="④",checkbox_positions=[True, False]
)
create_column_buttons(
    資料_comment_frame,
    [("頂きたい資料（進捗状況）", "Techme_頂きたい資料"), ("Excel", "Excel_頂きたい資料"),],
    row=4,label_text="⑤",checkbox_positions=[True, False]
)
create_column_buttons(
    資料_comment_frame,
    [("製品図（進捗状況）", "Techme_製品図進捗状況"), ("Excel", "Excel_製品図進捗状況"),],
    row=5,label_text="⑥",checkbox_positions=[True, False]
)
create_column_buttons(
    資料_comment_frame,
    [("現寸発注予定表(発注進捗状況）", "Techme_現寸発注予定表"), ("Excel", "Excel_現寸発注予定表"),],
    row=6,label_text="⑦",checkbox_positions=[True, False]
)

# Populate "設計図・見積書" tab with buttons
previous_frame = frames["設計図・見積書"]
previous_comment_frame = ttk.LabelFrame(previous_frame, text="設計図・見積書")
previous_comment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Add buttons to "設計図・見積書" tab
create_column_buttons(
    previous_comment_frame,
    [("意匠図", "Techme_意匠図"), ("PDF", "PDF_意匠図"), ],
    row=0
)
create_column_buttons(
    previous_comment_frame,
    [("構造図", "Techme_構造図"), ("PDF", "PDF_構造図"), ],
    row=1
)
create_column_buttons(
    previous_comment_frame,
    [("見積書", "Techme_見積書"), ("Excel", "Excel_見積書"), ],
    row=2
)
create_column_buttons(
    previous_comment_frame,
    [("Trimble Connect 2024", "Techme_Trimble Connect 2024"), ],
    row=3
)

# Populate "モデル" tab with buttons
previous_frame = frames["モデル"]

#モデルFrame1_基本モデル
previous_comment_frame = ttk.LabelFrame(previous_frame, text="基本モデル")
previous_comment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Add buttons to "基本モデル" tab
create_column_buttons(
    previous_comment_frame,
    [("意新規モデル作成 ", "Techme_新規モデル作成"), ("PDF", "PDF_新規モデル作成"), ],
    row=0, label_text="①",checkbox_positions=[True, False]
)
create_column_buttons(
    previous_comment_frame,
    [("基準線登録   ", "Techme_基準線登録  "), ("PDF", "PDF_基準線登録"),("チェック", "基準線チェック") ],
    row=1, label_text="②",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("モデルシェアリング", "モデルシェアリング"), ("PDF", "PDF_モデルシェアリング"), ("Model Sharing登録者一覧を開く","Excel_Model Sharing")],
    row=2, label_text="③",checkbox_positions=[True, False, False]
)
create_column_buttons(
    previous_comment_frame,
    [("部材登録", "部材登録"), ("PDF", "PDF_部材登録"),("チェック", "部材登録")  ],
    row=3, label_text="④",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("継手登録", "継手登録"), ("PDF", "PDF_継手登録"),("チェック", "継手登録")  ],
    row=4, label_text="⑤",checkbox_positions=[True, False, True]
)

#モデルFrame2_継手部
previous_comment_frame = ttk.LabelFrame(previous_frame, text="継手部(Ctrl+F)")
previous_comment_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Add buttons to "継手部" tab
create_column_buttons(
    previous_comment_frame,
    [("ベース継手", "Techme_ベース継手"), ("PDF", "PDF_ベース継手"), ],
    row=0, label_text="①",checkbox_positions=[True, False]
)
create_column_buttons(
    previous_comment_frame,
    [("SPL継手", "Techme_SPL継手"), ("PDF", "PDF_SPL継手"), ],
    row=1, label_text="②",checkbox_positions=[True, False]
)
create_column_buttons(
    previous_comment_frame,
    [("現場継手", "Techme_現場継手"), ("PDF", "PDF_現場継手"), ],
    row=2, label_text="③",checkbox_positions=[True, False]
)
create_column_buttons(
    previous_comment_frame,
    [("現場継手", "Techme_現場継手"), ("PDF", "PDF_現場継手"), ],
    row=3, label_text="③",checkbox_positions=[True, False]
)

#モデルFrame3_モデリング
previous_comment_frame = ttk.LabelFrame(previous_frame, text="モデリング")
previous_comment_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Add buttons to "モデリングル" tab
create_column_buttons(
    previous_comment_frame,
    [("部材配置", "Techme_部材配置"), ("PDF", "PDF_部材配置"),("チェック", "チェック_部材配置"),("※間柱フロア情報入力 ", "PDF_間柱フロア情報入力") ],
    row=0, label_text="⑥" ,checkbox_positions=[True, False, True, True,]
)
create_column_buttons(
    previous_comment_frame,
    [("仕口作成 ", "Techme_仕口作成 "), ("PDF", "PDF_仕口作成"),("チェック", "チェック_仕口"), ],
    row=1, label_text="⑦" ,checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("ベースPL配置  ", "Techme_ベースPL配置  "), ("PDF", "PDF_ベースPL配置 "),("チェック", "チェック_ベースPL配置 "), ],
    row=2, label_text="⑧",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("継手作成  ", "Techme_継手作成  "), ("PDF", "PDF_継手作成 "),("チェック", "チェック_継手作成 "), ],
    row=3, label_text="⑨",checkbox_positions=[True, False, True]
)

# Populate "一般図" tab with buttons
previous_frame = frames["一般図"]

#一般図Frame1_基本モデル
previous_comment_frame = ttk.LabelFrame(previous_frame, text="継手図面")
previous_comment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Add buttons to "継手図面" tab
create_column_buttons(
    previous_comment_frame,
    [("大梁継手", "Techme_大梁継手"), ("PDF", "PDF_大梁継手"), ("チェック", "小梁継手チェック")],
    row=0, label_text="①",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("小梁継手", "Techme_小梁継手"), ("PDF", "PDF_小梁継手"),("チェック", "小梁継手チェック") ],
    row=1, label_text="②",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("間柱継手", "Techme_間柱継手"), ("PDF", "PDF_間柱"),("チェック", "間柱継手チェック") ],
    row=2, label_text="③",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("ブレース継手", "Techme_ブレース継手"), ("PDF", "PDF_ブレース"),("チェック", "ブレース継手チェック") ],
    row=3, label_text="④",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("柱継手", "Techme_柱継手"), ("PDF", "PDF_柱"),("チェック", "柱継手チェック") ],
    row=4, label_text="⑤",checkbox_positions=[True, False, True]
)

#一般図Frame2_図面
previous_comment_frame = ttk.LabelFrame(previous_frame, text="図面")
previous_comment_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Add buttons to "図面" tab
create_column_buttons(
    previous_comment_frame,
    [("アンカープラン", "Techme_アンカープラン"), ("PDF", "PDF_アンカープラン"), ("チェック", "アンカープランチェック")],
    row=0, label_text="⑥",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("伏図作成", "Techme_伏図作成"), ("PDF", "PDF_伏図作成"),("チェック", "伏図作成チェック") ],
    row=1, label_text="⑦",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("軸作成", "Techme_軸作成"), ("PDF", "PDF_軸作成"),("チェック", "軸作成チェック") ],
    row=2, label_text="⑧",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("詳細図作成", "Techme_詳細図作成"), ("PDF", "PDF_詳細図作成"),("チェック", "詳細図作成チェック") ],
    row=3, label_text="⑨",checkbox_positions=[True, False, True]
)

#一般図Frame3_詳細図
previous_comment_frame = ttk.LabelFrame(previous_frame, text="詳細図")
previous_comment_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Add buttons to "詳細図" tab
create_column_buttons(
    previous_comment_frame,
    [("溶接詳細図作成", "Techme_溶接詳細図作成"), ("PDF", "PDF_溶接詳細図作成"), ("チェック", "溶接詳細図作成")],
    row=0, label_text="⑩",checkbox_positions=[True, False, True]
)
create_column_buttons(
    previous_comment_frame,
    [("溶接基準図修正", "Techme_溶接基準図修正"), ("PDF", "PDF_溶接基準図修正"),("チェック", "溶接基準図修正チェック") ],
    row=1, label_text="⑪",checkbox_positions=[True, False, True]
)




# Main window loop
root.mainloop()