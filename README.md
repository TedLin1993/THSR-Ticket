# 高鐵訂票小幫手

修改 https://github.com/BreezeWhite/THSR-Ticket 的 repo，並加入 https://github.com/sml2h3/ddddocr 圖形辨識，使流程更加快速。

## Installation

* Clone the repo
  ```
  git clone https://github.com/mrwenwei/THSR-Ticket.git

  cd THSR-Ticket
  ```

* Install packages
  ```
  pip install -r requirements.txt
  ```

* 執行（不加參數為可彈性選擇之版本）
  ```
  python thsr_ticket/main.py \
    --id ********** \
    --phone ********** \
    --start_station Zuouing \
    --dest_station Taipei\
    --auto auto \
    --train_no xxx\
    --date yyyy-MM-dd
  ```
  加參數為一鍵訂票之版本
  此功能主要目的為搶早鳥票，因此預設時間會是28天後 (or 29, 30)
  不加 auto 可選擇時間
  先查清楚車次後可節省許多時間（搶票第一名><）65折票大多數會在車程最長的班次，其他班次的數量比較少比較難搶。
  點此連結查詢: [高鐵早鳥優惠](https://www.thsrc.com.tw/ArticleContent/7039d17d-1463-4c14-ad93-4d491dedcad5)

## TODO
- [ ] 使用會員訂票
