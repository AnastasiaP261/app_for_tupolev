function set_lic_list() {
    // получаем выбранное значение из списка сайтов
    let elem1 = document.getElementById('select_menu1')
    let select_site_value = elem1.options[elem1.selectedIndex].value

    /*
    заменяем список, создающийся сервером, на список, обрабатываемый js

    сервер создал выпадающие списки для каждого из выбранных сайтов(см html-шаблон), но все они кроме all изначально скрыты
    при выборе значения сайта мы прячем все списки, а потом показываем только нужный
    атрибут display отвечает за отображение на странице
    атрибут disabled блокирует элемент, чтобы данные из него не обрабатывались
    */
    let elems = document.getElementsByName('select_menu2')
    for (let i = 0; i < elems.length; i++) {
        elems[i].style.display = 'none'
        elems[i].setAttribute("disabled", "disabled");
    }
    let elem2 = document.getElementById(`select_menu2_for_${select_site_value}`)
    elem2.style.display = 'block'
    elem2.removeAttribute('disabled')
}



