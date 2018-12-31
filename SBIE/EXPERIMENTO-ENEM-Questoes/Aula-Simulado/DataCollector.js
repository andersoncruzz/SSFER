var debug = true;
var timer;
var currentScreen = "";
var idClass = "";
//var ip = "localhost"; 
//var idAluno = "8";
console.log("DATA COLLECTOR FIRST");
var ip = localStorage.getItem('ip');
var idAluno = localStorage.getItem('idAluno');
var answerlist = localStorage.getItem('answerlist');
var aux_multioption = localStorage.getItem('multioption');

console.log("----");
console.log(aux_multioption);
aux_multioption = aux_multioption.split("/");
aux_question_multioption = aux_multioption[3].split(".");
aux_id_multioption = aux_multioption[1].split(",");
var multioption = {
    status: Boolean(aux_multioption[0]),
    id: aux_id_multioption,
    length: parseInt(aux_multioption[2]),
    question: aux_question_multioption
}
answerlist = answerlist.split(",");

console.log("answerlist: " + answerlist);
console.log(multioption);
/*var answerlist = ["0","0","0","0","0","0"];
var multioption = {
    status: false,
    id: "Q1-hard",
    len: "1",
    question: ["Q1-hard","Q2-hard","Q3-hard"]
} */

onload =  function(e){

	var html = document.querySelectorAll("html");
    currentScreen = e.target.baseURI.split("/").slice(-1)[0];
	for (var i=0;  i < html.length; i++) {
		html[i].addEventListener("click", listenClick);
	}

    timer = setInterval(overflowTimer, 2000);
}

function overflowTimer(){
   // idTela = getCookie("screen");
    var timestamp = new Date().getTime();

    if (currentScreen == "questionario.html" && idClass == "item" || currentScreen == "questionario.html#" && idClass == "item") {
        idClass = "Q:1:E:1-1";
    }

    if (currentScreen == "questionario.html" && idClass == "" || currentScreen == "questionario.html#" && idClass == "") {
        idClass = localStorage.getItem("idClass");
    }
    if (idClass == "troca-Q1 btn btn-info btn-lg"){
        idClass = "Q:1:E:1-1";
    } else if (idClass == "troca-Q2 btn btn-info btn-lg"){
        idClass = "Q:2:E:1-1";
    } else if (idClass == "troca-Q3 btn btn-info btn-lg"){
        idClass = "Q:3:E:1-1";
    } else if (idClass == "troca-Q4 btn btn-info btn-lg"){
        idClass = "Q:4:E:1-1";
    } else if (idClass == "troca-Q5 btn btn-info btn-lg"){
        idClass = "Q:5:E:1-1";
    } else if (idClass == "troca-Q6 btn btn-info btn-lg"){
        idClass = "Q:6:E:1-1";
    } else if (idClass == "troca-Q7 btn btn-info btn-lg"){
        idClass = "Q:7:E:1-1";
    } else if (idClass == "troca-Q8 btn btn-info btn-lg"){
        idClass = "Q:8:E:1-2";
    } else if (idClass == "troca-Q9 btn btn-info btn-lg"){
        idClass = "Q:9:E:1-2";
    } else if (idClass == "troca-Q10 btn btn-info btn-lg"){
        idClass = "Q:10:E:1-2";
    }


    if (idClass == "R:1:E:1-1 btn btn-info btn-lg"){
        idClass = "Q:1:H:1-1";
    } else if (idClass =="R:2:E:1-1 btn btn-info btn-lg"){
        idClass = "Q:2:H:1-1";
    } else if (idClass =="R:3:E:1-1 btn btn-info btn-lg"){
        idClass = "Q:3:H:1-1";
    } else if (idClass =="R:4:E:1-1 btn btn-info btn-lg"){
        idClass = "Q:4:H:1-1";
    } else if (idClass =="R:5:E:1-1 btn btn-info btn-lg"){
        idClass = "Q:5:H:1-1";
    } else if (idClass =="R:6:E:1-1 btn btn-info btn-lg"){
        idClass = "Q:6:H:1-1";
    } else if (idClass == "R:7:E:1-1 btn btn-info btn-lg"){
        idClass = "Q:7:H:1-1";
    } else if (idClass == "R:8:E:1-2 btn btn-info btn-lg"){
        idClass = "Q:8:H:1-2";
    } else if (idClass == "R:9:E:1-2 btn btn-info btn-lg"){
        idClass = "Q:9:H:1-2";
    } else if (idClass == "R:10:E:1-2 btn btn-info btn-lg"){
        idClass = "Q:10:H:1-2";
    }


    if (idClass == "D:1:H:1-1 close" || idClass == "C:1:H:1-1 close") idClass = "Q:1:H:1-1";
    else if (idClass == "D:2:H:1-1 close" || idClass == "C:2:H:1-1 close") idClass = "Q:2:H:1-1";
    else if (idClass == "D:3:H:1-1 close" || idClass == "C:3:H:1-1 close") idClass = "Q:3:H:1-1";
    else if (idClass == "D:4:H:1-1 close" || idClass == "C:4:H:1-1 close") idClass = "Q:4:H:1-1";
    else if (idClass == "D:5:H:1-1 close" || idClass == "C:5:H:1-1 close") idClass = "Q:5:H:1-1";
    else if (idClass == "D:6:H:1-1 close" || idClass == "C:6:H:1-1 close") idClass = "Q:6:H:1-1";
    else if (idClass == "D:7:H:1-1 close" || idClass == "C:7:H:1-1 close") idClass = "Q:7:H:1-1";
    else if (idClass == "D:8:H:1-2 close" || idClass == "C:8:H:1-2 close") idClass = "Q:8:H:1-2";
    else if (idClass == "D:9:H:1-2 close" || idClass == "C:9:H:1-2 close") idClass = "Q:9:H:1-2";
    else if (idClass == "D:10:H:1-2 close" || idClass == "C:10:H:1-2 close") idClass = "Q:10:H:1-2";
    else if (idClass == "D:1:E:1-1 close" || idClass == "C:1:E:1-1 close") idClass = "Q:1:E:1-1";
    else if (idClass == "D:2:E:1-1 close" || idClass == "C:2:E:1-1 close") idClass = "Q:2:E:1-1";
    else if (idClass == "D:3:E:1-1 close" || idClass == "C:3:E:1-1 close") idClass = "Q:3:E:1-1";
    else if (idClass == "D:4:E:1-1 close" || idClass == "C:4:E:1-1 close") idClass = "Q:4:E:1-1";
    else if (idClass == "D:5:E:1-1 close" || idClass == "C:5:E:1-1 close") idClass = "Q:5:E:1-1";
    else if (idClass == "D:6:E:1-1 close" || idClass == "C:6:E:1-1 close") idClass = "Q:6:E:1-1";
    else if (idClass == "D:7:E:1-1 close" || idClass == "C:7:E:1-1 close") idClass = "Q:7:E:1-1";
    else if (idClass == "D:8:E:1-2 close" || idClass == "C:8:E:1-2 close") idClass = "Q:8:E:1-2";
    else if (idClass == "D:9:E:1-2 close" || idClass == "C:9:E:1-2 close") idClass = "Q:9:E:1-2";
    else if (idClass == "D:10:E:1-2 close" || idClass == "C:10:E:1-2 close") idClass = "Q:10:E:1-2";

//localStorage.setItem ("classIdSection", "1-4,1-4,1-3,1-2,1-1,1-3,1-1,1-3,1-1,1-1");
    localStorage.setItem("idClass",idClass);

    if(debug) {
       /* console.log("-------after two seconds----------");
        console.log("DataCollector timestamp: "+timestamp);
        console.log("Tela Atual: "+currentScreen);*/
    }

    $.post("https://"+ ip +":5000/storage/1",
        {
            idUser: idAluno,
            timeStamp: timestamp,
            tipo: null,
            tela: currentScreen,
            tag: null,
            x: null,
            y: null,
			//	adaptacao: "1",
       //     id: idTela,
            classId: idClass
        },
        function(data, status){
            //console.log("PLAYER------Data: " + data + "\nStatus: " + status);
        if (currentScreen == "questionario.html" || currentScreen == "questionario.html#") {    
            response = data.recommendation[0].recommendation;
            questions = data.recommendation[1].questions;
            response = response.split(";");
            questions = questions.split(",");
            console.log("response: " + response);
            //console.log("response len: " + response.length);
            console.log("questions: " + questions);
            if (response.length > 1){
                multioption.status = true;
                multioption.length = response.length;
                multioption.id = response;
                multioption.question = questions;
               // console.log("multioption " + multioption.question[1]);
            } else {
                multioption.status = false;
                multioption.length = response.length;
                multioption.id = response;
                multioption.question = questions;
            }
            aux_questions = ""
            for (var i=0; i<questions.length; i++){
                if (i==0){
                    aux_questions = questions[i];    
                } else{
                    aux_questions = aux_questions + "." + questions[i];
                }        
            }
            console.log("------");
            console.log(multioption);

            localStorage.setItem ("multioption",""+multioption.status.toString()+"/"+
                                                    multioption.id + "/" + 
                                                    multioption.length + "/"+
                                                    aux_questions);

            }
        });
}

var escolha;
window.confirm = function(al, $){
    return function(msg) {
        al.call(window,msg);
        $(window).trigger("confirmacao");
    };
}(window.confirm, window.jQuery);


$(window).on("confirmacao", function(e) {
    console.log("escolhi: "+escolha);
});


function listenClick(e){
    clearInterval(timer);
    timer = setInterval(overflowTimer, 2000);
    currentScreen = e.target.baseURI.split("/").slice(-1)[0];
    
    if (e.target.className == "modal fade"){
        idClass = "Q" + idClass.substring(1, idClass.length); 
    } else if (e.target.className == "clickbody"){
        idClass = idClass;
    }
     else {
        idClass = e.target.className;
    }


    if (e.target.className == "Q:1:H:1-1 list-group-item" && multioption.question[0] == "Q1-easy" ) idClass = "Q:1:E:1-1 list-group-item";
    else if (e.target.className == "Q:2:H:1-1 list-group-item" && multioption.question[1] == "Q2-easy") idClass = "Q:2:E:1-1 list-group-item";
    else if (e.target.className == "Q:3:H:1-1 list-group-item" && multioption.question[2] == "Q3-easy") idClass = "Q:3:E:1-1 list-group-item";
    else if (e.target.className == "Q:4:H:1-1 list-group-item" && multioption.question[3] == "Q4-easy") idClass = "Q:4:E:1-1 list-group-item";
    else if (e.target.className == "Q:5:H:1-1 list-group-item" && multioption.question[4] == "Q5-easy") idClass = "Q:5:E:1-1 list-group-item";
    else if (e.target.className == "Q:6:H:1-1 list-group-item" && multioption.question[5] == "Q6-easy") idClass = "Q:6:E:1-1 list-group-item";
    else if (e.target.className == "Q:7:H:1-1 list-group-item" && multioption.question[6] == "Q7-easy") idClass = "Q:7:E:1-1 list-group-item";
    else if (e.target.className == "Q:8:H:1-2 list-group-item" && multioption.question[7] == "Q8-easy") idClass = "Q:8:E:1-2 list-group-item";
    else if (e.target.className == "Q:9:H:1-2 list-group-item" && multioption.question[8] == "Q9-easy") idClass = "Q:9:E:1-2 list-group-item";
    else if (e.target.className == "Q:10:H:1-2 list-group-item" && multioption.question[9] == "Q10-easy") idClass = "Q:10:E:1-2 list-group-item";
    
    //localStorage.setItem ("classIdSection", "1-4,1-4,1-3,1-2,1-1,1-3,1-1,1-3,1-1,1-1");
    //console.log("IDCLASS: " + idClass);

    //PARTE DA RESPOSTA
    if (e.target.defaultValue != undefined) {
        console.log("target class: " + e.target.className[2]);
        console.log("answlist before:" + answerlist);
        aux = e.target.className;
        aux = aux.split(":");
        console.log("--------");
        console.log(aux);
        i = parseInt(aux[1]);
        if (aux[2] == "H")
            answerlist[i-1] = e.target.defaultValue;
        else
            answerlist[i-1+10] = e.target.defaultValue;
        console.log("answlist after:" + answerlist);

        aux_answerlist = "";
        for (var i=0; i<answerlist.length; i++) {
            if (i==0) aux_answerlist = answerlist[i];
            else aux_answerlist = aux_answerlist + "," + answerlist[i];
        }
        localStorage.setItem ("answerlist", aux_answerlist);

/*        i = parseInt(e.target.className[2])
        console.log(i);
        iterador = i-1;
        answerlist[iterador] = e.target.defaultValue;
        console.log(answerlist);*/
    }



    //idTela = getCookie("screen");
    var timestamp = new Date().getTime();
    /*var tag = e.target.localName;
    if (e.target.localName == "input") {
       // console.log("INPUT");
        tag = e.target.localName + "-" + e.target.defaultValue;
        //console.log("INPUT: " + tag);
    }*/

    /*if(debug) {
       console.log("-----------------");
        console.log(e);
        console.log("tela:" + currentScreen);
        console.log("x: " + e.screenX + " y: " + e.screenY);
        console.log(e.type);
        console.log("target id: " + e.target.id);
        console.log("target class: " + e.target.className);
        console.log("selected option:", e.target.defaultValue);
        console.log(e.target.localName);
      //  console.log(tag);
        console.log(e.timeStamp);
        console.log(e.which);
        console.log("DataCollector timestamp: "+timestamp); 
    }*/

    localStorage.setItem("idClass",idClass);

    $.post("https://"+ ip +":5000/storage/1",
    {
      idUser: idAluno,
      timeStamp: timestamp,
      tipo: e.type,
      tela: currentScreen,
      tag: e.target.localName,
      x:e.screenX,
      y:e.screenY,
		adaptacao: "1",
     // alternativaSelecionada: e.target.defaultValue,
//      id: idTela,
      classId: idClass
    },
    function(data, status){
        console.log("currentScreen: " + currentScreen);
        if (currentScreen == "questionario.html" || currentScreen == "questionario.html#") {     
            response = data.recommendation[0].recommendation;
            questions = data.recommendation[1].questions;
            response = response.split(";");
            questions = questions.split(",")
            console.log("response: " + response);
            //console.log("response len: " + response.length);
            console.log("questions: " + questions);
            if (response.length > 1){
                multioption.status = true;
                multioption.length = response.length;
                multioption.id = response;
                multioption.question = questions;
                //console.log("multioption " + multioption.question);
            } else {
                multioption.status = false;
                multioption.length = response.length;
                multioption.id = response;
                multioption.question = questions;
            }
            //localStorage.setItem ("answerlist", "0,0,0,0,0,0");
            //localStorage.setItem ("multioption","false,Q1-hard,1,Q1-hard.Q2-hard.Q3-hard");
            aux_questions = ""
            for (var i=0; i<questions.length; i++){
                if (i==0){
                    aux_questions = questions[i];    
                } else{
                    aux_questions = aux_questions + "." + questions[i];
                }        
            }

            console.log("--------");
            console.log(multioption);
            localStorage.setItem ("multioption",""+multioption.status.toString()+"/"+
                                                    multioption.id + "/" + 
                                                    multioption.length + "/"+
                                                    aux_questions);

            }
        });
}

function listemMouseOver(e){
	console.log(e.target);
}

function listemMouseOut(e){
	console.log(e.target);
}
