const openFormBtn = document.getElementById('openFormBtn');
const popup = document.getElementById('popup');
const closePopup = document.getElementById('closePopup');

openFormBtn.addEventListener('click', () => {
  if (popup.style.display === 'none' || popup.style.display === '') {
    popup.style.display = 'block';
  } else {
    popup.style.display = 'none';
  }
});

closePopup.addEventListener('click', () => {
  popup.style.display = 'none';
});
