import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_email():
	mail_body="<I>shine shine up</I>"
	smtpserver = "smtp.163.com"
	user = "your_email_address"
	passwd = "your_email_password"	
	sender = user
	receiver = "target_email_address"
	subject = "自动定时发送报告%s" % (time.strftime("%Y%m%d"))

	msg = MIMEMultipart()

	msg_html = MIMEText(mail_body, 'html', 'utf-8')
	msg_html['Content-Disposition'] = 'attachment; filename="TestReport.html'
	msg.attach(msg_html)

	msg['From'] = sender
	msg['To'] = receiver
	msg['Subject'] = subject

	smtp = smtplib.SMTP()
	smtp.connect(smtpserver, '25')
	# smtp.set_debuglevel(1)
	smtp.login(user, passwd)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()

if __name__ == '__main__':
	print("=============AutoTest Start=============")
	# test_dir = r"test_case"
	# test_report_dir = r"report"

	send_email()

	print("=============AutoTest Over==============")