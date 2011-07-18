// JavaScript Document

function validarFormulariRegistre(){

var isNotOk=false;

var username = window.document.registrar.username.value;
if (username==""){
	document.getElementById("username").style.display="inline";
	isNotOk=true;
}else{
	document.getElementById("username").style.display="none";
}

var password = window.document.registrar.password.value;
if (password==""){
	document.getElementById("password").style.display="inline";
	isNotOk=true;
}else{
	document.getElementById("password").style.display="none";
}

var confirm_password= window.document.registrar.confirm_password.value;
if (password!=confirm_password){
	document.getElementById("confirm_password").style.display="inline";
	isNotOk=true;
}else{
	document.getElementById("confirm_password").style.display="none";
}

var email = window.document.registrar.email.value;
var i;
var longitud = email.length;
var out = false;
for(i=0;i<longitud;i++){
	if(email.charAt(i)=="@"){
		out = true;
	}
}

if(out){
	document.getElementById("email").style.display="none";
}else{
	document.getElementById("email").style.display="inline";
	isNotOk=true;
}

var integrants = window.document.registrar.integrants.value;
if (integrants==""){
        document.getElementById("integrants").style.display="inline";
        isNotOk=true;
}else{
        document.getElementById("integrants").style.display="none";
}

var escola_universitat = window.document.registrar.escola_universitat.value;
if (escola_universitat==""){
        document.getElementById("escola_universitat").style.display="inline";
        isNotOk=true;
}else{
        document.getElementById("escola_universitat").style.display="none";
}


if (!isNotOk){
	window.document.registrar.submit();
}


}


function validarFormulariModificacio(){

var isNotOk = false;

var email = window.document.modificar.email.value;
var i;
var longitud = email.length;
var out = false;
for(i=0;i<longitud;i++){
        if(email.charAt(i)=="@"){
                out = true;
        }
}

if(out){
        document.getElementById("email").style.display="none";
}else{
        document.getElementById("email").style.display="inline";
        isNotOk=true;
}

var integrants = window.document.modificar.integrants.value;
if (integrants==""){
        document.getElementById("integrants").style.display="inline";
        isNotOk=true;
}else{
        document.getElementById("integrants").style.display="none";
}

var escola_universitat = window.document.modificar.escola_universitat.value;
if (escola_universitat==""){
        document.getElementById("escola_universitat").style.display="inline";
        isNotOk=true;
}else{
        document.getElementById("escola_universitat").style.display="none";
}

if (!isNotOk){
        window.document.modificar.submit();
}
}

function validarFormulariSubmit(){

var isNotOk=false;

if(!document.presentar.title.value){
	document.getElementById("title").style.display="inline";
        isNotOk=true;}

if(!document.presentar.file.value){
        document.getElementById("file").style.display="inline";
        isNotOk=true;}

if(!document.presentar.comments.value){
        document.getElementById("comments").style.display="inline";
        isNotOk=true;}


if (!isNotOk){
	window.document.presentar.submit();
}
}

function validarFormulariPassword(){

var isNotOk=false;

var new_passwd = window.document.modpass.new_passwd.value;
if (new_passwd==""){
        document.getElementById("new_passwd").style.display="inline";
        isNotOk=true;
}else{
        document.getElementById("new_passwd").style.display="none";
}

var confirm_password= window.document.modpass.confirm_password.value;
if (new_passwd!=confirm_password){
        document.getElementById("confirm_password").style.display="inline";
        isNotOk=true;
}else{
        document.getElementById("confirm_password").style.display="none";
}

if (!isNotOk){
        window.document.modpass.submit();
}
}

