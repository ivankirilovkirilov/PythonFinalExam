$(document).ready(function (){
    $(':input[type=file]').change( function(event) {
	    var img_path = URL.createObjectURL(event.target.files[0]);
	    $("#image_preview").attr('src',img_path);
	    return;
	});
    var image_path = $("label[for='id_image']").next('a').attr('href');
    $("#image_preview").attr('src',image_path);
});