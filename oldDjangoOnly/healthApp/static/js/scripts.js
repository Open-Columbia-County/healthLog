var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "flex") {
        content.style.display = "none";
    } else {
        content.style.display = "flex";
        content.style.flexDirection = 'column';
    }
    });
}

function menu() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "flex") {
        x.style.display = "none";
    } else {
        x.style.display = "flex";
        x.style.flexDirection = 'column';
    }
}
function auth() {
    var l = document.getElementById('login')
    var r = document.getElementById('reg')
    var t = document.getElementById('text')
    if (r.style.display === 'flex') {
        r.style.display = 'none'
        l.style.display = 'flex'
        l.style.flexDirection = 'column';
        t.innerHTML = 'Register'
    } else {
        l.style.display = 'none'
        r.style.display = 'flex'
        r.style.flexDirection = 'column';
        t.innerHTML = 'Login'
    }
}

function copyInfo() {
    var copyText = document.querySelector('#drInfo')
    console.log("the copied text:", copyText)
    copyText.select()
    copyText.setSelectionRange(0, 999999)
    navigator.clipboard.writeText(copyText.value)
    alert("You have copied the text to your clipboard:", copyText.value)
}


$(document).ready(function(){
    $('#showMoods').click(function(){
        $('#hideMoods').animate( {
            width: 'toggle'
        })
    })
    $('#showMeds').click(function() {
        $('#hideMeds').animate( {
            width: 'toggle'
        })
    })
    $('#showSugars').click(function(){
        $('#hideSugars').animate( {
            width: 'toggle'
        })
    })
    $('#showWeeks').click(function(){
        $('#hideWeeks').animate( {
            width: 'toggle'
        })
    })
    $('#showLogs').click(function(){
        $('#hideLogs').animate( {
            width: 'toggle'
        })
    })
    $('#showAllMoods').click(function(){
        $('#hideAllMoods').animate( {
            width: 'toggle'
        })
    })
    $('#showAllTaken').click(function(){
        $('#hideAllTaken').animate( {
            width: 'toggle'
        })
    })
    $('#showAllSugars').click(function(){
        $('#hideAllSugars').animate( {
            width: 'toggle'
        })
    })
    $('#showDrForm').click(function(){
        $('#hideDrForm').animate( {
            width: 'toggle'
        })
    })
})

// var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
// (function(){
// var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
// s1.async=true;
// s1.src='https://embed.tawk.to/633ccb1654f06e12d898766e/1geioe0ce';
// s1.charset='UTF-8';
// s1.setAttribute('crossorigin','*');
// s0.parentNode.insertBefore(s1,s0);
// })();
