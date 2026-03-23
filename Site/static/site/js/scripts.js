// Конечная дата
const deadline = new Date("2026-08-29T13:40:00").getTime();

function updateCountdown() {
  const now = new Date().getTime();
  const diff = deadline - now;

  if (diff < 0) {
    document.getElementById('countdown').innerHTML = "Свадьба началась!";
    clearInterval(timerInterval);
    return;
  }

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((diff % (1000 * 60)) / 1000);

  document.getElementById('countdown').innerHTML =
    `${days}д ${hours}ч ${minutes}м ${seconds}с`;
}

const timerInterval = setInterval(updateCountdown, 1000);
updateCountdown();