
window.onload=function(){

    const ele=document.getElementById("chat")
    box=document.getElementById("box")
    ele.addEventListener("click", function() {
        usermessage=document.getElementById("usermessage")
        returnelement= `<div class="item right">
                <div class="msg">
                    <p>${usermessage.value}</p>
                </div>
            </div>`
       
    box.innerHTML+=returnelement
    console.log(box.lastChild.children[0].children[0].innerHTML)
    box.innerHTML+=`<br clear="both">`
    var objDiv = document.getElementById("box");
    objDiv.scrollTop = objDiv.scrollHeight;
    const usermessagejson={"user":usermessage.value}
    usermessage.value=''
    loader=`
    <div class="my message" id="loader">
         <span class="jumping-dots">
         <span class="dot-1"></span>
         <span class="dot-2"></span>
         <span class="dot-3"></span>
         </span>
         </div>
        </div>`
   box.innerHTML+=loader
   objDiv.scrollTop = objDiv.scrollHeight;
    
    const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json' 
        },
        body: JSON.stringify(usermessagejson) 
      };
     fetch('/send',options).then( response=> {
   
    response.json().then(result => {
      
     response_element=`<div class="item">
     <div class="icon">
         <i class="fa fa-user"></i>
     </div>
     <div class="msg">
         <p>${result.reply}</p>
     </div>
     </div>`
     loader_ele=document.getElementById("loader")
     loader_ele.remove()
     box.innerHTML+=response_element
     box.innerHTML+=`<br clear="both">`
     objDiv.scrollTop = objDiv.scrollHeight;

     })
    })
    

    });

  }

