function start_project() {
	var form = $("#startProjectForm");
	var data = form.serialize();

	$.ajax({
		url: '/start_project',
		type: 'POST',
		data: {
		      'json': data,
		     },
		dataType: 'json',
		success: function(data, textStatus, xhr) {
			console.log(data);
			messagePnotify('Success', 'Thank you for you interest. You have started a project with PPPYO. We will get back to you shortly.', 'success');
			$("#close_modal_btn").click();
		},
	});
}

function messagePnotify(title, text, type){
	var myStack = {"dir1":"down", "dir2":"right", "push":"top"};
			new PNotify({
				title: title,
				text: text,
				type: type,
				closer: true,
				delay: 20000,
				mouse_reset: false, 
				addclass: "stack-custom",
				stack: myStack
			});
		}