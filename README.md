# 關於Authentication

這是我自行開發的身分驗證程式，會應用在我往後所有的軟體

為照顧到所有使用者，所有軟體都會預設訪客帳號(guest/guest)

如果你需要，可以自行下載使用

## v1.0

此版本是採用線上驗證，需要先將檔案放至Google Drive並公開

之後程式會將以公開的資料爬下來並整理

加密法是用sha-256

## v2.0

相較上個版本，此版本新增了

1. HTTPS加密連線
2. sha-256 -> Bcrypt
