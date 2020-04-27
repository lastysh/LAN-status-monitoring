function swColor(){
	var sps = document.getElementsByClassName('spsty');
	for(var i=0;i<sps.length;i++)
	{	
		if(sps[i].getAttribute("name") == "1"){
			// sps[i].style.backgroundColor="#00FF00";
			sps[i].style.backgroundColor="rgba(0,255,0,0.8)";
		}else if(sps[i].getAttribute("name") == "0"){
			// sps[i].style.backgroundColor="#FF0000";
			sps[i].style.backgroundColor="rgba(255,0,0,0.8)";
		}
	}
	setTimeout("rmStyle()", 1000);
}
function rmStyle(){
	var sps = document.getElementsByClassName('spsty');
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