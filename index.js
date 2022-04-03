var gpa = 0; //gpa inital value

c = {   // c json variable is used to store the subject credit and grade scored by the user
        "ec1":[3,0],
        "dsd":[3,0],
        "ss":[4,0],
        "maths":[4,0],
        "emf":[4,0],
        "oops":[3,0],
        "adclab":[1.5,0],
        "oopslab":[1.5,0]
    };

g = {"O":10,"A+":9,"A":8,"B+":7,"B":6}; // g json varibale is to map the grade scored in Alphabet to numerical

// Theme changing
function toggle_theme(){
    document.getElementsByTagName("body")[0].classList.toggle("bg-secondary");
    document.getElementsByTagName("body")[0].classList.toggle("bg-dark");
    document.getElementById("toggle_mode").classList.toggle("btn-dark");
    document.getElementById("toggle_mode").classList.toggle("btn-secondary");
}

// Listens to changes in options, Calculates GPA value and updates accordingly
function eventlis_grade(e){
    var grade = e.target.value;
    var sub = e.target.name;
    if(grade==="RA or A"){
        alert("Sorry, you have Failed!");
    }
    else if(grade==="--Select an option--"){
        alert("Select a valid option!");
    }
    else{
        grade = g[grade];
        gpa-=((c[sub][1]*c[sub][0])/24);
        c[sub][1] = grade;
        gpa+=((c[sub][1]*c[sub][0])/24);
        document.getElementById("result-box").innerHTML = Math.round(gpa*1000)/1000;
    }
}


// Calling the Theme toggle function when click on Toggle theme button
document.getElementById("toggle_mode").addEventListener("click", toggle_theme);

// Adding event listener to options
var a = document.getElementsByClassName("sele");
for(let i=0;i<a.length;i++){
    a[i].addEventListener("change",eventlis_grade);
}