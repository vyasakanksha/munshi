var fileInput = document.getElementById('file_input_file');
var fileInputText = document.getElementById('file_input_text');
var fd = new FormData();

// Shows the filename when a file is uploaded. The filesname
// comes from the python function
fileInput.addEventListener('change', showInputText);
function showInputText() {
	console.log("change")
	fileInputText.style.display = "block";
	fileInputText.style.marginLeft = "auto";
	fileInputText.style.marginRight = "auto";
	fileInputText.style.textAlign = "center";
}


$(document).ready(function(){
	$("#upload").click(function(){

      // Get uploaded file
      if($(fileInput).prop('files').length > 0)
      {
         file =$(fileInput).prop('files')[0];
         var new_file = new File([file], fileInputText.value + ".wav");
         fd.append("data", new_file);
         console.log(new_file);
      }

		$.ajax({
			type:'post',
			url:'/upload',
			async:'asynchronous',
			data: fd,
			dataType: "json",
			processData: false,
         contentType: false,
         beforeSend: function() { 
            $("#upload").prop('disabled', true); // disable button
            $(fileInput).prop('disabled', true); // disable button
         },
			success: function(response) {
			  console.log('success')
           window.location.reload();
			},
			error: function(error) {
			  console.log(error)
			}
		});
	});
});
