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

    // генерация логина для tc
    let new_word_tc = ''
    new_word_tc += toTranslit(word[1].charAt(0))
    new_word_tc += toTranslit(word[0])
    let line = document.getElementsByName(obj.name)
    line[3].value = new_word_tc // 'tc_name'
    // генерация пароля для tc
    new_word_tc += Math.floor(Math.random() * 999)
    line[4].value = new_word_tc // 'tc_pass'

    // генерация логина для ОС
    // let new_word_os = ''
    // new_word_os += toTranslit(word[0].charAt(0)).toUpperCase()
    // new_word_os += toTranslit(word[0].substring(1))
    // new_word_os += toTranslit(word[1].charAt(0)).toUpperCase()
    // new_word_os += toTranslit(word[2].charAt(0)).toUpperCase()
    // document.getElementById('os_name').value = new_word_os
    }


function add_line_func() {
    let table = document.getElementsByName('table_line');
    let last_line = table[table.length - 1];

    let new_table_line = `<tr id="${Number(last_line.id) + 1}" name="table_line">
                    <td>
                        <input type="text" class="form-control" id="request_number" name="hand_form${Number(last_line.id) + 1}" required>
                    </td>
                    <td>
                        <input type="text" class="form-control" id="full_name" name="hand_form${Number(last_line.id) + 1}"
                               onchange="os_name_auto_fill(this)">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="os_name" name="hand_form${Number(last_line.id) + 1}">
                    </td>
                    <td>
                        <input type="text" placeholder="автоматически" class="form-control"
                               id="tc_name" name="hand_form${Number(last_line.id) + 1}">
                    </td>
                    <td>
                        <input type="text" placeholder="автоматически" class="form-control"
                               id="tc_pass" name="hand_form${Number(last_line.id) + 1}">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="group" name="hand_form${Number(last_line.id) + 1}">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="role" name="hand_form${Number(last_line.id) + 1}">
                    </td>
                    <td>
                        <input type="text" class="form-control" id="lic_server" name="hand_form${Number(last_line.id) + 1}" list="lic_list"
                               placeholder="начните ввод...">
                        <datalist id="lic_list">
                            {% for name in lic_servers %}
                                <option value="{{ name }}"/>
                            {% endfor %}
                        </datalist>
                    </td>
                    <td>
                        <input type="text" class="form-control" id="site" name="hand_form${Number(last_line.id) + 1}" list="site_list"
                               placeholder="начните ввод...">
                        <datalist id="site_list">
                            {% for name in sites %}
                                <option value="{{ name }}"/>
                            {% endfor %}
                        </datalist>
                    </td>
                </tr>`

    last_line.insertAdjacentHTML("afterend", new_table_line);
}

