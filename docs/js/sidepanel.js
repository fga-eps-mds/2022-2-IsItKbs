function openNav(parent) {
    document.getElementById("mySidepanel").style.marginLeft = "0px";
  }
  
function openNav2() {
    document.getElementById("projetoSidepanel").style.marginLeft = "0px";
  }
function openNav3() {
    document.getElementById("equipeSidepanel").style.marginLeft = "0px";
  }
function closeNav(parent) {
     document.getElementById(parent.id).style.marginLeft = "-250px";
  }

  function makeid() {
    var result_1 = '';
    var result_2 = '';
    var result_3 = '';
    var characters       = 'abcedfghijklmnopqrstuv!?,.#@1234567890';
    var charactersLength = characters.length;
    for ( var i = 0; i < 4; i++ ) {
       result_1 += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    for ( var i = 0; i < 8; i++ ) {
      result_2 += characters.charAt(Math.floor(Math.random() * charactersLength));
   }
   for ( var i = 0; i < 9; i++ ) {
    result_3 += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    
    var h1 = document.getElementById('main-title');
    h1.innerHTML = "<h1>" + result_1 + "<\h1> <span>" + result_2 + " " + result_3 + "<\span>"
    setTimeout(function() {
      h1.innerHTML = "<h1>is it<\h1><span>keyboard smashing?<\span>"
    }, 2500)
 }

 window.onload(makeid())