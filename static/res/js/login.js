logincheck = function(){
	var d = {
		'username':$('#username').val(),
		'password':$('#password').val(),
		'verify':$('#verify').val()
	};
	if(d.username == ''){
		layer.alert('请输入用户编号');
		return false;
	}
	if(d.password == ''){
		layer.alert('请输入登录密码');
		return false;
	}
	if(d.verify == ''){
		layer.alert('请输入验证码');
		return false;
	}
	$.post(document.URL,d,function(re){
		if(re.code == 1){
			window.location = re.msg;
		}else{
			layer.alert(re.msg);
			refreshImage();
		}
	});
	return false;
}
refreshImage = function(){
	$("#yzm")[0].src = $("#yzm").attr("src") + '?' + Math.random();
}
