# Literature_Data_Visualization_Analysis

1.	Literature data was obtained using the crawler at "https://github.com/tomleung1996/wos_crawler".
2.	Use Navicat to open the "result.db" file obtained by crawling.
3.	Export the table "wos_keyword" as a csv file, use the program "key_process.py" to process the exported file, get the processed "keyword_final.csv" file, and re-import the "keyword_final.csv" file into the Navicat database.
4.	For the "keyword_final.csv" file, use the program "all_keyword_fre.py" to obtain the "total_ word_frequency.csv" file.
5.	Associate the tables "keyword_final" and "wos_document" in Navicat, create a new table "time" to get the year and month of each keyword, and export the "time" table as "time.csv".
SQL statement: create table time as select keyword_final.document_unique_id, keyword_final.keyword, wos_document.pub_year, wos_document.pub_month_day from keyword_final join wos_document on keyword_final.document_unique_id = wos_document.unique_id
6.	Create a new "heatmap.csv" file, select the x keywords with the highest frequency in "total_ word_frequency.csv", set them as the first column of "heatmap.csv", and set the selected year as the first column of "heatmap.csv" one line.
![123](https://user-images.githubusercontent.com/103013914/162561094-937546ca-cf30-4c72-b1ec-e573b6066e56.png)
