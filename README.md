建立資料庫, 連接資料庫, 管理資料庫


資料庫選擇:
  不同DB有不同的特性, 合適的應用情境。根據使用情境不同:DB儲存平台, 讀寫頻率, 用戶數量等需選擇不同的DB架構。
  
  DB依使用情境分為: 1. 商用DB: 有大量支援
                        ex: Oracle, DB2, SQL Server
                   2. 開源DB: 
                        
                        ex: MySQL, PostgreSQL, SQLite
                        
  各不同DB架構的特色:
  
     開源DB:
       
       1. SQLite: 輕量級DB(可能只有幾十KB), 用C寫成, 適合用於嵌入式系統
          優點: 處理速度極快, 容易在不同系統之間遷移
          缺點: 不善於處理multithread 和multiprocessing, 容易被單一程式線程卡住, 讀寫文件會出問題
                部分SQL語法不支援
                
       2. MySQL: 使用者廣大的RDBMA系統
          優點: 完全支持multithread和multiprocessing, 速度快。支持GROUP BY, ORDER BY等SQL語法
          缺點: 安全系統較複雜, 而非標準。
          應用場景: 安全性高, 需多用戶訪問, 分散式DB(如同時使用SQLite)
          
       3. PostgreSQL:
          優點:
          缺點: 不支援multiprocessing, 速度較MySQL慢。不完全支持24hr運行, 需定期執行VACUUM.權限系統較不完整。
          應用場景:需要遷移的DB環境, PostgreSQL易於遷移。
          
       

