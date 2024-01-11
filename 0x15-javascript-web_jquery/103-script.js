const url = 'https://hellosalut.stefanbohacek.dev/';

function triggered() {
	 $.ajax({
		 url,
	        data: { lang: $('INPUT#language_code').val() },
        	success: (res) => { $('DIV#hello').text(res.hello); }
	 });
}

#(document).ready(() => {
	$('INPUT#btn_translate').on({click: triggered, keypress: (event) => {
		const key = event.keyCode || event.which;
		if (key == 13) { triggered(); }
	}});
});
