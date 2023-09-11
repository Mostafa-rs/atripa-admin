import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "127.0.0.1"
SMTP_PORT = 587
USERNAME = "no_reply@atripa"
PASSWORD = "Ktbr@v3h6?c83vH?$X1INH"
CONTEX = ssl.create_default_context()
SENDER = "no_reply@atripa.com"


def send_email_otp(name, receiver, code):
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "آتریپا - کد احراز رایانامه"
        message["From"] = SENDER
        message["To"] = receiver
        html = """\
        <div>
            <div>
                <div style="Margin:0;box-sizing:border-box;color:#0a0a0a;font-family:Roboto,sans-serif;font-size:16px;
                font-weight:400;line-height:1.3;margin:0;min-width:100%;padding:0;text-align:left;width:100%!important">
                    <span style="color:#fff;display:none!important;font-size:1px;line-height:1px;max-height:0;max-width:
                    0;opacity:0;overflow:hidden"></span>
                    <table style="Margin:0;background-color:#041866;background-image:linear-gradient(135deg,#021038 
                    0,#041866 100%)!important;border-collapse:collapse;border-color:transparent;border-spacing:0;color:
                    #0a0a0a;font-family:Roboto,sans-serif;font-size:16px;font-weight:400;height:100%;line-height:1.3;
                    margin:0;padding:0;text-align:left;vertical-align:top;width:100%"><tbody><tr style="padding:0;text-
                    align:left;vertical-align:top"><td align="center" valign="top" style="Margin:0;border-collapse:
                    collapse!important;color:#0a0a0a;font-family:Roboto,sans-serif;font-size:16px;font-weight:400;line-
                    height:1.3;margin:0;padding:0;text-align:left;vertical-align:top;word-wrap:break-word"><center 
                    style="min-width:580px;width:100%">
                        <table style="Margin:0 auto;border-collapse:collapse;border-color:transparent;border-spacing:0;
                        float:none;margin:0 auto;padding:0;text-align:center;vertical-align:top;width:100%"><tbody><tr 
                        style="padding:0;text-align:left;vertical-align:top">
                            <td height="40px" style="Margin:0;border-collapse:collapse!important;color:#0a0a0a;font-
                            family:Roboto,sans-serif;font-size:40px;font-weight:400;line-height:40px;margin:0;padding:
                            0;text-align:left;vertical-align:top;word-wrap:break-word">&nbsp;</td>
                        </tr></tbody></table>
                        <table align="center" style="Margin:0 auto;background:0 0;border-collapse:collapse;border-color:
                        transparent;border-spacing:0;float:none;margin:0 auto;padding:0;text-align:center;vertical-align
                        :top;width:580px;max-width:580px"><tbody><tr style="padding:0;text-align:left;vertical-align:top
                        "><td style="Margin:0;border-collapse:collapse!important;color:#0a0a0a;font-family:Roboto,sans-
                        serif;font-size:16px;font-weight:400;line-height:1.3;margin:0;padding:0;text-align:left;vertical
                        -align:top;word-wrap:break-word">
                            <table style="background:0 0;border-collapse:collapse;border-color:transparent;border-
                            spacing:0;display:table;padding:0;text-align:left;vertical-align:top;width:100%"><tbody>
                                <tr style="padding:0;text-align:left;vertical-align:top"><th style="Margin:0 auto;color:
                                #0a0a0a;font-family:Roboto,sans-serif;font-size:16px;font-weight:400;line-height:1.3;
                                margin:0 auto;padding:0;padding-bottom:0;padding-left:0;padding-right:0;text-align:left;
                                width:200px">
                                    <table style="border-collapse:collapse;border-color:transparent;border-spacing:0;
                                    padding:0;text-align:left;vertical-align:top;width:100%"><tbody><tr style="padding:0
                                    ;text-align:left;vertical-align:top"><th valign="middle" height="49" style="Margin:0
                                    ;color:#0a0a0a;font-family:Roboto,sans-serif;font-size:16px;font-weight:400;line-
                                    height:1.3;margin:0;padding:0;text-align:left"></th></tr></tbody></table>
                                </th></tr>
                            </tbody></table>
                        </td></tr></tbody></table>
                        <table style="Margin:0 auto;border-collapse:collapse;border-color:transparent;border-spacing:0;
                        float:none;margin:0 auto;padding:0;text-align:center;vertical-align:top;width:100%"><tbody><tr 
                        style="padding:0;text-align:left;vertical-align:top"><td height="32px" style="Margin:0;border-
                        collapse:collapse!important;color:#0a0a0a;font-family:Roboto,sans-serif;font-size:32px;font-
                        weight:400;line-height:32px;margin:0;padding:0;text-align:left;vertical-align:top;word-wrap:
                        break-word">&nbsp;</td></tr></tbody></table>
                        <table cellspacing="0" cellpadding="0" border="0" align="center" style="Margin:0 auto;border-
                        bottom-left-radius:3px;border-bottom-right-radius:3px;border-collapse:collapse;border-color:
                        transparent;border-spacing:0;float:none;margin:0 auto;padding:0;text-align:center;vertical-align
                        :top;width:580px;max-width:580px"><tbody><tr style="padding:0;text-align:left;vertical-align:top
                        ">
                            <td style="Margin:0;border-collapse:collapse!important;color:#0a0a0a;font-family:Roboto,sans
                            -serif;font-size:16px;font-weight:400;line-height:1.3;margin:0;padding:0;text-align:left;
                            vertical-align:top;word-wrap:break-word;max-width:600px!important">
                                <table style="border-left-color:#e6e6e6!important;border-bottom-color:#e6e6e6!important;
                                border-right-color:#e6e6e6!important;border-width:0;border-style:solid;border-bottom-
                                left-radius:3px;border-bottom-right-radius:3px;border-color:#e6e6e6;border-top:none;
                                display:table-cell;padding-bottom:32px;border-spacing:48px 0;border-collapse:separate;
                                width:100%!important;background:#fff;max-width:600px"><tbody><tr><td>
                                    <table style="border-collapse:collapse;border-color:transparent;border-spacing:0;dis
                                    play:table;padding:0;text-align:left;vertical-align:top;width:100%"><tbody><tr style
                                    ="padding:0;text-align:left;vertical-align:top"></tr></tbody></table>
                                    <table style="border-collapse:collapse;border-color:transparent;border-spacing:0;
                                    padding:0;text-align:left;vertical-align:top;width:100%"><tbody><tr style="padding:0
                                    ;text-align:left;vertical-align:top"><td height="32px" style="Margin:0;border-
                                    collapse:collapse!important;color:#0a0a0a;font-family:Roboto,sans-serif;font-size:32
                                    px;font-weight:400;line-height:32px;margin:0;padding:0;text-align:left;vertical-
                                    align:top;word-wrap:break-word"></td></tr></tbody></table>
                                    <div style="text-align:right">&nbsp;</div>
                                    <div style="text-align:right">
                                        <span style="font-size:small;font-family:Vazir,IRANSans,Iransans,IranSansWeb,B 
                                        Mitra,B Nazanin,arial,calibri,tahoma;color:#fff;">""" + name + """
                                        عزیز</span><br>
                                        <span style="font-size:small;font-family:Vazir,IRANSans,Iransans,IranSansWeb,B 
                                        Mitra,B Nazanin,arial,calibri,tahoma;color:#fff;">
                                        کد احراز ایمیل شما در سامانه آتریپا 
                                        """ + code + """ می باشد</span>
                                    </div>
                                    <div style="text-align:right">&nbsp;</div>
                                    <div style="text-align:right">&nbsp;</div>
                                    <p style="text-align:center" align="right"><span style="font-size:14pt">
                                        <strong><span style="font-family:Vazir,IRANSans,Iransans,IranSansWeb,B Mitra,B 
                                        Nazanin,arial,calibri,tahoma">
                                            <a style="background-color:#0069ff;display:inline-block;color:#fff;padding:
                                            15px 30px;border-radius:3px;text-decoration:none;font-weight:bold" href=
                                            "https://www.atripa.com/" target="_blank">سامانه هوشمند سفر آتریپا</a>
                                        </span></strong>
                                    </span></p>
                                </td></tr></tbody></table>
                                <div style="display:none;white-space:nowrap;font:15px courier;line-height:0">&nbsp; 
                                &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
                                &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
                                &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div>
                                <table style="border-collapse:collapse;border-color:transparent;border-spacing:0;padding
                                :0;text-align:left;vertical-align:top;width:100%;background:transparent"><tbody><tr 
                                style="padding:0;text-align:left;vertical-align:top"></tr></tbody></table>
                            </td>
                        </tr></tbody></table>
                    </center></td></tr></tbody></table>
                </div>
            </div>
        </div>"""
        part1 = MIMEText(html, "html")
        message.attach(part1)
        server = smtplib.SMTP("localhost")
        server.login(USERNAME, PASSWORD)
        server.sendmail("no_reply@atripa.com", receiver, message.as_string())
        server.quit()
        return [1, f"{receiver} - {message}"]
    except Exception as e:
        return [0, str(e)]
