常見的嵌入式web服務器(embedded web server)有哪些

Lighttpd
地址：http://www.lighttpd.net/
lighttpd 適合靜態資源類的服務，比如圖片、資源文件、靜態HTML等等的應用，性能應該比較好，同時也適合簡單的CGI應用的場合，lighttpd可以很方便的通過fastcgi支持php


Shttpd
地址：https://www.oschina.net/p/shttpd?hmsr=aladdin1e1
Shttpd，開源。它是另一個輕量級的web server，具有比thttpd更豐富的功能特性，支持CGI, SSL, cookie, MD5認證, 還能嵌入(embedded)到現有的軟體里。最有意思的是不需要配置文件！由於shttpd可以輕鬆嵌入其他程序里，因此shttpd是較為理想的web server開發原形，開發人員可以基於shttpd開發出自己的webserver，官方網站上稱shttpd如果使用uclibc/dielibc(libc的簡化子集)則開銷將非常非常低。


Thttpd
地址：https://acme.com/software/thttpd/
Thttpd還有一個較為引人注目的特點：基於URL的文件流量限制，這對於下載的流量控制而言是非常方便的。象Apache就必須使用插件實現，效率較thttpd低。Thttp是開源的。是用C語言編寫的，使用的很多。

Boa
地址：http://www.boa.org/
是一種非常小巧的Web伺服器，其可執行代碼只有大約60KB左右。作為一種單任務Web伺服器，Boa只能依次完成用戶的請求，而不會fork出新的進程來處理並發連接請求。但Boa支持CGI，能夠為CGI程序fork出一個進程來執行。Boa的設計目標是速度和安全。


Mini_httpd
地址：https://www.oschina.net/p/mini-httpd
Mini_httpd是一個小型的HTTP伺服器。開源，它的性能不強，但是它非常適合於中小訪問量的站點。Mini_httpd和thttpd都是ACME Labs 開發的軟體，功能沒有thttpd強。


Appweb
地址：https://www.embedthis.com/
appweb 是下一代嵌入式web伺服器，它天生是為嵌入式開發的，它的最初設計理念就是安全。Appweb是一個快速、低內存使用量、標準庫、方便的伺服器。與其它嵌入式web伺服器相比，appweb最大特點就是功能多和高度的安全保障。Appweb簡單、方便、開源。

