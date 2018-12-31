import httplib, urllib, base64

def bkreadFile (user):
   with open ("/home/acruz/Documents/EXPERIMENTO-SBIE/logs-photos/file_photos/"+user+".txt") as fp:
      for line in fp:
         photo = line.replace("\n", "")
         print(photo)
         send(user, photo)

def send(user, foto):
   headers = {
       # Request headers. Replace the placeholder key below with your subscription key.
       'Content-Type': 'application/json',
       'Ocp-Apim-Subscription-Key': '479e4da3956a4b9a90dba80e6be619b2',
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
