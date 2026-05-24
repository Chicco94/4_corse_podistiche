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
	const sortSelect = document.getElementById('race-sort');
	if(!input) return;

	const items = Array.from(document.querySelectorAll('.race-item'));
	const raceList = document.querySelector('.race-list');

	function getItemData(item){
		return {
			element: item,
			name: item.querySelector('.race-name')?.textContent || '',
			place: item.querySelector('.race-place')?.textContent || '',
			meta: item.querySelector('.race-meta')?.textContent || '',
			rating: parseFloat(item.querySelector('.race-average')?.textContent.split(' ')[1] || 0),
			reviews: parseInt(item.querySelector('.race-count')?.textContent.match(/\d+/) || 0),
			dateStr: item.querySelector('.race-meta')?.textContent.match(/\d{2}\/\d{2}\/\d{4}/)?.[0] || ''
		};
	}

	function parseDate(dateStr){
		const [d, m, y] = dateStr.split('/');
		return new Date(y, m-1, d);
	}

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
		sort();
	}

	function sort(){
		const sortValue = sortSelect?.value || 'name-asc';
		const visibleItems = items.filter(item => item.style.display !== 'none');
		const itemsData = visibleItems.map(getItemData);

		itemsData.sort((a, b) => {
			switch(sortValue){
				case 'name-asc':
					return a.name.localeCompare(b.name);
				case 'name-desc':
					return b.name.localeCompare(a.name);
				case 'rating-desc':
					return b.rating - a.rating;
				case 'rating-asc':
					return a.rating - b.rating;
				case 'date-desc':
					return parseDate(b.dateStr) - parseDate(a.dateStr);
				case 'date-asc':
					return parseDate(a.dateStr) - parseDate(b.dateStr);
				case 'reviews-desc':
					return b.reviews - a.reviews;
				default:
					return 0;
			}
		});

		itemsData.forEach(data => {
			raceList.appendChild(data.element);
		});
	}

	input.addEventListener('input', debounce(filter, 150));
	if(sortSelect) sortSelect.addEventListener('change', sort);
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

// Toggle info tooltips
;(function(){
	document.addEventListener('click', function(e){
		const icon = e.target;
		if(icon && icon.classList && icon.classList.contains('info-icon')){
			const tooltipId = icon.getAttribute('data-info');
			if(!tooltipId) return;
			const tooltip = document.getElementById(tooltipId);
			if(!tooltip) return;
			const isHidden = tooltip.hasAttribute('hidden');
			if(isHidden){
				tooltip.removeAttribute('hidden');
			} else {
				tooltip.setAttribute('hidden','');
			}
		}
	});
})();

// Toggle user menu dropdown
;(function(){
	const userMenuButton = document.querySelector('.user-menu-button');
	const userMenu = document.getElementById('user-menu-dropdown');
	if(!userMenuButton || !userMenu) return;

	userMenuButton.addEventListener('click', function(e){
		e.preventDefault();
		const isExpanded = userMenuButton.getAttribute('aria-expanded') === 'true';
		if(isExpanded){
			userMenu.setAttribute('hidden', '');
			userMenuButton.setAttribute('aria-expanded', 'false');
		} else {
			userMenu.removeAttribute('hidden');
			userMenuButton.setAttribute('aria-expanded', 'true');
		}
	});

	document.addEventListener('click', function(e){
		if(userMenu.contains(e.target) || userMenuButton.contains(e.target)) return;
		userMenu.setAttribute('hidden', '');
		userMenuButton.setAttribute('aria-expanded', 'false');
	});
})();
