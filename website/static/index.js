const sentenceDisplayElement = document.getElementById("quoteDisplay");


function renderSentence(jsonQuote) { 
  //Gets the list of words and creates span objects of each letter, each of 
  //which are encapsulated in a div
  const wordsArr = JSON.parse(jsonQuote); //converts 
  sentenceDisplayElement.innerText = null;
  let charNum = 0;
  let wordCharNum = 0
  let wordNum = 0
  wordsArr.forEach((word, i) => {
    wordCharNum = 0
    const wordDiv = document.createElement("div");
    wordDiv.classList.add("d-inline")
    wordDiv.classList.add("mx-1")
    wordDiv.classList.add("word")
    sentenceDisplayElement.appendChild(wordDiv);
    wordDiv.setAttribute("data-word-num", wordNum);
    wordNum++
    word.split("").forEach((character, j) => {
      const charSpan = document.createElement('span');
      charSpan.setAttribute("word-char-num", wordCharNum);
      charSpan.setAttribute("data-char-num", charNum);
      charSpan.innerText = character;
      wordDiv.appendChild(charSpan);
      ++charNum;
      ++wordCharNum;
    });
})}

function whichWord (charnum) {
  try {
    whichWord = currentSpan.parentElement.getAttribute("data-word-num")
    return 
  } catch (e) {}
}

// document.addEventListener("DOMContentLoaded", () => {
//   const words = `{{ sentence|safe }}`
//   console.log(words)
//   renderSentence(words)
//   wordsArr = JSON.parse(words);
//   // console.log(wordsArr)   
//   wordsDict = wordsArr.map(x => ({word: x, wordSpeed: null, letters: new Array(x.length)}))
//   console.log(wordsDict)

//   let backspaceFlag = false
//   let charnum = 0
//   let nextKeystrokeTime
//   let keystrokeTime
//   window.addEventListener('keydown', (event) => {
//     console.log(wordsDict)
//     const charCode = event.key.charCodeAt();
//     if (event.key.length === 1 && (charCode >= 65 && charCode  <= 90) || (charCode >= 97 && charCode <= 122)) {     
//       let currentSpan = document.querySelector(`span[data-char-num="${charnum}"]`) 
//       if ((charnum !== 0) || (backspaceFlag === true)) {
//         backspaceFlag = false
//         nextKeystrokeTime = new Date().getTime()
//         keystrokeTimeDifference = nextKeystrokeTime - keystrokeTime 
//         console.log(keystrokeTimeDifference)
//         keystrokeTime = nextKeystrokeTime
//         wordsDict[currentSpan.getAttribute("data-word-num")].letters[currentSpan.getAttribute("word-char-num")]
//       } else {
//         keystrokeTime = new Date().getTime()
//       } 
      
//       let currentCharinSpan = currentSpan.innerText
//       charnum = charnum+1 
//       console.log(charnum)
//       if (event.key === currentCharinSpan) {
//       currentSpan.classList.add("correct")
//       currentSpan.classList.remove("incorrect")
//       } else if (event.key !== currentCharinSpan) {
//       currentSpan.classList.add("incorrect")
//       currentSpan.classList.remove("correct")} 
//     } 
    
//     if (event.key==="Backspace") {  
//       backspaceFlag = true
//       if (charnum > 0) {
//         charnum = charnum-1
//       }   
//       console.log(charnum)
//       let currentSpan = document.querySelector(`span[data-char-num="${charnum}"]`);
//       currentSpan.classList.remove("correct");
//       currentSpan.classList.remove("incorrect");
//     } else if (event.key==="Backspace" && event.ctrlKey === True){}
//     })
// })