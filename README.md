# Literature_Data_Visualization_Analysis

1.	Literature data was obtained using the crawler at "https://github.com/tomleung1996/wos_crawler".

2.	Use Navicat to open the "result.db" file obtained by crawling.

3.	Export the table "wos_keyword" as a csv file, use the program "key_process.py" to process the exported file, get the processed "keyword_final.csv" file, and re-import the "keyword_final.csv" file into the Navicat database.

4.	For the "keyword_final.csv" file, use the program "all_keyword_fre.py" to obtain the "total_ word_frequency.csv" file.

5.	Associate the tables "keyword_final" and "wos_document" in Navicat, create a new table "time" to get the year and month of each keyword, and export the "time" table as "time.csv". (SQL statement: create table time as select keyword_final.document_unique_id, keyword_final.keyword, wos_document.pub_year, wos_document.pub_month_day  from   keyword_final join wos_document on keyword_final.document_unique_id = wos_document.unique_id)


6.	Create a new "heatmap.csv" file, select the x keywords with the highest frequency in "total_ word_frequency.csv", set them as the first column of "heatmap.csv", and set the selected year as the first column of "heatmap.csv" one line.

![5](https://user-images.githubusercontent.com/103013914/162569589-0b483c3b-a0c1-45be-9813-a704961d2c4b.png)

7.	Run the "year_frequent.py" program to process the "time.csv" and "heatmap.csv" files to get the "heatmaps.csv" file.

8.	Run the "Heat_Visualization.py" program to process the "heatmaps.csv" file to get the heat figure.

![1](https://user-images.githubusercontent.com/103013914/162569612-14199374-8a82-4f5c-9c7e-45b73f040f4b.png)

9.	Create a new "co-data.csv" file and copy the x keywords with the highest frequency in "total_ word_frequency.csv" and the word frequency to the "co-data.csv" table.

![6](https://user-images.githubusercontent.com/103013914/162569616-d9f8e71d-a4d3-4d89-abc8-d90045829e75.png)

10.	Run the "Co_Occ_Matrix.py" program to process the "keyword_final.csv" file and get the "Co_score.csv" file.

11.	Run the "Co_Occurence.py" program to process the "Co_score.csv" and "co-data.csv" files to obtain the co-occurrence figure.

![2](https://user-images.githubusercontent.com/103013914/162569628-f6962e9d-9e1b-4504-9978-df3eb9c8e2ba.png)

12.	Run the following SQL code in Navicat to get a series of tables. (SQL statement: create table aaa as select corresponding_author.document_unique_id, keyword_final.keyword, corresponding_author.author_id from corresponding_author join keyword_final on corresponding_author.document_unique_id = keyword_final.document_unique_id create table address as select aaa.document_unique_id, aaa.keyword, aaa.author_id, wos_affiliation.address from aaa join wos_affiliation on aaa.author_id = wos_affiliation.author_id create table country as select corresponding_author.document_unique_id, wos_affiliation.address from corresponding_author LEFT OUTER join wos_affiliation on corresponding_author.author_id = wos_affiliation.author_id create table address_time as select country.document_unique_id, wos_document.pub_year, country.address from country join wos_document on country.document_unique_id = wos_document.unique_id)

13.	Export the table "address_time" as "address_time.csv" file.

14.	Run the "address_time_process.py" program to process the "address_time.csv" file to get the " number_of_articles_by_country_per_year.csv" file.

15.	Open the "nation_figure.py" program. On line 44 of the code, sort by the countries in the " number_of_articles_by_country_per_year.csv" file and re-enter the value of the "attr" country name attribute by the standardized name of the country in the nameMap on line 6 of the code. After re-entering the "attr" attribute, run the program, get "nation.html", and open it to get a map of the number of articles in the country.

![3](https://user-images.githubusercontent.com/103013914/162569641-b8319d3b-8fec-48c0-8627-8a8f3a9b5bf0.png)

16.	Create a new "number_of_country_articles.csv" file, select the annual data of the top 6 countries with the largest number of published articles according to the data in the " number_of_articles_by_country_per_year.csv", and merge the annual data of the remaining countries into The other lines form the " number_of_country_articles.csv" file. The last line of the " number_of_country_articles.csv" file counts the total number of all countries in each year, and the last column counts the total number of countries for all years.

![7](https://user-images.githubusercontent.com/103013914/162569650-b4e65257-19de-4283-b918-60bc379f2d63.png)

17.	Open the "nation_time.py" program. On line 11 of the code, re-enter the "country_data_count" attribute according to the data in the "number_of_country_articles.csv.csv" file. Run the "nation_time.py" program to get a graph of the percentage of articles published by each country each year.
![4](https://user-images.githubusercontent.com/103013914/162569656-e3422f98-5557-4bd1-9b0c-d27b90bb3592.png)
