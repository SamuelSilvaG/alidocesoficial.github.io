from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication
import smtplib, time, os, smtplib, sys

def envia(getmail):



	corpoemail ="""
	<!DOCTYPE html>
<html >
   <head>
      <meta charset="UTF-8">
      <title>Alidoces Oficial</title>
   </head>
   <body>
      <div style="display: none; font-size: 1px; color: #333; line-height: 1px; font-family: Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
         Produto do dia! Abre esse email e confira!
      </div>
      <table width="100%" bgcolor="#eeeeee" border="0" cellspacing="0" cellpadding="0">
         <tr>
            <td align="center">
               <table width="100%" bgcolor="#eeeeee" border="0" cellspacing="0" cellpadding="0">
                  <tr bgcolor="#eeeeee"  >
                     <td bgcolor="#eeeeee" align="center" style="font-family:sans-serif; font-size:20px; padding:10px; line-height:auto; color:#333;">
                        <img src="https://user-images.githubusercontent.com/4019334/29381154-abf112a0-829e-11e7-8bd3-88d396ae7689.PNG" alt="Lopes" width="400" style="display:block;font-size: 19px;font-family:Arial, Helvetica, sans-serif;"> 
                     </td>
                  </tr>
               </table>
               <table width="100%" border="0" cellspacing="0" bgcolor="#eeeeee" align="center" style=" max-width:550px;" cellpadding="0">
                  <tr>
                     <td bgcolor="#eeeeee" align="center" style="font-family:sans-serif; line-height:auto; color:#333; max-width:550px;"><a href="https://www.lopes.com.br/imovel/apartamento-3-dormitorios-cambuci-sao+paulo-com-garagem-72m2-ref-14894?&utm_campaign=Livingresort-v3&utm_source=Crm-Lps&utm_medium=emkt&utm_content=_img" target="_blank">
                        <img src="%s" alt="Conhe&ccedil;a  Living Resort" width="550" style="border-radius: 1rem;display:block; max-width:550px;"/></a>
                     </td>
                  </tr>
                  <tr>
                     <td bgcolor="#eeeeee" align="center" width="100%" >
                        <h1 style="font-family:Helvetica; font-size:30px; color:#333">%s</h1>
                  </tr>
                  <tr bgcolor="#eeeeee">
                     <td bgcolor="#eeeeee" align="center" width="100%" style="font-family:sans-serif, Helvetica; font-size:16px; padding:5px; color:#333">%s</td>
                  </tr>
               </table>
               <table cellpadding="0" cellspacing="0" width="100%" bgcolor="#eeeeee" align="center">
                  <tr>
                     <td align="center">
                        <table bgcolor="#eee" align="center" width="100%" cellspacing="0" cellpadding="0" style="padding:5px; max-width:550px;" >
                           <tr>
                              <td class="column" align="center"><a href="https://web.whatsapp.com/send?l=pt&phone=5511981909548&text=Gostaria de  Informações" target="_blank"><img src="http://www2.lopes.com.br/multimidia/divulgacao/living_resort/img/chat_ok.gif" alt="Info" style="display:block; margin:0 auto; text-align:center"/></a></td>
                           </tr>
                        </table>
                     </td>
                  </tr>
               </table>
      </table>
      <table width="100%" border="0" cellspacing="0" bgcolor="#eee" cellpadding="0">
         <tr>
            <td width="100%" align="center" height="40" >
               <a href="https://www.facebook.com/pages/Lopes-Consultoria-de-Imoveis/186729691112" target="_blank">
                  <?xml version="1.0" encoding="iso-8859-1"?>
                  <!-- Generator: Adobe Illustrator 19.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
                  <svg style="width: 2rem;" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                     viewBox="0 0 291.319 291.319" style="enable-background:new 0 0 291.319 291.319;" xml:space="preserve">
                     <g>
                        <path style="fill:#3B5998;" d="M145.659,0c80.45,0,145.66,65.219,145.66,145.66c0,80.45-65.21,145.659-145.66,145.659
                           S0,226.109,0,145.66C0,65.219,65.21,0,145.659,0z"/>
                        <path style="fill:#FFFFFF;" d="M163.394,100.277h18.772v-27.73h-22.067v0.1c-26.738,0.947-32.218,15.977-32.701,31.763h-0.055
                           v13.847h-18.207v27.156h18.207v72.793h27.439v-72.793h22.477l4.342-27.156h-26.81v-8.366
                           C154.791,104.556,158.341,100.277,163.394,100.277z"/>
                     </g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                  </svg>
               </a>
               <a href="http://instagram.com/lopesimoveis" target="_blank">
                  <svg style ="width: 2rem;" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                     viewBox="0 0 112.197 112.197" style="enable-background:new 0 0 112.197 112.197;" xml:space="preserve">
                     <g>
                        <circle style="fill:#55ACEE;" cx="56.099" cy="56.098" r="56.098"/>
                        <g>
                           <path style="fill:#F1F2F2;" d="M90.461,40.316c-2.404,1.066-4.99,1.787-7.702,2.109c2.769-1.659,4.894-4.284,5.897-7.417
                              c-2.591,1.537-5.462,2.652-8.515,3.253c-2.446-2.605-5.931-4.233-9.79-4.233c-7.404,0-13.409,6.005-13.409,13.409
                              c0,1.051,0.119,2.074,0.349,3.056c-11.144-0.559-21.025-5.897-27.639-14.012c-1.154,1.98-1.816,4.285-1.816,6.742
                              c0,4.651,2.369,8.757,5.965,11.161c-2.197-0.069-4.266-0.672-6.073-1.679c-0.001,0.057-0.001,0.114-0.001,0.17
                              c0,6.497,4.624,11.916,10.757,13.147c-1.124,0.308-2.311,0.471-3.532,0.471c-0.866,0-1.705-0.083-2.523-0.239
                              c1.706,5.326,6.657,9.203,12.526,9.312c-4.59,3.597-10.371,5.74-16.655,5.74c-1.08,0-2.15-0.063-3.197-0.188
                              c5.931,3.806,12.981,6.025,20.553,6.025c24.664,0,38.152-20.432,38.152-38.153c0-0.581-0.013-1.16-0.039-1.734
                              C86.391,45.366,88.664,43.005,90.461,40.316L90.461,40.316z"/>
                        </g>
                     </g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                     <g></g>
                  </svg>
               </a>
            </td>
         </tr>
         <tr bgcolor="#eeeeee"  >
            <td bgcolor="#eeeeee" align="center" height="40" width="100%" style="font-family:'Trebuchet MS', Arial, Helvetica, sans-serif; font-size:10px; color:#333">
               <span style="font-family:Arial, Helvetica, sans-serif; font-size:11px; color:#333;">LPS Brasil - Consultoria de Im&oacute;veis S/A -  Rua Estados Unidos,1971 - S&atilde;o Paulo - SP</span><br>
               <span style="font-family:Arial, Helvetica, sans-serif; font-size:9px; color:#333;"> </span>CRECI/SP n&deg;J-19585 
            </td>
         </tr>
      </table>
      </td></tr>
      </table>
   </body>
</html>
""" % (imagembolo, bolo, descricaobolo)

def enviamial(corpoemail)
	texto = MIMEText(corpoemail)
    env.attach(texto)
    arquivo = MIMEApplication(open(file_arquivo,"rb").read())
    arquivo.add_header('Content-Disposition', 'anexo', filename=file_arquivo)
    env.attach(arquivo)
    try:
        gm = smtplib.SMTP("smtp.gmail.com", 587)
        gm.ehlo()
        gm.starttls()
        gm.ehlo()
        gm.login(gmail, passwd)
        gm.sendmail(env['From'], env['To'], env.as_string())
        gm.close()
        print (frescurinha.OKGREEN + "[+] - Meus parabéns seu email foi enviado com sucesso." + frescurinha.ENDC)
        print
    except:
        print (frescurinha.FAIL + "[!] - Ops! Não consegui encaminhar o seu email :( " + frescurinha.ENDC)
        pass


def emails():

	lista =["nglauzer@gmail.com"]

	for getmail in lista:
		envia(getmail)

emails()