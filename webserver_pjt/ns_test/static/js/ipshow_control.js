function swColor(){
	var sps = document.getElementsByClassName("spsty");
	for(var i=0;i<sps.length;i++)
	{	
		if(sps[i].getAttribute("name") == "1"){
			// sps[i].style.backgroundColor="#00FF00";
			sps[i].style.backgroundColor="rgba(0,255,0,0.8)";
		}else if(sps[i].getAttribute("name") == "0"){
			// sps[i].style.backgroundColor="#FF0000";
			sps[i].style.backgroundColor="rgba(255,0,0,0.8)";
		}else if(sps[i].getAttribute("name") == "3"){
			// sps[i].style.backgroundColor="#FF0000";
			sps[i].style.backgroundColor="rgba(255,150,0,1)";
		}else{
			sps[i].style.setProperty('background-color','#DCDCDC');
			sps[i].style.color = "red";
			sps[i].style.fontSize = "18px";
			sps[i].style.fontFamily = "宋体";
			sps[i].style.textAlign = "center";
			sps[i].style.lineHeight = "12px";
			sps[i].innerHTML = "!";
		}
	}
	setTimeout("rmStyle()", 1000);
}
function rmStyle(){
	var sps = document.getElementsByClassName("spsty");
	for(var i=0;i<sps.length;i++)
	{
		if(sps[i].getAttribute("name") == "1"){
			sps[i].removeAttribute("style");
		}
	}
}
function begin(){
	var _switch=setInterval("swColor()", 2000);
}
begin();
// swColor();