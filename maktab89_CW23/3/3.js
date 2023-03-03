btn = document.getElementById('btn');
card = document.getElementById('card');
btn.addEventListener('click', function() {
    card.classList.remove('d-none');
    btn.classList.add('d-none');
})