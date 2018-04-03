var slider = document.getElementById("priceFilter");
var output = document.getElementById("priceLabel");
output.innerHTML = slider.value;

slider.onmouseup = function() {
  output.innerHTML = this.value;
}