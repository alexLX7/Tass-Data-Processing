# Tass-Data-Processing

Processing the data from "Tass" (Russian News Agency). The links: https://tass.ru/ and https://tass.com/.

This repo will help You to understand how to extract, load, transform, analyze and visualize information from the "Tass".

Оригинальные разъяснения на русском языке представлены в конце README.md (The original explanations in Russian are also included in this README.md)


# Results

Tass-Data-Processing visual results can be opened right in a browser

<h4>

```diff
! [NOTICE] 

Unfortunately, it may take some time to load these heavy (35Mb) pages. 
These files contain brief info about each article (about 70.000 articles).
So it may take a while to react to Your actions (e.g. zoom in; show each cell info; etc.)

```

</h4>

Colorization by number of articles per day:
https://alexlx7.github.io/Tass-Data-Processing/output_images/full_info.html

COVID-related visualization:
https://alexlx7.github.io/Tass-Data-Processing/output_images/final_info.html

![Screenshot](/output_images/demo_img_2.png)


# Explanation

### Colorization by number of articles per day:

![Screenshot](/output_images/demo_img_0.png)

https://alexlx7.github.io/Tass-Data-Processing/output_images/full_info.html

There is a selection of days: from the beginning of October 2019 to mid-April 2020.
Each and every day consists of a different number of articles.
Meanwhile, each cell contains a piece of information about one article.
Each day has its own color, depending on number of articles per day:

As You can see from 'full_info.html': the days highlighted in blue are weekends and holidays, on such days there is much less news.

![](/output_images/gif_holidays.gif)


### COVID-related visualization:

There is the same selection of days. But the colors correspond to the field called 'covid_related'.
If the cell is indeed covid_related, the cell is highlighted in red:

![Screenshot](/output_images/demo_img_3.png)

https://alexlx7.github.io/Tass-Data-Processing/output_images/final_info.html

The 'final_info.html' file shows that COVID has only been gaining attention in Russia since mid-January 2020:

![](/output_images/gif_zoom_in_january.gif)

By mid-March, COVID-related news exceeded half of all articles per day:

![](/output_images/gif_zoom_in_march.gif)


### Additional info:

The most common words from articles:

![Screenshot](output_images/most_common_words.png)

It is possible to make a Wordcloud by these common words. The size of each word corresponds to its frequency:

![Screenshot](output_images/wordcloud_0.png)


For more info check out 'analyzing.ipynb'.


# What is this?

This is a personal project to practice in data processing.

The results of this research provide a visual answer about mentions in TASS about COVID-19 in Russia.

This repo contains downloaded data, supplemented by primary processing with basic analysis of article texts for the time: from the beginning of October 2019 to mid-April 2020.


# What are the parts of this data-processing repo?

### Web scraping:

Extracting.py contains ways to get info from the 'https://tass.ru/' (e.g. 'article_text', 'title', 'category', 'href') by the start date and the end date (e.g. ['2020-04-21 00:00:00', '2020-04-20 00:00:00']).
That parsed information is stored in '/data/' folder as .pickle file (per each month).

### ETL:

Cleaning.py contains ways to extract, transform and load an important data to the dataframe.

### Analyzing and visualizing:

Analyzing.ipynb contains ways to show some basic info about the dataframe.
The information is stored in '/output_images/' folder.



# What is the reason for this research?

Initially (April 2020), I wanted to try a new at that time Jupyter Notebook in VS Code.

So, I chose the direction of data mining:

- Mentions in TASS about COVID-19

By the beginning of May 2020, many countries were under a lockdown, so, one way or another, everyone was aware of COVID-19. So, I decided to check out the old articles to see how it all started.


# Результаты продублированы на русском (explanations in Russian)

Результатом проекта являются файлы final_info.html и full_info.html из папки output_images.

<h4>

```diff
! [ПРЕДУПРЕЖДЕНИЕ] 

К сожалению, загрузка представленных тяжелых (35 МБ) страниц может занять некоторое время.
Страницы содержат краткую информацию о каждой статье (всего около 70 тысяч статей).
Может потребоваться время, чтобы отреагировать на приближение области и отображение информации о статье.

```

</h4>

Отображение каждого дня определенным цветом (в зависимости от количества статей за день):
https://alexlx7.github.io/Tass-Data-Processing/output_images/full_info.html

Визуализация данных, связанных с COVID:
https://alexlx7.github.io/Tass-Data-Processing/output_images/final_info.html


# Объяснения


### Цветное отображение (в зависимости от количества статей за день):

![Screenshot](/output_images/demo_img_0.png)

https://alexlx7.github.io/Tass-Data-Processing/output_images/full_info.html

Выше представлены выборки дней: с начала октября 2019 года до середины апреля 2020 года.
Каждый день состоит из некоторого количества статей.
Каждая ячейка содержит информацию об одной статье. 
Каждый день подсвечен в зависимости от количества статей за этот день.

Как видно из full_info.html: выделенные темно-синим цветом дни - это выходные и праздники, в такие дни новостей заметно меньше.

![](/output_images/gif_holidays.gif)



### Визуализация данных, связанных с COVID:

На другом отображении представлена та же выборка. Красным подсвечены ячейки, в которых упоминается COVID.

![Screenshot](/output_images/demo_img_3.png)

https://alexlx7.github.io/Tass-Data-Processing/output_images/final_info.html

Отображение final_info.html наглядно демонстрирует, что общее внимание в новостях COVID привлек к себе только с середины января 2020 года.

![](/output_images/gif_zoom_in_january.gif)

А в середине марта связанных с COVID новостей было больше половины от всех новостей за день.

![](/output_images/gif_zoom_in_march.gif)



# Дополнительно

Самые распространенные слова из статей:

![Screenshot](output_images/most_common_words.png)

Кроме этого, представлены: график самых частых слов и облако из этих слов. Размер слова зависит от частоты повторения в тексте.

![Screenshot](output_images/wordcloud_0.png)


Для более подробной информации можно скачать/посмотреть 'analyzing.ipynb'.



## Rate this project! :star:
### If you liked this repo, give it a star. Thanks!

