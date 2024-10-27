"use strict";

const quizData = [
    {
        question: "  Which gas is needed for photosynthesis?",
        a: " Oxygen",
        b: " Carbon Dioxide",
        c: "Hydrogen",
        d: "Carbon monoxide",
        correct: "b",
    },
    {
        question: "What type of energy is required for photosynthesis to happen?",
        a: "Light",
        b: "Heat",
        c: "Electrical",
        d: "Sand",
        correct: "a",
    },
    {
        question: "What is the chemical symbol for water?",
        a: "HO",
        b: "H2O",
        c: "O2H",
        d: "OH2",
        correct: "b",
    },
    {
        question: "Which planet is known as the Red Planet?",
        a: "Earth",
        b: "Mars",
        c: "Jupiter",
        d: "Venus",
        correct: "b",
    },
    {
        question: "What is the value of π (pi) up to two decimal places?",
        a: "3.12",
        b: "3.14",
        c: "3.33",
        d: "3.18",
        correct: "b",
    },
    
    {
        question: "Who was the first President of the United States? ",
        a: "Thomas Jefferson",
        b: "Abraham Lincoln",
        c: "George Washington",
        d: "John Adams",
        correct: "c",
    } ,
    {
        question: "What is the sum of the angles in a triangle? ",
        a: "90 degrees",
        b: "180 degrees",
        c: "270 degrees",
        d: "360 degrees",
        correct: "b",
    } ,
    {
        question: "What is the capital of Australia? ",
        a: " Sydney",
        b: "Melbourne",
        c: "Canberra",
        d: "Brisbane",
        correct: "c",
    } ,
    {
        question: "In which year did World War II end? ",
        a: "1942",
        b: "1944",
        c: "1945",
        d: "1946",
        correct: "c",
    } ,
    {
        question: "Which is the largest ocean on Earth? ",
        a: "Atlantic Ocean",
        b: "Indian Ocean",
        c: "Arctic Ocean",
        d: "Pacific Ocean",
        correct: "d",
    } 
];

const quiz = document.querySelector(".quiz-body");
const answerEl = document.querySelectorAll(".answer");
const questionEl = document.getElementById("question");
const footerEl = document.querySelector(".quiz-footer");
const quizDetailEl = document.querySelector(".quiz-details");
const liEl = document.querySelector("ul li");

const a_txt = document.getElementById("a_text");
const b_txt = document.getElementById("b_text");
const c_txt = document.getElementById("c_text");
const d_txt = document.getElementById("d_text");
const btnSubmit = document.getElementById("btn");

let currentQuiz = 0;
let score = 0;

loadQuiz();

function loadQuiz() {
 deselectAnswers();
 const currentQuizData = quizData[currentQuiz];
 questionEl.innerText = currentQuizData.question;
 a_txt.innerText = currentQuizData.a;
 b_txt.innerText = currentQuizData.b;
 c_txt.innerText = currentQuizData.c;
 d_txt.innerText = currentQuizData.d;
 quizDetailEl.innerHTML = `<p>${currentQuiz + 1} of ${quizData.length}</p>`;
}

// deselect
function deselectAnswers() {
 answerEl.forEach((answerEl) => {
  answerEl.checked = false;
 });
}

// get selected
function getSelected() {
 let answer;
 answerEl.forEach((answerEls) => {
  if (answerEls.checked) {
   answer = answerEls.id;
  }
 });
 return answer;
}

btnSubmit.addEventListener("click", function () {
 const answers = getSelected();

 if (answers) {
  if (answers === quizData[currentQuiz].correct) {
   score++;
  }
  nextQuestion();
 }
});

// next Slide
function nextQuestion() {
 currentQuiz++;

 if (currentQuiz < quizData.length) {
  loadQuiz();
 } else {
  quiz.innerHTML = `<h2>You answered ${score}/${quizData.length} question correctly</h2>
  <h2> Marks = ${score*4} </h2>
    <button type="button" onclick="location.reload()">Reload</button>
    `;
  footerEl.style.display = "none";
 }
}