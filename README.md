# 高鐵訂票小幫手

### 警告: 本程式僅供學術研究使用，若使用此程式導致任何問題，本人概不負責

感謝 https://github.com/BreezeWhite/THSR-Ticket 的高鐵訂票原始碼，並感謝 https://github.com/mrwenwei/THSR-Ticket 的圖形辨識。
因高鐵近幾個月的改版，導致原本的程式已無法正常執行。
此版本因應高鐵網站的改版，修改爬蟲邏輯，並修改訂票程序使訂票更加便利。

## Version

- python 3.9以上版本

## Installation

* Clone the repo
  ```
  git clone https://github.com/TedLin1993/THSR-Ticket.git

  cd THSR-Ticket
  ```

* Install packages
  ```
  pip install -r requirements.txt
  ```

* 執行
  ```
  python thsr_ticket/main.py \
    --id ********** \
    --phone ********** \
    --start_station Zuouing \
    --dest_station Taipei \
    --train_no xxx \
    --date yyyy/MM/dd \
    --time 700P
  ```

## Arguments

此程式必須使用參數進行訂票

- id (required): 身分證字號

- phone (required): 手機號碼

- start_station (required): 出發站
  - 車站需輸入英文，列表如下:
    ```
    南港: Nangang
    台北: Taipei
    板橋: Banqiao
    桃園: Taoyuan
    新竹: Hsinchu
    苗栗: Miaoli
    台中: Taichung
    彰化: Changhua
    雲林: Yunlin
    嘉義: Chiayi
    台南: Tainan
    左營: Zuoying
    ```

- dest_station (required): 抵達站
  - 車站列表同 `start_station`

- date (required): 出發日期
  - format: `yyyy/MM/dd`

- train_no (option): 車次號碼
  - 若不使用此參數，則自動改為依時間選擇車次

- time (option): 出發時間
  - 若不使用此參數，則在執行程式時透過清單點選
  - 時間需透過以下列表擇一使用:
    ```
      "1201A", "1230A", "600A", "630A", "700A", "730A", "800A", "830A", "900A",
      "930A", "1000A", "1030A", "1100A", "1130A", "1200N", "1230P", "100P", "130P",
      "200P", "230P", "300P", "330P", "400P", "430P", "500P", "530P", "600P",
      "630P", "700P", "730P", "800P", "830P", "900P", "930P", "1000P", "1030P",
      "1100P", "1130P"
    ```
      其中"A"代表早上，"P"代表下午，因此"700P"代表下午7點
  - 程式會自動選擇最接近出發時間的班次

## TODO
- [ ] 使用會員訂票
