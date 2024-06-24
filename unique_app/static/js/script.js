window.addEventListener('load', function() {
  var loaderContainer = document.querySelector('.container-loader');
  if (loaderContainer) {
      loaderContainer.style.display = 'none';
  }
});
  
  
  const heroSection = document.querySelector('.main-hero');
  const squaresPerRow = 20; // Примерное количество квадратов в ряду
  const numRows = 20; // Примерное количество рядов


  for (let i = 0; i < squaresPerRow * numRows; i++) {
    let square = document.createElement('div');
    square.classList.add('square');
    square.style.left = `${(i % squaresPerRow) * 110}px`; // Расстояние между квадратами 120px
    square.style.top = `${Math.floor(i / squaresPerRow) * 110}px`; // Расстояние между рядами 120px
    heroSection.appendChild(square);
  }

  // Анимация квадратов
  setInterval(() => {
    document.querySelectorAll('.square').forEach(square => {
      if (Math.random() < 0.1) { // 10% вероятность мигания для каждого квадрата
        square.style.backgroundColor = '#292929';
        setTimeout(() => {
          square.style.backgroundColor = '#222222';
        }, Math.random() * 2000); // Продолжительность мигания от 0 до 2 секунд
      }
    });
  }, 1000); // Периодичность проверки каждую секунду


  window.addEventListener('scroll', function() {
    var header = document.querySelector('.header');
    if (window.scrollY > 50) { // Например, при прокрутке больше чем на 50px
        header.style.backgroundColor = 'rgba(0, 0, 0, 0.8)'; // Делаем фон немного прозрачным
    } else {
        header.style.backgroundColor = '#1B1B1B;'; // Возвращаем прозрачность при скролле вверх
    }
});


document.addEventListener('DOMContentLoaded', function () {
    const toggleSwitch = document.querySelector('#switch');
    const body = document.body;

    // Функция для переключения темы
    function switchTheme(e) {
        if (e.target.checked) {
            body.classList.add('light-theme');
            body.classList.remove('dark-theme');
            localStorage.setItem('theme', 'light-theme'); // Сохраняем выбор темы в localStorage
        } else {
            body.classList.add('dark-theme');
            body.classList.remove('light-theme');
            localStorage.setItem('theme', 'dark-theme');
        }
    }

    // Слушатель событий на изменение чекбокса
    toggleSwitch.addEventListener('change', switchTheme, false);

    // Проверяем сохраненную тему в localStorage и обновляем интерфейс
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
    if (currentTheme) {
        body.classList.add(currentTheme);
        if (currentTheme === 'light-theme') {
            toggleSwitch.checked = true;
        }
    }
});


function filterTech(category) {
  const elements = document.querySelectorAll('.technology');
  elements.forEach(el => {
      if (category === 'all' || el.getAttribute('data-category') === category) {
          el.style.display = 'block';
      } else {
          el.style.display = 'none';
      }
  });
}


function nextStep(step) {
  for (let i = 1; i <= 4; i++) {
      document.getElementById('step' + i).classList.add('hidden');
  }
  document.getElementById('step' + step).classList.remove('hidden');
}

function calculateTotal() {
  let total = 0;
  total += parseInt(document.getElementById('type').value);
  total += parseInt(document.getElementById('design').value);

  if (document.getElementById('logo').checked) {
      total += parseInt(document.getElementById('logo').value);
  }

  if (document.getElementById('banner').checked) {
      total += parseInt(document.getElementById('banner').value);
  }

  if (document.getElementById('seo').checked) {
      total += parseInt(document.getElementById('seo').value);
  }

  if (document.getElementById('analytics').checked) {
      total += parseInt(document.getElementById('analytics').value);
  }

  if (document.getElementById('multilingual').checked) {
    total += parseInt(document.getElementById('multilingual').value);
  }

  if (document.getElementById('blog').checked) {
    total += parseInt(document.getElementById('blog').value);
  }

  document.getElementById('total').textContent = total;
}

function startCalculation() {
  window.location.href = '/services/calculator-web'; // Предполагается, что у вас есть страница калькулятора
}


const menuBtn = document.querySelector('.menu-btn');
const menu = document.querySelector('.menu');

menuBtn.addEventListener('click', () => {
    menu.classList.toggle('show');
});


