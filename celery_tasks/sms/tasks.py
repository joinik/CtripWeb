from celery_tasks.main import app
from utils.sms.SendMessage import Sms


@app.task(name="celery_send_sms_code")
def celery_send_sms_code(moblie,code):
    print("发送短信。》》》")
    Sms().send_message(moblie,(code,2))