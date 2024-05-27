document.addEventListener("DOMContentLoaded", function() {
    // Get the uploaded image element
    var uploadedImage = document.getElementById("uploaded-image");

    // Get the prediction element
    var prediction = document.getElementById("prediction");

    // Update the uploaded image source and prediction text based on the uploaded image
    uploadedImage.onload = function() {
        prediction.textContent = "Predicted Caption: " + this.dataset.prediction;
    };
});
