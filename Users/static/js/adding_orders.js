// function func_for_options(opt) {
//     // информация о том, какая из кнопок выбрана, передается как входной аргумент
//
//     // отключаем все что включено
//     let elems = document.getElementsByName('form_')
//     for (let i = 0; i < elems.length; i++) {
//         elems[i].style.display = 'none'
//         elems[i].setAttribute("disabled", "disabled");
//     }
//
//     // включаем необходимое
//     let form
//     if (opt == 1){
//         form = document.getElementById(`form_to_add_manually`)
//     }
//     else {
//         form = document.getElementById(`form_to_add_excel_file`)
//     }
//
//     form.style.display = 'block'
//     form.removeAttribute('disabled')
// }

function toTranslit(text) {
    return text.replace(/([а-яё])|([\s_-])|([^a-z\d])/gi,
        function (all, ch, space, words, i) {
            if (space || words) {
                return space ? ' ' : '';
            }
            var code = ch.charCodeAt(0),
                index = code == 1025 || code == 1105 ? 0 :
                    code > 1071 ? code - 1071 : code - 1039,
                t = ['yo', 'a', 'b', 'v', 'g', 'd', 'e', 'zh',
                    'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
                    'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
                    'shch', '', 'y', '', 'e', 'yu', 'ya'
                ];
            return t[index];
        });
}

function os_name_auto_fill(obj) {
    // получение ФИО из поля ввода
    let word = obj.value.split(' ')
    let id = obj.parentElement.parentElement.id

    // генерация логина для tc
    let new_word_tc = ''
    new_word_tc += toTranslit(word[1].charAt(0))
    new_word_tc += toTranslit(word[0])
    let field = document.getElementsByName(`form-${id}-tc_name`)
    document.getElementsByName(`form-${id}-tc_name`)[0].value = new_word_tc // 'tc_name'
    // генерация пароля для tc
    new_word_tc += Math.floor(Math.random() * 999)
    document.getElementsByName(`form-${id}-tc_pass`)[0].value = new_word_tc // 'tc_pass'

    // генерация логина для ОС
    // let new_word_os = ''
    // new_word_os += toTranslit(word[0].charAt(0)).toUpperCase()
    // new_word_os += toTranslit(word[0].substring(1))
    // new_word_os += toTranslit(word[1].charAt(0)).toUpperCase()
    // new_word_os += toTranslit(word[2].charAt(0)).toUpperCase()
    // document.getElementById('os_name').value = new_word_os
}

// добавление новой доп строки в таблицу
function add_line_func() {
    let table = document.getElementsByName('table_line');
    let last_line = table[table.length - 1];

    let new_table_line = `<tr name="table_line" id="${Number(last_line.id) + 1}">
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-req_num" class="form-control" id="request_number" autocomplete="off">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-full_name" class="form-control" id="full_name" onchange="os_name_auto_fill(this)" autocomplete="off">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-os_name" class="form-control" id="os_name" autocomplete="off">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-tc_name" class="form-control" id="tc_name" placeholder="авт." autocomplete="off">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-tc_pass" class="form-control" id="tc_pass" autocomplete="off" placeholder="авт.">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-group" class="form-control" id="group" autocomplete="off">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-role" class="form-control" id="role" autocomplete="off">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-lic_server" class="form-control" id="lic_server" autocomplete="off" placeholder="начните ввод..." list="lic_list">
                            </td>
                            <td>
                                <input type="text" name="form-${Number(last_line.id) + 1}-site" class="form-control" id="site" autocomplete="off" placeholder="начните ввод..." list="site_list">
                            </td>
                        </tr>
                        `

    last_line.insertAdjacentHTML("afterend", new_table_line);
}
