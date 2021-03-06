(function($) {
    $.fn.inputFilter = function(inputFilter) {
      return this.on("input keydown keyup mousedown mouseup select contextmenu drop", function() {
        if (inputFilter(this.value)) {
          this.oldValue = this.value;
          this.oldSelectionStart = this.selectionStart;
          this.oldSelectionEnd = this.selectionEnd;
        } else if (this.hasOwnProperty("oldValue")) {
          this.value = this.oldValue;
          this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
        } else {
          this.value = "";
        }
      });
    };
  }(jQuery));

$("#codeInput").inputFilter(function(value) {
    return /^-?\d*$/.test(value); 
});  

document.querySelector('.checker').addEventListener('submit', function(e) {
    e.preventDefault();
    var code = document.getElementById("codeInput").value;
    const check_key = Module.cwrap('__wasm_get_12vyatwd76', 'string', ["string"]);
    const treasure = check_key(code);
    if(treasure == "0"){
        return;
    }else{
        alert("Okay, okay...take your dogecoins: " + treasure);
    }    
});