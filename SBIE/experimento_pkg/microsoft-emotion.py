########### Python 2.7 #############
import httplib, urllib, base64


def send(user, foto):
   headers = {
       # Request headers. Replace the placeholder key below with your subscription key.
       'Content-Type': 'application/json',
       'Ocp-Apim-Subscription-Key': 'a4758a2589fb409f9c8892d293576583',
   }

   params = urllib.urlencode({
   })

   # Replace the example URL below with the URL of the image you want to analyze.
   #body = "{ 'url': 'http://gisexp.icomp.ufam.edu.br/julio.png' }"
   body = "{ 'url': 'http://gisexp.icomp.ufam.edu.br/fotos/"+user+"/"+foto+"' }"
   print (body)
   try:
       # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
       #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
       #   URL below with "westcentralus".
       conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
       conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
       response = conn.getresponse()
       data = response.read()
       #print (data)
       print(foto +"$" + data + "\n")
       log = open("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-classification/"+user+".csv", "a+")
       log.write(foto +"$"  + data  + "\n")
       log.close()
       #print(data)
       conn.close()
   except Exception as e:
       print("[Errno {0}] {1}".format(e.errno, e.strerror))
