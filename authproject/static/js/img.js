var x;
b=document.querySelector('button');
function bansal(){
$.getJSON("https://api.thingspeak.com/channels/581726/fields/1/last.json?results=2",function(data){
	x=data['field1']
	console.log(x);
	if(x==='0')
	{
		b.textContent="Start";
	}
	else{
		b.textContent="Stop";
	}
});
}
setInterval(bansal,500);