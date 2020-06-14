function load(){
	var _switch=setInterval("swColor()", 2000);
}

function swColor(){
	var sps = document.getElementsByClassName("sp_style");
	for(var i=0;i<sps.length;i++)
	{	
		if(sps[i].getAttribute("name") == "1"){
			// sps[i].style.backgroundColor="#00FF00";
			sps[i].style.backgroundColor="rgba(0,255,0,0.8)";
		}else if(sps[i].getAttribute("name") == "0"){
			// sps[i].style.backgroundColor="#FF0000";
			sps[i].style.backgroundColor="rgba(255,0,0,0.8)";
		}else if(sps[i].getAttribute("name") == "2"){
			// sps[i].style.backgroundColor="#FF0000";
			sps[i].style.backgroundColor="rgba(255,150,0,1)";
		}else{
			sps[i].style.setProperty('background-color','#DCDCDC');
			sps[i].style.color = "#FF4500";
			sps[i].style.fontSize = "25px";
			sps[i].style.fontFamily = "宋体";
			sps[i].style.textAlign = "center";
			sps[i].style.lineHeight = "13px";
			sps[i].innerHTML = "⚡︎";
		}
	}
	setTimeout("rmStyle()", 1000);
}

function rmStyle(){
	var sps = document.getElementsByClassName("sp_style");
	for(var i=0;i<sps.length;i++)
	{
		if(sps[i].getAttribute("name") == "1"){
			sps[i].removeAttribute("style");
		}
	}
}

function startipt(obj){
	// console.log(obj);
	alert("igie");
	obj.removeAttribute("onclick")
	obj.innerHTML = '<input type="text" maxlength="10" size="10"></input>';
	// console.log(obj);
}

function update_status(){
	var _update = document.getElementById("update");
	_update.innerHTML = "<img src='static/img/loading_1.gif' style='width:80px;height:60px;'></img>";
	var xmlhttp;
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}
	else
	{// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	// _update.innerHTML = xmlhttp.responseText;
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			_update.innerHTML= '<p style="color:red;">' + xmlhttp.responseText + '</p>';
			var update = "javascript:location.href='/'"
    		setTimeout(update,1000);
		}
	}
	xmlhttp.open("GET","/update_state",true);
	xmlhttp.send();
}