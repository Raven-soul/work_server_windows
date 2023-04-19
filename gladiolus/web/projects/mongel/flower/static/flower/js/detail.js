function collapsElement(elem)
	{
        id = elem.getAttribute('aria-controls');
        
		if (elem.getAttribute('aria-expanded') == 'true'){
            document.getElementById(id).style.display = 'none';
            elem.setAttribute('aria-expanded', false);
        } else {
            document.getElementById(id).style.display = '';
            elem.setAttribute('aria-expanded', true);
        }
	}