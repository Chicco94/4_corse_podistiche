// Script principale dell'applicazione
console.log('App caricata correttamente');

// Client-side filter per la lista delle gare
;(function(){
	function debounce(fn, wait){
		let t;
		return function(){
			clearTimeout(t);
			const args = arguments;
			t = setTimeout(()=> fn.apply(this, args), wait);
		}
	}

	function normalize(s){
		return (s||'').toLowerCase().trim();
	}

	const input = document.getElementById('race-filter');
	if(!input) return;

	const items = Array.from(document.querySelectorAll('.race-item'));

	function filter(){
		const q = normalize(input.value);
		items.forEach(item=>{
			if(!q){
				item.style.display = '';
				return;
			}
			const name = normalize(item.querySelector('.race-name')?.textContent);
			const place = normalize(item.querySelector('.race-place')?.textContent);
			const meta = normalize(item.querySelector('.race-meta')?.textContent);

			const matches = name.includes(q) || place.includes(q) || meta.includes(q);
			item.style.display = matches ? '' : 'none';
		});
	}

	input.addEventListener('input', debounce(filter, 150));
})();

// Toggle review details (collapsible)
;(function(){
	function toggleDetails(e){
		const btn = e.target
		const card = btn.closest('.review-card');
		if(!card) return;
		const details = card.querySelector('.review-details');
		if(!details) return;
		const isHidden = details.hasAttribute('hidden');
		if(isHidden){
			details.removeAttribute('hidden');
			btn.textContent = 'Nascondi dettagli';
			card.classList.add('open');
		} else {
			details.setAttribute('hidden','');
			btn.textContent = 'Mostra dettagli';
			card.classList.remove('open');
		}
	}

	document.addEventListener('click', function(e){
		const t = e.target;
		if(t && t.classList && t.classList.contains('toggle-details')){
			toggleDetails(e);
		}
	});
})();

// Toggle add review form
;(function(){
	document.addEventListener('click', function(e){
		const btn = e.target;
		if(btn && btn.classList && btn.classList.contains('toggle-add-review')){
			const addReviewDiv = btn.closest('.add-review');
			if(!addReviewDiv) return;
			const form = addReviewDiv.querySelector('.add-review-form');
			if(!form) return;
			const isHidden = form.hasAttribute('hidden');
			if(isHidden){
				form.removeAttribute('hidden');
				btn.textContent = 'Nascondi Recensione';
				addReviewDiv.classList.add('open');
			} else {
				form.setAttribute('hidden','');
				btn.textContent = 'Aggiungi una Recensione';
				addReviewDiv.classList.remove('open');
			}
		}
	});
})();
