console.log("hello")
window.trainnumber=()=>{
    console.log("shyd chl jaye")
    const train_number = document.getElementById('train-number')
    const train_timing = document.getElementById('train-timing')
    if(train_number.style.visibility === 'hidden'){
        train_number.style.visibility = 'visible'
        train_timing.style.visibility='hidden'
    }
}
window.traintiming=()=>{
    console.log("shyd chl jaye")
    const train_timing = document.getElementById('train-timing');
    const train_number = document.getElementById('train-number')
    console.log(train_number.style.visibility)
    if(train_timing.style.visibility !== 'hidden'){
        train_timing.style.visibility='hidden'
        train_number.style.visibility = 'visible'

    }else{
        train_timing.style.visibility = 'visible'
        train_number.style.visibility = 'hidden'

    }
}
