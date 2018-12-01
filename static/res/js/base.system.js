var sc = {
	ajaxreturn:function(URL,data){
		URL = URL==''?document.URL:URL;
		layer.load(0,{shade: [0.2,'#000']});
		$.post(URL, data, function(re){
			layer.closeAll();
			if(re.code == 1){
				layer.alert(re.msg, function(){
					window.location.reload();
				});
			}else{
				layer.alert(re.msg);
			}
		});
	},
	opentab:function(link,w,h,r){
		w = w == ''?'98%':w;
		h = h == ''?'98%':h;
		layer.open({
			type: 2,
			title: false,
			area: [w, h],
			content: link,
			cancel: function(){
				if(r)
					window.location.reload();
			}
		});
	},
	pageurl:function(url,arg,arg_val) {
		url = url == ''?document.URL:url;
	    var pattern		= arg+'=([^&]*)';
	    var replaceText	=arg+'='+arg_val;
	    var newurl		='';
	    if(url.match(pattern)){
	        var tmp 	= '/('+ arg+'=)([^&]*)/gi';
	        newurl		= url.replace(eval(tmp),replaceText);
	    }else{
	        if(url.match('[\?]')){
	            newurl	= url+'&'+replaceText;
	        }else{ 
	            newurl	= url+'?'+replaceText;
	        }
	    }
	    window.location	= newurl;
	}
};