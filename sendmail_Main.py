import urllib
import smtplib
import xlrd


space = '\n'
textfile = open('message_file.txt','r')
global mess_data
mess_data = textfile.read()
textfile.close()

def readfromexcel(excelBookName, message_data):
    wb = xlrd.open_workbook(excelBookName)
    #print(wb.sheet_names())
    sh1 = wb.sheet_by_index(0)
    r1 = sh1.nrows
    #print(sheet.ncols)

    for i in range(r1):
        cus_name = sh1.cell_value(i,1)
        cus_emailID = sh1.cell_value(i,2)
        if '@gmail.com' in cus_emailID:
            print(cus_name)
            print(cus_emailID)
            msg_data = 'Hi ' + cus_name + space + message_data
            sendemail('S4silver Team',cus_emailID,
                      '',mail_subject,
                      msg_data,
                      'hari.navoinfotech@gmail.com',
                      'rejeesh123','smtp.gmail.com:587')


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()


mail_subject = 'testing'
readfromexcel('consumer_mailID.xls', mess_data)
