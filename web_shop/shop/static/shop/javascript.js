function reviews() {
  var x = document.getElementById("reviews_div");
  var y = document.getElementById("write_review_div");

  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  }
  else {
    x.style.display = "none";
  }
}

function writeReview() {
  var x = document.getElementById("write_review_div");
  var y = document.getElementById("reviews_div");

  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  }
  else {
    x.style.display = "none";
  }
}

function show_alert() {
  $("#alert_container").delay(3000).fadeOut(2000);
}
