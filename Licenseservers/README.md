

|![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.001.png)|<p>**Министерство науки и высшего образования Российской Федерации Федеральное государственное бюджетное образовательное учреждение  высшего образования** </p><p>**«Московский государственный технический университет имени Н.Э. Баумана** </p><p>**(национальный исследовательский университет)»** </p><p>**(МГТУ им. Н.Э. Баумана)**</p>|
| - | :-: |
ФАКУЛЬТЕТ   *Робототехники и комплексной автоматизации ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.002.png)*КАФЕДРА  *Системы автоматизированного проектирования (РК-6)* 

**ОТЧЕТ ПО ПРОИЗВОДСТВЕННОЙ ПРАКТИКЕ** 

Студент 

Группа 

Тип практики Название предприятия 

Студент 

Руководитель практики  

  Петричук Анастасия Олеговна   РК6-61б 

`  `Производственная ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.003.png)![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.004.png)

`  `ПАО «Туполев» ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.005.png)![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.006.png)

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_    Петричук А.О.\_\_\_** 

`         `*подпись, дата                   фамилия, и.о.*             

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**  

`         `*подпись, дата                  фамилия, и.о.*             

Оценка  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 

*Москва, 2021 г.*

**Индивидуальное задание** 

Спроектировать и реализовать веб-приложение для существующей базы данных. Должен присутствовать следующий функционал:  

1) просмотр лицензий на всех сайтах с возможностью фильтрации данных по каждому отдельному сайту. 
1) просмотр  свободных  лицензий  с  возможностью фильтрации  по сайтам и по типу лицензий 
1) просмотр сводной таблицы пользователей 
1) обработка заявок на выдачу лицензий 

Детали реализации и информация баз данных приведена не будет, так как  данная  информация  принадлежит  ПАО  «Туполев»  и  является засекреченной. 

**Оглавление** 

[**Индивидуальное задание** ................................................................................. 3 ](#_page1_x70.00_y71.68)[**Оглавление** ......................................................................................................... 4 ](#_page2_x70.00_y71.68)[**Введение** .............................................................................................................. 5 ](#_page3_x70.00_y71.68)[**Основная часть** .................................................................................................. 6 ](#_page4_x70.00_y71.68)[**Обзор используемых в разработке средств** ........................................... 6 ](#_page4_x70.00_y104.68)[**Описание архитектуры проекта** .............................................................. 8 ](#_page5_x70.00_y482.68)[**Работа над приложением Licenseservers** .............................................. 10 ](#_page8_x70.00_y414.68)[**Работа над приложением Users** .............................................................. 13 ](#_page11_x70.00_y467.68)[**Заключение** ....................................................................................................... 21 ](#_page19_x70.00_y71.68)

**Введение** 

Производственная  практика  проходила  в  ПАО  «Туполев». Предприятие  занимается  разработкой,  производством,  испытаниями, ремонтом  и  поддержанием  лётной  годности  авиационной  техники.  В настоящее  время  ПАО  «Туполев»  является  предприятием,  способным обеспечивать  все  стадии  жизненного  цикла  авиационной  техники  от разработки  до  серийного  производства,  модернизации,  ремонта, послепродажного обслуживания и поддержки эксплуатации. Значительная часть  инженеров  компании  работает  на  ПО  компании  Siemens  NX Teamcenter.  Для  распределения  лицензий  на  ПО  между  сотрудниками используются базы данных, импортированные из Teamcenter с помощью скриптов.  Было  важно  обеспечить  удобную  и  быструю  работу  с полученными  данными.  Для  этого  решено  было  разработать  веб- приложение с бэкендом на Python, и фронтовой частью с использованием Bootstrap и JavaScript.  

В  результате  прохождения  практики  были  получены  новые  и закреплены уже имеющиеся знания в сфере веб-разработки. А также был получен опыт работы с языком JavaScript. 

**Основная часть** 

**Обзор используемых в разработке средств**  

Дадим некоторые определения: 

1) **Python** –[ высокоуровневый язык программирования ](https://ru.wikipedia.org/wiki/%D0%92%D1%8B%D1%81%D0%BE%D0%BA%D0%BE%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5%D0%B2%D1%8B%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)общего назначения с[ динамической](https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%82%D0%B8%D0%BF%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)[ строгой ](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D0%BE%D0%B3%D0%B0%D1%8F_%D1%82%D0%B8%D0%BF%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно- ориентированным — всё является объектами. 
1) **Django** -[ свободный](https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B5_%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)[ фреймворк ](https://ru.wikipedia.org/wiki/%D0%A4%D1%80%D0%B5%D0%B9%D0%BC%D0%B2%D0%BE%D1%80%D0%BA)для[ веб-приложений ](https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%B1-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5)на 

языке Python, использующий шаблон проектирования[ MV](https://ru.wikipedia.org/wiki/Model-View-Controller)[C\[8\].](https://ru.wikipedia.org/wiki/Django#cite_note-8) Проект поддерживается организацией Django Software Foundation. 

3) **MVC** - Model-View-Controller (MVC, «Модель-Представление- Контроллер», «Модель-Вид-Контроллер») — схема разделения данных приложения, и управляющей логики на три отдельных компонента: модель, представление и контроллер — таким образом, что модификация каждого компонента может осуществляться независимо. 
3) **Модель** (Model) предоставляет данные и реагирует на команды контроллера, изменяя своё состояние. 
3) **Представление** (View) отвечает за отображение данных модели пользователю, реагируя на изменения модели. 
3) **Контроллер** (Controller) интерпретирует действия пользователя, оповещая модель о необходимости изменений. 
3) **JavaScript**(также js) - мультипарадигменный[ язык программирования.](https://ru.wikipedia.org/wiki/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F) 

Поддерживает объекториентированный,[ императивный ](https://ru.wikipedia.org/wiki/%D0%98%D0%BC%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)и[ функци ональный ](https://ru.wikipedia.org/wiki/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)стили. Обычно используется как встраиваемый язык для программного доступа к объектам[ приложений.](https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%8F_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0) Наиболее широкое применение находит в[ браузерах ](https://ru.wikipedia.org/wiki/%D0%91%D1%80%D0%B0%D1%83%D0%B7%D0%B5%D1%80)как язык сценариев для придания[ интерактивности](https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D1%8C)[ веб-страницам.](https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%B1-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0) 

8) **SQL** -  [(англ. ](https://ru.wikipedia.org/wiki/%D0%90%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA)structured query language — «язык структурированных запросов») —[ декларативный](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BA%D0%BB%D0%B0%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)[ язык программирования,](https://ru.wikipedia.org/wiki/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F) применяемый для создания, модификации и управления данными в[ реляционной базе данных,](https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%BB%D1%8F%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5_%D0%B1%D0%B0%D0%B7%D1%8B_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85) управляемой соответствующей[ системой управления базами данных.](https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B1%D0%B0%D0%B7%D0%B0%D0%BC%D0%B8_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85) 
8) **MySQL** - [ свободная](https://ru.wikipedia.org/wiki/%D0%A1%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B5_%D0%9F%D0%9E)[ реляционная система управления базами данных.](https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%BB%D1%8F%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D0%A1%D0%A3%D0%91%D0%94) 
8) **БД** – база данных. 
8) **Модуль** — это один файл Python.  
8) **Пакет** — это каталог таких модулей. В отличие от простых директорий, содержащих скрипты Python, пакет содержит еще и дополнительный файл — \_init\_.py. 

**Описание архитектуры проекта** 

Разработка  приложения  велась  на  языке  Python.  Скрипты  в клиентской части приложения были написаны с использованием JavaScript. Верста осуществлялась с помощью CSS, HTML и Bootstrap. Запросы к базе данных были написаны на диалекте MySQL. 

При  создании  нового  проекта  с  использованием  Django, автоматически создается следующая структура проекта: 

TUPOLEV\_APP 

|    

|   manage.py 

|            +---tupolev\_app 

|   |   asgi.py 

|   |   settings.py |   |   urls.py 

|   |   views.py 

|   |   wsgi.py 

|   |   \_\_init\_\_.py |   |    

|   \---static 

|        \---templates 

*Структура проекта при создании приложения.* 

Корневая папка (в данном случае TUPOLEV\_APP), в которой находится главный  пакет  (tupolev\_app),  пустая  папка  templates,  в  которой  в дальнейшем  будут  создаваться  шаблоны  страниц,  и  модуль  manage.py, который является управляющим скриптом для всего проекта. Этот скрипт на  языке  Python  сгенерирован  фреймворком  Django  автоматически.  В пакете  tupolev\_app  находятся  файлы,  управляющие  проектом  в  целом: settings.py,  в  котором  объявлены  основные  переменные  для  настройки приложения, urls.py, который является главным контроллером и передает управление между контроллерами других приложений, а также папка static, в которую будут помещены статические файлы (например, css и js), общие для всего проекта. В данном случае база данных находилась на другой машине и подключение к ней осуществлялось по сети. 

После настройки главного пакета в корне приложения был создан пакет Licenseservers, имеющий следующую структуру: 

Licenseservers |   admin.py 

|   apps.py 

|   models.py |   tests.py 

|   urls.py 

|   views.py 

|   \_\_init\_\_.py | +---migrations | 

+---static 

| \---templates 

*Структура приложения Licenseservers.* 

- **models.py** – модель приложения. Здесь описываются классы, по которым после выполнения определенной команды создаются миграции. 
- **migrations**  –  внутрь  этой  папки  помещаются  автоматически созданные  миграции  –  скрипты,  которые  способны самостоятельно  записать  в  базу  данных  все  необходимые описанные  ранее  таблицы.  Этот  инструмент  позволяет разработчику минимизировать работу непосредственно с базой данных. 
- **app.py** – здесь описан класс приложения. 
- **urls.py** – контроллер приложения. 
- **admin.py**  –  классы  для  администрирования  сайта.  В  Django администрирование  максимально  автоматизировано,  его  не нужно  писать  с  нуля.  Это  позволяет,  опять-таки,  свести  к минимуму работу с БД.  
- папки  **templates**  и  **static**  –  аналогичны  тем,  что  хранятся  в главном пакете. 
- **views.py** – в этом модуле описаны отображения приложения. Каждому отображению передается управление из контроллера приложения  и  в  нем  ведется  работа  по  обработке  запроса пользователя. 

Аналогично был создан пакет Users. 

Users 

|   admin.py 

|   apps.py 

|   models.py |   tests.py 

|   urls.py 

|   views.py 

|   \_\_init\_\_.py | +---migrations | 

+---static 

| \---templates 

*Структура приложения Users.* 

**Работа над приложением Licenseservers** 

Сначала  будет  описана  работа  с  приложением  Licenseservers. Приложение  должно  обрабатывать  все  запросы,  связанные непосредственно с таблицами серверов лицензий и таблиц лицензий.  

В  модуле  views.py  был  описан  класс  ViewLicenses,  который обрабатывает запрос, связанный с просмотром лицензий на всех сайтах. Плюс, необходимо было реализовать фильтрацию данных по сайту.  

При передаче управления классу, соответствующий метод проверяет поступивший get-запрос. Если в нем нет параметров или есть параметр all, то метод возвращает все имеющиеся в таблице данные о серверах лицензий, если же передан какой-то параметр (название сайта), то метод возвращает только соответствующие строки из таблицы. Передача параметров в get- запрос осуществляется с помощью выбора одного из пунктов списка на странице. 

**class** **ViewLicenses**(**ListView**):     model = Licenseservers  ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.007.png)

`    `**def** **get\_context\_data**(**self**, \*, object\_list=None, \*\*kwargs): 

`        `context = **super**().get\_context\_data(\*\*kwargs) 

`        `context['sites'] = Licenseservers.objects.values\_list('site', flat=True).distinct() 

`        `context['select\_site'] = **self**.request.GET['select\_menu'] **if** len(**self**.request.GET) **else** 'all' 

`        `**return** context 

`    `**def** **get\_queryset**(**self**): 

`        `req = **self**.request.GET 

`        `**if** len(req) == 0 **or** req['select\_menu'] == 'all': 

`            `**return** Licenseservers.objects.all() 

`        `else: 

`            `**return** Licenseservers.objects.filter(site=req['select\_menu']) 

*Класс ViewLicenses.* 

Там же был описан класс ViewFreeLicenses, связанный с запросом предоставления  свободных  лицензий  с  возможностью  фильтрации  по сайтам и по типу лицензий, с соответствующим приоритетом фильтров.  

Метод  возвращает  данные  для  заполнения  полей  фильтров,  и запрошенные данные: все, либо фильтрованные по указанным параметрам. Получение  данных  осуществляется  с  помощью  сложного  SQL-запроса, описанного в методе get\_request. 

**class** **ViewFreeLicenses**(**ListView**): ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.008.png)

`    `model = Licenseservers 

`    `template\_name = 'freelicenseservers\_list.html' 

`    `**def** **get\_context\_data**(**self**, \*, object\_list=None, \*\*kwargs): 

`        `context = **super**().get\_context\_data(\*\*kwargs) 

`        `context['sites'] = Licenseservers.objects.values\_list('site', flat=True).distinct() 

`        `context['lic\_names'] = dict() 

`        `context['lic\_names']['all'] = Licenseservers.objects.values\_list('name', flat=True).distinct() 

`        `**for** site **in** context['sites']: 

`            `context['lic\_names'][f'{site}'] = Licenseservers.objects.filter(site=site).values\_list('name', flat=True).distinct() 

`        `context['select\_site'] = **self**.request.GET['select\_menu1'] \ 

`            `**if** 'select\_menu1' **in** **self**.request.GET **else** 'all' 

`        `context['select\_lic\_name'] = **self**.request.GET['select\_menu2'] \ 

`            `**if** 'select\_menu2' **in** **self**.request.GET **else** 'all'         **return** context 

`    `**def** **get\_queryset**(**self**): 

`        `req = **self**.request.GET         sql\_request = ''' 

`            `SELECT  

`                `lic.id, 

`                `lic.site, 

`                `lic.name,  ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.009.png)

`                `lic.host,  

`                `lic.total\_auth, 

`                `us1.count\_auth, 

`                `lic.total\_auth - us1.count\_auth as difference\_author,                 lic.total\_cons, 

`                `us2.count\_cons, 

`                `lic.total\_cons - us2.count\_cons as difference\_consumer 

`                `FROM tcusers.licenseservers lic  

`                `left join (select  

`                        `site, 

`                        `licenseServer, 

`                        `licenseLevel, 

`                        `count(\*) as count\_auth 

`                            `from tcusers.users as us where us.status = 0 and us.licenseLevel = 0  

`                            `group by us.licenseLevel, us.site, us.licenseServer) as us1 

`                `on lic.name=us1.licenseServer and lic.site = us1.site  

`                `left join (select  

`                        `site, 

`                        `licenseServer, 

`                        `licenseLevel, 

`                        `count(\*) as count\_cons 

`                            `from tcusers.users as us where us.status = 0 and us.licenseLevel = 1  

`                            `group by us.licenseLevel, us.site, us.licenseServer) as us2 

`                `on lic.name=us2.licenseServer and lic.site = us2.site 

`            `''' 

- если это не первый заход на страницу, то в запросе будут хоть какие то 

аргументы 

`        `**if** len(req) != 0: 

- проверка выбраны ли фильтры по сайту и не all ли это 

`            `site\_filter = 'select\_menu1' **in** **self**.request.GET \ 

`                          `**and** **self**.request.GET['select\_menu1'] != 'all' 

- проверка выбраны ли фильтры по лицензии и не all ли это 

`            `name\_lic\_filter = 'select\_menu2' **in** **self**.request.GET \ 

`                              `**and** **self**.request.GET['select\_menu2'] != 'all' 

- если оба фильтра выбраны all то нет смысла фильтровать данные, 

достаточно выполнить исходный запрос 

`            `**if** site\_filter **or** name\_lic\_filter: 

`                `sql\_request += '\nWHERE ' 

`                `params = [] 

`                `**if** site\_filter: 

`                    `sql\_request += 'lic.site=%s' 

`                    `params.append(**self**.request.GET['select\_menu1'])                     **if** name\_lic\_filter: 

`                        `sql\_request += ' and ' 

`                `**if** name\_lic\_filter: 

`                    `sql\_request += 'lic.name=%s' 

`                    `params.append(**self**.request.GET['select\_menu2']) 

`                `data = Licenseservers.objects.raw(sql\_request, params=params)                 **return** data 

`        `data = Licenseservers.objects.raw(sql\_request)         **return** data 

*Класс ViewFreeLicenses.* 

Фильтрация реализована на js. Функция set\_lic\_list срабатывает по клику на одно из значений выпадающего списка. Работа функции описана в  комментариях  в  приведенном  коде.  Данный  файл  находится  в TUPOLEV\_APP/Licenseservers/static/js/. 

**function** **set\_lic\_list**() { ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.010.png)

`    `// получаем выбранное значение из списка сайтов 

`    `**let** elem1 = document.getElementById('select\_menu1') 

`    `**let** select\_site\_value = elem1.options[elem1.selectedIndex].value 

`    `/\* 

`    `заменяем список, создающийся сервером, на список, обрабатываемый js 

`    `сервер создал выпадающие списки для каждого из выбранных сайтов(см html- шаблон), но все они кроме all изначально скрыты 

`    `при выборе значения сайта мы прячем все списки, а потом показываем только нужный 

`    `атрибут display отвечает за отображение на странице 

`    `атрибут disabled блокирует элемент, чтобы данные из него не обрабатывались     \*/ 

`    `**let** elems = document.getElementsByName('select\_menu2') 

`    `**for** (**let** i = 0; i < elems.length; i++) { 

`        `elems[i].style.display = 'none' 

`        `elems[i].setAttribute("disabled", "disabled"); 

`    `} 

`    `**let** elem2 = document.getElementById( select\_menu2\_for\_${select\_site\_value} )     elem2.style.display = 'block' 

`    `elem2.removeAttribute('disabled') 

} 

*Функция set\_lic\_list, осуществляющая фильтрацию данных.* 

**Работа над приложением Users** 

Необходимо  реализовать  показ  данных,  в  которых  можно  будет видеть соответствие пользователей и групп, к которым они принадлежат. Должна быть предусмотрена фильтрация либо по ФИО пользователя, либо по его логину.  

Для этого был написан класс ViewGroupMembers. Его работа в целом аналогична  работе  предыдущих  описанных  классов,  поэтому  будет приведен только код с комментариями. 

**class** **ViewGroupmembers**(ListView):     model = Users ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.011.png)

`    `**def** **get\_context\_data**(self, \*args, object\_list=None, \*\*kwargs): 

- кладем все нужное в контекстную переменную 

`        `context = super().get\_context\_data(\*\*kwargs) 

`        `context['names'] = Users.objects.values\_list('fullname', 

flat=True).order\_by('fullname').distinct() ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.012.png)

`        `context['tcnames'] = Users.objects.values\_list('tcname', flat=True).order\_by('tcname').distinct() 

`        `context['table\_print'] = len(self.request.GET) != 0 

`        `**return** context 

`    `**def** **get\_queryset**(self): 

`        `req = self.request.GET 

`        `sql\_request = ''' 

`            `SELECT  

`            `us.id, 

`            `us.fullName as fullname, 

`            `us.tcName as tcname, 

`            `us.osName as osname, 

`            `gm.group, 

`            `gm.role, 

`            `us.lastLogin as lastlogin, 

`            `us.licenseServer as licserver,             us.site as site,  

`            `us.status    

`            `FROM tcusers.users us right join tcusers.groupmembers gm on us.tcName = gm.tcName and us.site = gm.site         ''' 

`        `**if** req: 

`            `sql\_request += '\nWHERE ' 

`            `params = [] 

`            `**if** req['fullname\_choice'] != '': 

`                `sql\_request += 'fullname=%s' 

`                `params.append(self.request.GET['fullname\_choice'])                 **if** req['tcname\_choice'] != '': 

`                    `sql\_request += ' and ' 

`            `**if** req['tcname\_choice'] != '': 

`                `sql\_request += 'us.tcName=%s' 

`                `params.append(self.request.GET['tcname\_choice']) 

`            `data = Users.objects.raw(sql\_request, params=params)             **return** data 

`        `data = Users.objects.raw(sql\_request)         **return** data 

*Функция set\_lic\_list, осуществляющая фильтрацию данных.* 

Для полей фильтров реализована система быстрого ввода с помощью стандартных  средств  html,  а  именно  тега  datalist.  Его  работа  такова: например,  пользователь  начинает  вводить  какое-то  ФИО,  и  ему предлагаются варианты, соответствующие уже написанной части строки, полученные  из  БД.  Алгоритм  работы  аналогичен:  если  никаких дополнительных данных при get-запросе не поступило, будут возвращены все данные, которые в последствии отобразятся пользователю. Иначе, будут отображены фильтрованные данные. 

Последний из реализованных классов ViewAddingOrders описывает процесс обработки поступающих запросов о создании и выдаче лицензий. Запрос поступает пользователю либо в текстовом виде, либо в виде exel- таблицы.  В  первом  случае  пользователю  удобнее  было  бы  иметь  на странице  форму,  в  которую  можно  было  бы  быстро  занести  все необходимые данные.  

Если класс получает на вход форму, он обрабатывает данные в ней, валидирует каждую строку, а затем записываю всю информацию в файл и в специальную таблицу логов в базе данных. Если на вход не пришло никаких параметров, отображается пустая таблица-форма с одной строкой. 

**class** **ViewAddingOrders**(TemplateView): ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.013.png)

`    `template\_name = 'adding\_orders.html' 

`    `**def** **get**(self, request, \*args, \*\*kwargs): 

`        `req = self.request.GET 

`        `**if** req:  # эта часть кода сработает, когда мы отправим данные из формы 

- достаем данные 

`            `form\_set = TableFormSet0(req).data 

`            `table = defaultdict(list) 

`            `**for** inf **in** form\_set: 

`                `key = inf.split('-')[1] 

`                `table[key].append(form\_set[inf]) 

- валидируем каждую строку 

`            `**for** key **in** table: 

`                `self.validate\_data(table[key]) 

- запись в файл 

`            `**with** open(FILE\_FOR\_PROC\_REQUESTS, 'w', encoding='ansi') **as** f:                 **for** key **in** table: 

`                    `f.write('|'.join(table[key])) 

`                    `f.write('\n') 

- запись в логи 

`            `new\_info = '' 

`            `**for** key **in** table: 

`                `new\_info += '|'.join(table[key][1:]) + '\n' 

`            `Logs(info=new\_info, 

`                 `sd\_number=table[key][0],                  session\_id=os.getlogin(),                  action='something' 

`                 `).save() 

`            `**return** redirect('menu') 

- эта часть кода сработает чтобы отобразить таблицу в начальном состоянии 

`        `**return** render(request, self.template\_name, self.get\_context\_data()) 

`    `**def** **get\_context\_data**(self, \*\*kwargs): 

`        `context = super().get\_context\_data(\*\*kwargs) 

- помещаем данные из сессии в контекстную переменную 

`        `**if** self.request.session.get('table\_data') != None:             context['form\_set'] = TableFormSet0(initial=self.request.session.get('table\_data'))         ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.014.png)**else**: 

`            `context['form\_set'] = TableFormSet1() 

`        `**try**:  # чистим сессию 

`            `**del** self.request.session['table\_data']         **except** KeyError: 

`            `**pass** 

- вставка полей для подсказок 

`        `context['sites'] = Licenseservers.objects.values\_list('site', flat=True).distinct() 

`        `context['lic\_servers'] = Licenseservers.objects.values\_list('name', flat=True).distinct() 

`        `**return** context 

`    `**def** **validate\_data**(self, data: list):  # функция для валидации строки таблицы         **def** **valid\_req\_name**(dat):  # валидация номера заявки 

`            `**return** False 

`        `**def** **valid\_full\_name**(dat):  # валидация фио             **return** False 

`        `**if** valid\_req\_name(data[1]): 

`            `**raise** ValidationError('текст ошибки', code='код ошибки') 

`        `**if** valid\_full\_name(data[0]): 

`            `**raise** ValidationError('текст ошибки', code='код ошибки') 

*Класс ViewAddingOrders.* 

При  необходимости,  в  нее  можно  добавлять  еще  строки  (процесс реализован  с  помощью  js,  функция  add\_line\_func).  К  тому  же,  в  html добавлена  возможность  предзаполнения  для  полей,  которые  чаще  всего имеют одно и то же значение.  

// добавление новой доп строки в таблицу ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.015.png)

**function** add\_line\_func() { 

`    `let table = document.getElementsByName('table\_line');     let last\_line = **table**[**table**.length - 1]; 

`    `let new\_table\_line =  <tr name="table\_line" id="${Number(last\_line.id) + 1}">                             <td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-req\_num" **class**="form-control" id="request\_number" autocomplete="off"> 

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-full\_name" **class**="form-control" id="full\_name" onchange="os\_name\_auto\_fill(this)" autocomplete="off"> 

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-os\_name" **class**="form-control" id="os\_name" autocomplete="off"> 

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-tc\_name" **class**="form-control" id="tc\_name" 

placeholder="авт." autocomplete="off"> ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.016.png)

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-tc\_pass" **class**="form-control" id="tc\_pass" autocomplete="off" placeholder="авт."> 

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-group" **class**="form-control" id="group" autocomplete="off"> 

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-role" **class**="form-control" id="role" autocomplete="off"> 

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-lic\_server" **class**="form-control" id="lic\_server" autocomplete="off" placeholder="начните ввод..." list="lic\_list"> 

`                            `</td> 

`                            `<td> 

`                                `<**input** **type**="text" name="form- ${Number(last\_line.id) + 1}-site" **class**="form-control" id="site" autocomplete="off" placeholder="начните ввод..." list="site\_list"> 

`                            `</td> 

`                        `</tr> 

`    `last\_line.insertAdjacentHTML("afterend", new\_table\_line); } 

*Функция add\_line\_func, осуществляющая добавление строки в форму-таблицу.* 

Также, некоторые поля, например, логин, можно сгенерировать из ФИО по заданным правилам. Этот функционал реализован на js в функции os\_name\_auto\_fill,  которая  также  вызывает  функцию  toTranslit, переводящую  ФИО  на  кириллице  в  транслит  на  латинице.  Функция os\_name\_auto\_fill срабатывает при заполнении поля ФИО в строке таблицы. Далее  пользователь  сможет  исправить  автоматически  сгенерированные поля, если это требуется. 

**function** **toTranslit**(text) { ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.017.png)

`    `**return** text.replace(/([а-яё])|([\s\_-])|([^a-z\d])/gi, 

`        `**function** (all, ch, space, words, i) { 

`            `**if** (space || words) { 

`                `**return** space ? ' ' : ''; 

`            `} 

`            `**var** code = ch.charCodeAt(0), 

`                `index = code == 1025 || code == 1105 ? 0 : 

`                    `code > 1071 ? code - 1071 : code - 1039, 

`                `t = ['yo', 'a', 'b', 'v', 'g', 'd', 'e', 'zh', 

`                    `'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',                     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',                     'shch', '', 'y', '', 'e', 'yu', 'ya' 

`                `]; 

`            `**return** t[index];         }); ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.018.png)

} 

**function** **os\_name\_auto\_fill**(obj) { 

`    `// получение ФИО из поля ввода 

`    `**let** word = obj.value.split(' ') 

`    `**let** id = obj.parentElement.parentElement.id 

`    `// генерация логина для tc 

`    `**let** new\_word\_tc = '' 

`    `new\_word\_tc += toTranslit(word[1].charAt(0)) 

`    `new\_word\_tc += toTranslit(word[0]) 

`    `**let** field = document.getElementsByName( form-${id}-tc\_name ) 

`    `document.getElementsByName( form-${id}-tc\_name )[0].value = new\_word\_tc      // генерация пароля для tc 

`    `new\_word\_tc += Math.floor(Math.random() \* 999) 

`    `document.getElementsByName( form-${id}-tc\_pass )[0].value = new\_word\_tc  } 

*Функция os\_name\_auto\_fill, осуществляющая автоматическое предзаполнение некоторых полей.* 

Если же данные заявки поступили в виде таблицы, соответствующей строго заданному формату, то добавлена возможность загрузки xls файла. Тогда  срабатывает  функция  upload\_excel,  которая  обрабатывает  файл  и передает  управление  и  обработанные  данные  из  файла  классу ViewAddingOrders, описанному выше.  

Обработка  переданного  производится  с  помощью  функции handle\_upload\_file.  В  ней  из  файла  достаются  данные  и  помещаются  в структуру данных языка Python – словарь. Также эта функция несколько раз вызывает функцию transliterate, которая работает аналогично приведенной ранее функции toTranslite. Разница в работе этих функцию только в том, что одна работает на сервере и обрабатывает данные из файла, а другая на клиенте  и  обрабатывает  данные  формы.  С  помощью  этих  функций  мы получаем одинаковый функционал для пользователя в обоих сценариях: и при заполнении формы вручную, и при помощи загрузки файла, некоторые поля таблицы будут определенным образом предзаполнены. 

**def** **upload\_excel**(request): ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.019.png)

`    `**if** request.method == 'POST' **and** request.FILES['file']: 

- обработка данных полученных из формы 

`        `file = request.FILES['file'] 

`        `table\_data = handle\_uploaded\_file(file) 

- поместим полученные данные из файла в сессию ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.020.png)

`        `request.session['table\_data'] = table\_data 

`        `**return** redirect('adding\_orders')  # будет вызван метод get\_context\_data класса ViewAddingOrders 

`    `**else**: 

- вывод самой формы при первом заходе на страницу 

`        `form = UploadExcelFileForm() 

`    `**return** render(request, 'adding\_excel\_file.html', {'form': form}) 

**def** **handle\_uploaded\_file**(f): 

`    `**try**: 

`        `ex\_file = openpyxl.load\_workbook(f) 

`    `**except**: 

`        `**raise** ValidationError('Invalid format', code='invalid') 

`    `sheet = ex\_file.get\_sheet\_by\_name(ex\_file.get\_sheet\_names()[0])     table\_data = [] 

`    `req\_num = sheet['A2'].value 

`    `**for** row **in** range(2, sheet.max\_row + 1): 

`        `trans\_name = transliterate(sheet[(f"B{row}")].value.split(' ')[1][:1]) \ 

\+ transliterate(sheet[(f"B{row}")].value.split(' ')[0]) 

`        `trans\_name = trans\_name.lower() 

`        `table\_data.append({ 

`            `'req\_num': f'{req\_num}', 

`            `'full\_name': f'{sheet[(f"B{row}")].value}', 

`            `'os\_name': f'{sheet[(f"F{row}")].value}', 

`            `'tc\_name': f'{trans\_name}', 

`            `'tc\_pass': f'{trans\_name + str(randint(111, 999))}',             'group': f'{sheet[(f"D{row}")].value}', 

`            `'role': f'{sheet[(f"E{row}")].value}', 

`            `'lic\_server': f'{sheet[(f"G{row}")].value}', 

`            `'site': f'{sheet[(f"H{row}")].value}', 

`        `}) 

`    `**return** table\_data 

**def** **transliterate**(name): 

- Слоаврь с заменами 

`    `slovar = { 

`        `'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 

`        `'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 

`        `'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 

`        `'ю': 'yu', 'я': 'ya', 

`        `'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',         'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 

`        `'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 

`        `'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 

`        `'Ю': 'Yu', 'Я': 'Ya', 

' ': ' ', 

`    `} 

- Циклически заменяем все буквы в строке 

`    `**for** key **in** slovar: 

`        `name = name.replace(key, slovar[key])     ![](Aspose.Words.e8e915ba-eed7-419a-9d2c-6ad7b63a2444.021.png)**return** name 

*Функции upload\_excel и handle\_upload\_file, осуществляющие загрузку и обработку данных из excel файла.* 

Класс  ViewAddingOrders  выводит  всё  ту  же  форму,  заполненную извлеченными  данными.  Пользователь  может  проверить,  что  все  было обработано  верно,  отредактировать  что-то  при  необходимости,  а  затем отправить данные формы далее. При этом будет создана запись в таблице логов, которая будет содержать всю необходимую информацию о заявке.  

**Заключение** 

В  процессе  прохождения  практики  был  получен  опыт  работы  с реальными  задачами  под  руководством  опытных  наставников,  удалось принципы и методы работы и проектирования веб-приложений.  

За время практики было разработано веб-приложение, состоящее из 1034  строк  на  Python  и  125  строк  на  JavaScript,  реализующее  удобный интерфейс для удобной работы с существующей базой данных.  В процессе удалось  закрепить  и  углубить  знания  веб-фреймворка  Django, познакомиться  с  языком  JavaScript.  Получить  практический  опыт разработки коммерческого приложения и его архитектуры по требованиям заказчика, в роли которого выступал руководитель, также контролирующий и управляющий процессом разработки. 
PAGE21 
