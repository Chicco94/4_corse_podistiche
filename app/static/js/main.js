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
