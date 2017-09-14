(function($){
	$(window).on("load",function(){

		var delModal = $('#deleteModal'),
			editModal = $('#editModal'),
			table = $('.table');

		table.off('click');
		/* 点击事件绑定 */
		table.on('click','.j-edit',function(){
			editModal.modal('show');
		})
		.on('click','.j-del',function(){
			delModal.modal('show');
		});

		$('.j-add').on('click',function(){
			editModal.modal('show');
		});

	});
})(jQuery);

/*
*全选
*/
function selectBox() {
	var objs = document.getElementsByName("id");
	if (document.getElementById("J_selectAllCheckBox").checked == true) {	
		for ( var i = 0; i < objs.length; i++) {
			objs[i].checked = true;
		}	
	} else {
		for ( var i = 0; i < objs.length; i++) {
			objs[i].checked = false;
		}
	}
}
	