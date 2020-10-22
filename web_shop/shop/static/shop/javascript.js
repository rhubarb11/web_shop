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


function star_rating(avg_num) {
  var x = document.getElementById("filled_stars1");
  //var x = document.getElementById(string);
  if(avg_num <= 0) {
    x.style.width = '0%'
  }
  else {
    avg_num = (avg_num/5)*100;
    avg_num = avg_num.toString();
    avg_num = avg_num.concat('%');
    x.style.width = avg_num
  }
}
