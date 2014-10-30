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
		},
	});
}
