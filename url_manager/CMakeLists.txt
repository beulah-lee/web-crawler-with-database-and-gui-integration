cmake_minimum_required(VERSION 3.10)
project(WebCrawler)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories("C:/Program Files/MySQL/mysql-connector-c++-9.2.0-winx64/include/jdbc")
link_directories("C:/Program Files/MySQL/mysql-connector-c++-9.2.0-winx64/lib64")

add_executable(url_manager
    url_manager.cpp
    utils.cpp
    content_processor.cpp
    main.cpp
)

target_link_libraries(url_manager pthread mysqlcppconn)