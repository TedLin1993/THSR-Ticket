# 高鐵訂票小幫手

修改 https://github.com/BreezeWhite/THSR-Ticket 的 repo，並加入 https://github.com/maxmilian/thsrc_captcha 的 model，使流程更加快速。

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

* Modified [my_info.py](https://github.com/mrwenwei/THSR-Ticket/blob/f4b525ed192898691c650bdd3762bd15ffa77744/thsr_ticket/configs/web/my_info.py#L2) to your own information.

* 執行（不加參數為可彈性選擇之版本）
  ```
  python thsr_ticket/main.py
  ```
  加參數為一鍵訂票之版本(起站/訖站/車次號碼/auto)
  此功能主要目的為搶早鳥票，因此預設時間會是28天後（不加 auto 可選擇時間）
  先查清楚車次後可節省許多時間（搶票第一名><）。
  EX.
  ```
  python thsr_ticket/main.py Taipei Zuouing 803 auto
  ```

## TODO
- [ ] 使用會員訂票 
