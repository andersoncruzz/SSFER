def sq(nro):
   qfile = open('/home/acruz/Documents/EXPERIMENTO-ENEM/questoes/q' + nro + '.txt', 'r').read()
   string = qfile.split("#")

   template = """<div class="question" id="Q""" + nro + """-hard">
      <h1 class="Q:""" + nro + """:H:1-2">Questão """ + nro + """ - Principal</h1>
      <p class="Q:""" + nro + """:H:1-2">""" + string[0] +"""<br></p>
      <div class="alternativas">

         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:A" id="Q:""" + nro + """:H:1-2:A" type="radio" name="1" value="A">A) """ + string[1] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:B" id="Q:""" + nro + """:H:1-2:B" type="radio" name="1" value="B">B) """ + string[2] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:C" id="Q:""" + nro + """:H:1-2:C" type="radio" name="1" value="C">C) """ + string[3] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:D" id="Q:""" + nro + """:H:1-2:D" type="radio" name="1" value="D">D) """ + string[4] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:E" id="Q:""" + nro + """:H:1-2:E" type="radio" name="1" value="E">E) """ + string[5] + """</label>
         </div>
      </div>
      <!--<button type="button" id="A""" + nro + """-hard" class="Q:""" + nro + """:H:1-2 btn btn-info btn-lg">Responder</button> -->
      <button type="button" id="D""" + nro + """-hard" class="D:""" + nro + """:H:1-2 btn btn-info btn-lg" data-toggle="modal" data-target="#tip-Q""" + nro + """-hard">Sugestão</button>
      <button type="button" id="C""" + nro + """-hard" class="C:""" + nro + """:H:1-2 btn btn-info btn-lg" data-toggle="modal" data-target="#my-contentQ""" + nro +"""-hard">Consultar ao conteúdo</button>	
   </div>
   <!-- Fim da div de uma questão-->
   <div id="tip-Q"""+nro+"""-hard" class="modal fade" role="dialog">
      <div class="modal-dialog">
         <!-- Modal content-->
         <div class="modal-content">
            <div class="modal-header">
               <button type="button" class="D:"""+nro+""":H:1-2 close" data-dismiss="modal">&times;</button>
               <h4 class="modal-title">Sugestão para Questão """+nro+"""</h4>
            </div>
            <div class="modal-body">
               <p>As ondas eletromasnéticas</p>
            </div>
            <div class="modal-footer">
               <button type="button" class="D:"""+nro+""":H:1-2 btn btn-default " data-dismiss="modal">Fechar</button>
            </div>
         </div>
      </div>
   </div>
   <!-- modal que fica escondido para trocar questão -->
   <div class="container">
   </div>
   <!-- para voltar ao conteúdo -->
   <div id="my-contentQ"""+nro+"""-hard" class="modal fade" role="dialog">
  	<div class="modal-dialog modal-lg">

           <!-- Modal content-->
           <div class="modal-content">
              <div class="modal-header">
                 <button type="button" class="C:"""+nro+""":H:1-2 close" data-dismiss="modal">&times;</button>
                 <h4 class="modal-title">1-2</h4>
              </div>
              <div class="modal-body">
                 <iframe id="content-frame" src="../c1-2.html"></iframe>
              </div>
              <div class="modal-footer">
                 <button type="button" class="C:"""+nro+""":H:1-2 close" data-dismiss="modal">&times;</button>
              </div>
           </div>
        </div>
   </div>
   
   """
   template = template.replace("\n", "")
   template = template.replace("\t", "")
   return template


def sque(nro):
   qfile = open('/home/acruz/Documents/EXPERIMENTO-ENEM/questoes/q' + nro + '.txt', 'r').read()
   string = qfile.split("#")

   template = """<div class="question" id="Q""" + nro + """-hard">
      <h1 class="Q:""" + nro + """:H:1-2">Questão """ + nro + """ - Principal</h1>
      <p class="Q:""" + nro + """:H:1-2">""" + string[0] +"""<br></p>
      <div class="alternativas">

         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:A" id="Q:""" + nro + """:H:1-2:A" type="radio" name="1" value="A">A) """ + string[1] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:B" id="Q:""" + nro + """:H:1-2:B" type="radio" name="1" value="B">B) """ + string[2] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:C" id="Q:""" + nro + """:H:1-2:C" type="radio" name="1" value="C">C) """ + string[3] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:D" id="Q:""" + nro + """:H:1-2:D" type="radio" name="1" value="D">D) """ + string[4] + """</label>
         </div>
         <div class="radio">
            <label><input class="Q:""" + nro + """:H:1-2:E" id="Q:""" + nro + """:H:1-2:E" type="radio" name="1" value="E">E) """ + string[5] + """</label>
         </div>
      </div>
      <!--<button type="button" id="A""" + nro + """-hard" class="Q:""" + nro + """:H:1-2 btn btn-info btn-lg">Responder</button> -->
      <button type="button" id="D""" + nro + """-hard" class="D:""" + nro + """:H:1-2 btn btn-info btn-lg" data-toggle="modal" data-target="#tip-Q""" + nro + """-hard">Sugestão</button>
      <button type="button" id="C""" + nro + """-hard" class="C:""" + nro + """:H:1-2 btn btn-info btn-lg" data-toggle="modal" data-target="#my-contentQ""" + nro +"""-hard">Consultar ao conteúdo</button>	
   </div>
   """
   template = template.replace("\n", "")
   template = template.replace("\t", "")
   return template
