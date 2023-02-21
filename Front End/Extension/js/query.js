function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var details = document.getElementById("details").value;
    var subject = document.getElementById("subject").value;
    var emailRangeCheck =  /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

    if (name == "" ) {
        alert ("Please enter your Name");
        return false;
    }
 
    if (email == "" ) {
        alert ("Please enter your Email");
        return false;
    }
   

    if(!emailRangeCheck.test(email)){
      alert ("Please enter a valid Email");
      return false;
   }
  

    if (subject == "") {
        alert ("Please select a subject for your inquiry.");
        return false;
    }

    if(details == "" ) {
        alert ("Please enter a inquiry");
        return false;
    }


let btnclear = document.querySelector('button')

    
  }

