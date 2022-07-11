import smtplib
# Read Me 
# 구글 보안 권한을 설정하셔야 하므로 새로운 계정을 생성하셔서 사용하는걸 권장 드립니다.

# https://blogpack.tistory.com/1056 위 블로그를 참조하시면 개인 SMTP 서버 생성이 가능합니다.
my_email = 'TestEmail@example.com' # 본인의 이메일을 적으시면 됩니다.
my_password = 'TestPassword'
connection = smtplib.SMTP('smtp.gmail.com')

connection.starttls() # tls : Transport Layer Server 이메일 서버와의 연결을 안전하게 만드는 방식.
connection.login(user=my_email, password=my_password) 
connection.sendmail(from_addr=my_email, to_addrs="test", msg = 'Subject:HelloThere \n\n this part is Body') # from_addr : 발신 메일 >> to_addrs : 수신 메일
connection.close()
