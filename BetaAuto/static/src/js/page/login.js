$(function(){ 
	var errorMsg = '',
		errorTxt = $('#j-error');

	// 登录事件：默认用户名 admin，密码 123456
	$('.btn-login').on('click',function( event ){
		var username = $('input[name="username"]').eq(0).val(),
		password = $('input[name="password"]').eq(0).val();

		event.stopPropagation();

		if( validForm(username,password) ){ 
			errorTxt.text('');
			if(username == 'admin' && password == '123456'){
				location = "./index.html";
			}
			else{
				errorMsg = '用户名或密码错误';
				errorTxt.text(errorMsg);
			}
			
		}
		else{
			errorTxt.text(errorMsg);
		}
		
		return false;
	});

	// 验证表单是否为空
	function validForm(username,password) {  
	    if(  username == '' ||  password== ''){
	        errorMsg = '请输入用户名和密码';
	        return false;
	    }else{
	        return true;
	    }
	    
	}


});

	