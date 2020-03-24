const url = "http://localhost:4000/"

$(document).ready(function () {
  bsCustomFileInput.init();
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('#inputImage').attr('src', e.target.result);
    };

    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#input").change(function() {
  $('#resultsDiv').html('');
  $('#inputImage').removeClass('hidden');
  $('#inputImageTitle').removeClass('hidden');
  readURL(this);
});

$('#submit').click(function () {
  $('#submit').attr('disabled', '');
  $('#resultsDiv').html(`
    <div class="spinner-border text-info" style="width: 6rem; height: 6rem;" role="status">
      <span class="sr-only">Loading...</span>
    </div>
  `);

  if ($('#input')[0].files.length) {
    var fd = new FormData();
    fd.append('image', document.getElementById('input').files[0]);

    $.ajax({
      type: "POST",
      url: url + 'detect',
      data: fd,
      success: function(data) {
        if (data) {
          var classes = data.results.classesDetected;
          var images = data.results.images;
          console.log(images);
          $('#resultsDiv').html('');
          for (var i = 0; i < images.length; i++) {
            $('#resultsDiv').append(`
                <div class="row p-4">
                 <div class="col-12" align="center">
                  <div class="card" style="width: 18rem;">
                    <img src="${images[i].imagePath}" class="card-img-top">
                      <div class="card-body">
                        <h5 class="card-title" style="text-transform: capitalize;">${images[i].class}</h5>
                        <hr>
                        <a download href="${images[i].imagePath}" class="btn btn-outline-info">Download</a>
                      </div>
                    </div>
                  </div>
                </div>
              `);
          }
        } else {
          $('#resultsDiv').html(`
              <h3>No classes found.</h3>
            `);
          $('#submit').removeAttr('disabled');
        }
        $('#submit').removeAttr('disabled');
        console.log(data);
      },
     error: function(error) {
       console.log(error);
       $('#resultsDiv').html(``);
       $('#submit').removeAttr('disabled');
       alert("There was some error. Please try again");
     },
     dataType: 'json',
     processData: false,
     contentType: false
    });

  } else {
    alert('Please choose an image');
    $('#resultsDiv').html(``);
    $('#submit').removeAttr('disabled');
  }
});


//
