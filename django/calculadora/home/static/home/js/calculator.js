const display = document.getElementById("display");
let current = "0";
let previous = "";
let op = null;
let reset = false;

document.querySelector(".buttons").onclick = (e) => {
  if (!e.target.matches(".btn")) return;
  handle(e.target.dataset.action);
};

document.onkeydown = (e) => {
  const k = e.key;
  if (/[0-9.+\-*/%]/.test(k)) handle(k);
  else if (k === "Enter") handle("=");
  else if (k === "Backspace") handle("delete");
  else if (k === "Escape") handle("clear");
};

function handle(a) {
  if (/[0-9]/.test(a)) {
    if (current === "0" || reset) {
      current = a;
    } else {
      current += a;
    }
    reset = false;
  } else if (a === "." && !current.includes(".")) {
    current += ".";
  } else if (a === "clear") {
    current = "0";
    previous = "";
    op = null;
  } else if (a === "delete") {
    if (current.length > 1) {
      current = current.slice(0, -1);
    } else {
      current = "0";
    }
  } else if (a === "%") {
    current = String(parseFloat(current) / 100);
  } else if (["+", "-", "*", "/"].includes(a)) {
    if (previous && op && !reset) current = calc();
    previous = current;
    op = a;
    reset = true;
  } else if (a === "=" && previous && op) {
    current = calc();
    previous = "";
    op = null;
    reset = true;
  }
  display.value = current;
}

function calc() {
  const p = parseFloat(previous);
  const c = parseFloat(current);
  if (op === "/" && c === 0) return "Error";

  let r;
  if (op === "+") {
    r = p + c;
  } else if (op === "-") {
    r = p - c;
  } else if (op === "*") {
    r = p * c;
  } else {
    r = p / c;
  }

  return String(Math.round(r * 1e9) / 1e9);
}
