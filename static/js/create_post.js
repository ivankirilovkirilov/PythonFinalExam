$(document).ready(function (){
    $(':input[type=file]').change( function(event) {
	    var img_path = URL.createObjectURL(event.target.files[0]);
	    $("#image_preview").attr('src',img_path);
});
})