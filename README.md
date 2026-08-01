# Python-data-analysis

## 房價與結婚意願之相關分析

本專案探討「**買房壓力是否影響台灣年輕世代的結婚意願**」。透過自行設計的問卷收集受訪者對婚姻、購屋與經濟壓力的態度，並結合政府公開統計資料（結婚率、出生率、房價指數、歷年所得），以資料視覺化、關聯規則探勘（Apriori）與分群分析（K-means）呈現結果，最後以 Django 架設網站，把所有圖表與分析結論整合成可互動的網頁。

---

## 目錄

- [研究主題與問題](#研究主題與問題)
- [資料來源](#資料來源)
- [網站功能](#網站功能)
- [分析方法](#分析方法)
- [專案結構](#專案結構)
- [環境架設](#環境架設)
- [執行方式](#執行方式)
- [資料匯入與重新產生分析結果](#資料匯入與重新產生分析結果)
- [開發注意事項](#開發注意事項)

---

## 研究主題與問題

台灣近年結婚率與出生率持續下降，同時房價指數逐年攀升。本專案想回答的核心問題是：

1. 房價與購屋壓力，對結婚意願的影響程度有多大？
2. 除了經濟因素，還有哪些非經濟因素（自由、信任、家庭磨合、對婚姻失敗的恐懼等）在影響結婚意願？
3. 不同年齡、學歷、薪資水平的族群，在結婚意願上是否呈現可辨識的族群差異？

## 資料來源

### 一、自行收集的問卷資料

- 樣本數：**126 筆**有效回覆
- 題目數：29 題（另含時間戳記與開放式意見欄）
- 原始檔：`analysis/home/data/collect.xlsx`
- 儲存方式：匯入 SQLite 資料庫，對應 `home.models.MarriageSurvey` 模型

問卷題目分為五大構面：

| 構面 | 內容範例 |
|---|---|
| 一般資訊 | 生理性別、最高學歷、年齡、月薪資水平、是否已婚 |
| 買房觀念 | 買房是否為影響結婚的重要因素、買房影響結婚意願的程度、結婚是否一定得買房、對政府配套措施的評價 |
| 可能使擁有結婚意願的因素 | 想與心愛的人共組家庭、想要小孩、希望伴侶關係被法律認同、傳統觀念、想要伴侶一同承擔責任 |
| 可能影響結婚意願的經濟因素 | 不想犧牲現有生活水平、無法負擔高額房價、無法負擔結婚開銷、想先穩定事業、無法負擔子女教養費用 |
| 可能影響結婚意願的非經濟因素 | 只需情感需求不想綁定法律義務、害怕與對方家庭磨合、不確定對方是否值得信任、不想養小孩、婚後失去自由、沒有對象、害怕婚姻失敗 |

除「一般資訊」為類別型答案外，其餘題目皆為 1～5 分的李克特量表（Likert scale）。

### 二、政府公開統計資料

存放於 `analysis/home/data/`，同時在 `Visualization/` 下保留各自的原始檔與繪圖腳本：

| 檔案 | 內容 |
|---|---|
| `birthrate1.xlsx` | 歷年出生率 |
| `housepriceindex1.xlsx` | 歷年房價指數 |
| `age1.xlsx` | 各年齡層結婚率 |
| `educationlevel1.xlsx` | 各教育程度結婚率（國小、國中、高中、專科、大學） |
| `maritalstatus1.xlsx` | 婚姻狀況分布（未婚、離婚、喪偶） |
| `number_of_marriages1.xlsx` | 歷年結婚對數（總計／男／女） |
| `income1.xlsx` | 歷年所得相關指標（GDP、GNI、國民所得、經濟成長率、平均匯率、中期人口） |

## 網站功能

網站共三個頁面，路由定義於 `analysis/home/urls.py`：

### 1. Data Visualization（`/`）

呈現政府公開統計資料的趨勢圖，用來建立「房價上升、結婚率下降」的背景脈絡。包含：

- **出生率**與**房價指數**歷年趨勢
- **結婚率**：依年齡層、依教育程度（含圓餅圖）、依婚姻狀況（未婚／離婚／喪偶）
- **結婚對數**：總計、男性、女性與圓餅圖
- **歷年所得**：GDP、平均每人 GDP、GNI、平均每人 GNI、國民所得、平均每人所得、經濟成長率、平均匯率、中期人口

全站共 32 張圖表，皆由 matplotlib 於後端繪製，經 `fig_to_base64()` 轉為 base64 PNG 後直接嵌入 HTML，不依賴任何前端繪圖函式庫。

### 2. Data Analysis（`/analysis`）

- **Questionnaire Design**：完整問卷題目一覽表
- **Questionnaire Data**：可依屬性篩選的問卷資料瀏覽器

使用者從下拉選單挑選條件（性別、學歷、年齡、收入、婚姻狀況、各題答案等），前端以 AJAX 送出 `selected_option` 參數，後端 `filiterdata()` 動態查詢資料庫，回傳該子群體的筆數、佔全體比例，以及重新繪製的長條圖（`create_bar_chart()`），以 `JsonResponse` 回應。

### 3. Conclusion（`/apriori`）

呈現 Apriori 關聯規則探勘的結果。規則依前述五大構面分組，每條規則顯示：

- **Attributes**：規則涉及的屬性數
- **Rule**：關聯規則本體，例如 `1-afford_house_price → 0～19999-salary`
- **Support**（支持度）、**Confidence**（信賴度）、**Lift**（提升度）

資料來源為預先計算好的 `analysis/outputtest.json`，頁面只負責讀取與呈現，不即時運算。

## 分析方法

### 關聯規則探勘（Apriori）

使用 `apyori` 套件。前處理時把每個欄位的值轉成「`答案-欄位名`」形式的項目（例如 `1-afford_house_price`），讓每位受訪者成為一筆交易紀錄，再探勘題目答案之間的共現關係，用以找出「哪些條件常常一起出現」——例如低薪資水平與「無法獨自負擔房價」的高度關聯。

相關腳本：

- `analysis/apriori_alloftest.py`：從資料庫讀取資料執行 Apriori，輸出 `apriori_results.txt` 與 `output.json`
- `analysis/apriori_alloftest_changeoutput.py`：同上，但改為輸出網站使用的 JSON 結構——`outputtest.json` 與 `apriori_resultstest.txt`
- `DataAnalysis/`：早期以 Excel 為輸入的實驗版本與各階段輸出

### 分群分析（K-means）

使用 `scikit-learn` 的 `KMeans`。以「年齡」「月薪資」「買房影響結婚意願的程度」三個特徵做分群（`n_clusters=3`），並繪製相關係數熱力圖觀察三者關聯。年齡與薪資為區間型答案，先以區間中位數映射為數值後再分群。

相關腳本：

- `analysis/home/views.py` 的 `kmeansAgeIntention()`：網站使用的版本
- `analysis/trykmeans.py`、`kmeans/`：獨立實驗腳本（含標準化、PCA 降維、3D 散布圖等不同嘗試）

### 描述性統計與視覺化

`Visualization/` 下依主題分資料夾，每個資料夾包含該主題的 Excel 原始檔與獨立繪圖腳本，可單獨執行檢視圖表；網站版本則整合進 `views.py`。

## 專案結構

```
Python-data-analysis/
├── analysis/                   # Django 專案
│   ├── manage.py
│   ├── db.sqlite3              # SQLite 資料庫（含問卷資料）
│   ├── outputtest.json         # Apriori 結果，供 /apriori 頁面讀取
│   ├── importcsv.py            # 將 collect.xlsx 匯入資料庫
│   ├── trykmeans.py            # K-means 實驗腳本
│   ├── apriori_alloftest.py            # Apriori（文字輸出）
│   ├── apriori_alloftest_changeoutput.py  # Apriori（JSON 輸出）
│   ├── analysis/               # Django 設定（settings/urls/wsgi/asgi）
│   └── home/                   # 主要 app
│       ├── models.py           # MarriageSurvey 模型
│       ├── views.py            # 所有頁面與圖表產生邏輯
│       ├── urls.py             # 路由
│       ├── data/               # 問卷與政府統計原始資料
│       ├── migrations/
│       ├── templates/home/     # home / analysis / apriori / header / footer
│       └── commands/
├── DataAnalysis/               # Apriori 早期實驗版本與輸出
├── Visualization/              # 各主題獨立繪圖腳本與資料
│   ├── Birth Rate 出生率/
│   ├── House Price Index 房價指數/
│   ├── Income over the years 歷年所得/
│   └── Marriage rate 結婚率/
├── kmeans/                     # K-means 早期實驗版本
├── requirements.txt
└── README.md
```

## 環境架設

### 主要套件

| 用途 | 套件 |
|---|---|
| 網站框架 | Django |
| 資料處理 | pandas、numpy、openpyxl |
| 視覺化 | matplotlib、seaborn |
| 關聯規則 | apyori |
| 機器學習 | scikit-learn |
| 表格輸出 | prettytable |

> `mpld3` 列於 `requirements.txt` 且在 `views.py` 中 import，但目前程式並未實際使用（圖表一律走 base64 靜態圖）。

### 安裝步驟

建議使用虛擬環境（venv），避免套件版本互相干擾：

```powershell
# 1. 建立虛擬環境（於專案根目錄）
python -m venv venv

# 2. 啟動虛擬環境
.\venv\Scripts\Activate.ps1

# 3. 安裝套件
pip install -r requirements.txt
```

> 若 PowerShell 因執行原則擋下啟動指令，先執行 `Set-ExecutionPolicy -Scope Process RemoteSigned` 再重試。
> macOS / Linux 的啟動指令為 `source venv/bin/activate`。

### Before you runserver please enter this code in your terminal:

pip install -r requirements.txt

### To make sure you can run django :

Please check your folder is on `\Python-data-analysis\analysis`
You can use `cd foldername` to move your folder position.
After you check it, please run:

python manage.py runserver

Then you can see the website.

## 執行方式

```powershell
# 啟動虛擬環境（若尚未啟動）
.\venv\Scripts\Activate.ps1

# 切換到 Django 專案目錄
cd analysis

# 啟動開發伺服器
python manage.py runserver
```

伺服器啟動後，於瀏覽器開啟 <http://127.0.0.1:8000/> 即可瀏覽網站。

首頁會即時繪製全部圖表，第一次載入需要數秒鐘屬正常現象。

## 資料匯入與重新產生分析結果

資料庫（`db.sqlite3`）已包含問卷資料，一般情況下不需重跑。若更新了 `collect.xlsx` 或需要重新產生分析結果：

```powershell
cd analysis

# 1. 建立資料表（初次設定或模型變更後）
python manage.py migrate

# 2. 將 collect.xlsx 匯入資料庫
#    注意：此腳本會先清空 MarriageSurvey 全部資料再重新匯入
python importcsv.py

# 3. 重新計算 Apriori 並更新 outputtest.json
python apriori_alloftest_changeoutput.py
```

## 開發注意事項

### Before update your code, update the project from github first:

Use vscode open the terminal, and make sure the termial path is on project path,
then type `git pull` on the terminal. p.s. don't type "" on terminal.

### 其他

- **中文字型**：圖表使用 `Microsoft JhengHei` 顯示中文。若在非 Windows 環境執行，需修改 `views.py` 中的 `rcParams['font.sans-serif']` 為系統已安裝的中文字型，否則中文會顯示為方框。
- **檔案路徑**：所有資料檔路徑皆以 `os.path.join(script_dir, ...)` 相對於程式檔案位置計算，請勿改寫為絕對路徑，否則換一台電腦就會失效。
- **matplotlib 記憶體**：`views.py` 中建立的 figure 未呼叫 `plt.close()` 釋放，長時間執行伺服器時記憶體會持續累積，重啟伺服器即可回復。

---

If there's any problem please tell me - Dai Yun Wu
