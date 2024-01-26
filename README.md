# Line-bot  

### 功能說明

* 檔案說明:  
  *  app.py，必要，主要執行檔，控管line機器人執行訊息及排程運行(次/870s)。
  *  config.txt，選擇，控制token及sercet等相關資訊。
  *  Procfile，必要，用於虛擬平台(Render)判定執行專案的文件。
  *  requirements.txt，必要，紀錄所需要的python套件版本。
  *  Module/flexModule.py，選擇，各式訊息版型透過呼叫檔案內方法實現各式訊息樣式。
  *  Module/messageModule.py，選擇，訊息回應，透過呼叫檔案內方法對應不同訊息樣式提供不同回應。
* 功能說明：
  *  提供交通資訊予使用者選看，依據不同線路查看各線路圖片。
* 操作說明：
  * 工具：Line Developer、Line Designer、Python編譯器(Pycharm、VScode...)、Render架站平台、GitHub
  * 初次建置：
  	1. Line Developer建立Bot並取得token及secret。
    2. 建立一個資料夾並新增app.py、Procfile、requirements.txt(該文件請在cmd中下pip freeze > requirement.txt)
    3. 透過Python編譯器將基本LineBot呼叫語法寫入app.py中，並把token及secret寫入其中。
    4. 將完成的資料夾內檔案commit及push至Github專案中。
    5. Render建立一個webservice，將token及secret設置進去，並連結至對應的Github專案中，完成建立後確認服務是否正常執行。
    6. 將Render建立完成的webservice所產生的URL，填入Line Developer中的WebHook，並將自動回覆訊息關掉。
  * 後續更新：
    1. Python編譯器編譯完成檔案，將檔案commit及push至Github專案中。
    2. Render確認是否正常deploy完成。
### 2024/01/26
```
* 08:30：  
	* 加入Readme.txt  
```
