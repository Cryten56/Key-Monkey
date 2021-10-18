





/*
const quoteDisplayElement = document.getElementById("quoteDisplay");
const quoteInputElement = document.getElementById("quoteInput");


quoteInputElement.addEventListener("input", () => {
  const arrayQuote = quoteDisplayElement.querySelectorAll("span");
  const arrayValue = quoteInputElement.value.split("");
  let correct = true
  arrayQuote.forEach((characterSpan, index) => {
    const character = arrayValue[index]
    if (character == null) {
        characterSpan.classList.remove('incorrect')
        characterSpan.classList.remove('corect')
        correct = false
    }
    else if (character === characterSpan.innerText) {
        characterSpan.classList.add('correct')
        characterSpan.classList.remove('incorrect')
    } else {
        characterSpan.classList.remove('coreect')
        characterSpan.classList.add('incorrect')
        correct = false
    }

  })
  
});


function renderSentence(quote) {
  quoteDisplayElement.innerText = null;
  quote.split("").forEach((character) => {
    const characterSpan = document.createElement("span");
    characterSpan.innerText = character;
    quoteDisplayElement.appendChild(characterSpan);
  });
  quoteInputElement.value = null;
} */
