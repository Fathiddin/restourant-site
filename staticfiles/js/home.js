let increment = document.querySelectorAll(".increment"),
 decrement = document.querySelectorAll(".decrement")
 increment.forEach(element => {
    element.addEventListener("click", ()=>{
        element.nextElementSibling.value = Number(element.nextElementSibling.value) + 1 
        })
    });

decrement.forEach(element => {
    element.addEventListener("click", ()=>{
        if(Number(element.previousElementSibling.value) > 1) {
            element.previousElementSibling.value = Number(element.previousElementSibling.value) - 1
        }
        })
    });