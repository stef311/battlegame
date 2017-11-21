<script type="text/javascript">

    var montharray=new Array("January","February","March","April","May","June","July","August","September","October","November","December")
    var serverdate = new Date({% now "Y,n,j,G,i,s"%})
    function padlength(what){
	var output=(what.toString().length==1)? "0"+what : what
	return output
    }
    function displaytime(){
        serverdate.setSeconds(serverdate.getSeconds()+1)
        var datestring=montharray[serverdate.getMonth()]+" "+padlength(serverdate.getDate())+", "+serverdate.getFullYear()
        var timestring=padlength(serverdate.getHours())+":"+padlength(serverdate.getMinutes())+":"+padlength(serverdate.getSeconds())
        document.getElementById("tm").innerHTML=datestring+" "+timestring
    }
    window.onload=function(){
        displaytime()
        setInterval("displaytime()", 1000)
    }
</script> 
