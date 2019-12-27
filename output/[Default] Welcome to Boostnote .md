  # Welcome to Boostnote :)
  This is a markdown note.
  http://niisi.hatenablog.jp/entry/2016/01/20/020000
  
  Click to edit this note.
  
  - List
    - subitem1
    - subitem2
   
   1. numlist1
   1. numlist2
   1. numlist3
   
  *bold*
  **2bold**
  
  Space  
  Between
  
  Draw a line
  ***
  - - -
  
  
  
  ```
  <html>
  <body>
  <h1 id='hello'>Hello World</h1>
  </body>
  </html>
  ```
  
  ```
  Create table from CSV
  import csv
  import sqlite3
  import glob
  import os
  
  def do_directory(dirname, db):
    for filename in glob.glob(os.path.join(dirname, '*.csv')):
      do_file(filename, db)
  ```
  
  Draw Table
  |header1|header2|header3|
  |:-|:-|:-|
  |Data1|Data2|Data3|
  
  
  
