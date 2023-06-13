//
// accountList.js
// development of an online flower shop
//
// Created by Artem Kozyrev on 20.04.2023.
//

function collapsElement(elem, main_id){
    main_elem = document.getElementById(main_id);

    area_id = main_elem.getAttribute('area-id');
    link_last_id_number =  elem.getAttribute('id').substr(elem.getAttribute('id').length - 4); //id нажимаемой строки
    
    id = area_id + link_last_id_number;
    
    if (elem.getAttribute('aria-expanded') == 'true'){
        document.getElementById(id).style.display = 'none';
        elem.setAttribute('aria-expanded', false);
    } else {
        document.getElementById(id).style.display = '';
        elem.setAttribute('aria-expanded', true);
    }

    collapsOtherElements(elem, main_elem);
}

function collapsOtherElements(elem, main_elem){
    link_id = main_elem.getAttribute('link-id');
    area_id = main_elem.getAttribute('area-id');

    max_number_rows = main_elem.getAttribute('max-elements'); //максимальное количество скрываемых строк
    this_id = Number(elem.getAttribute('id').substr(elem.getAttribute('id').length - 4)); //id нажимаемой строки

    for (let i = 0; i <= max_number_rows; i++) {

        if(i != this_id){
            link = document.getElementById(link_id + zero_val(i) + String(i));

            if(link.getAttribute('aria-expanded') == 'true'){
                document.getElementById(area_id + zero_val(i) + String(i)).style.display = 'none';
                link.setAttribute('aria-expanded', 'false');
            }
        }
    }
}

function zero_val(i){
    if (i<10){ return '000'; }
    else if (i<100) { return '00'; }
    else if (i<1000) { return '0'; }
    else { return '';}
}



