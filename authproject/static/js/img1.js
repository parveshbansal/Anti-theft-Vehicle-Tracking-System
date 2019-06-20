var x;
b=document.querySelector('button');
function bansal(){
$.getJSON("https://api.thingspeak.com/channels/581726/fields/1/last.json?results=2",function(data){
	x=data['field1']
	console.log(x);
	if(x==='0')
	{
		b.textContent="OFF";
	}
	else{
		b.textContent="ON";
	}
});
}
setInterval(bansal,500);