function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

async function c() {
    let a = new Date().getTime();
    console.log(a)
    await sleep(2000)
    let b = new Date().getTime()
    console.log(b)
    console.log(a + " - " + b + " = " + (b-a))
}

c()