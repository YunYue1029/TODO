# ToDo List

## 系統簡介

這是一個使用 **Django** 開發的 ToDo 待辦清單管理系統，具備：

- 任務輸入表單（含標題、截止日期與時間）
- 整合 **FullCalendar** 顯示任務截止日
- 自動顯示任務在對應日曆格，僅以「日期」為主

## 專案結構說明

```
todo_project/
│
├── manage.py                  # Django 管理工具
├── db.sqlite3                 # 預設 SQLite 資料庫
├── todo_project/              # 專案設定
│   ├── settings.py
│   └── urls.py
│
├── todolist/                  # ToDo App 主程式
│   ├── models.py              # 資料模型
│   ├── views.py               # 邏輯處理
│   ├── templates/todolist/
│   │   └── index.html         # 主畫面
```

## 安裝與啟動步驟

### 1. 建立虛擬環境與安裝套件

```bash
python -m venv venv
source venv/bin/activate
pip install django
```

### 2. 啟動伺服器

```bash
python manage.py runserver
```

開啟瀏覽器輸入：`http://127.0.0.1:8000/`

## 使用說明

### 新增任務

1. 輸入任務名稱
2. 選擇截止日期與時間（可輸入 4 位數自動補冒號）
3. 點擊「新增」

系統會：
- 將任務即時加入下方任務列表
- 將任務標註到右側日曆中（日曆以「日期」為主）

### 完成/刪除任務

- 點擊「切換」：標記為已完成（加上刪除線）
- 點擊「刪除」：移除任務（從列表與日曆中消失）

### 日曆顯示

- 所有有填寫截止日期的任務，會自動出現在對應日期的日曆格中
- 不顯示時間段（只顯示任務名稱）
