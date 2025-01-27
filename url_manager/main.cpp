#include "url_manager.h"
#include "utils.h"
#include <iostream>
#include "C:/Program Files/MySQL/mysql-connector-c++-9.2.0-winx64/include/jdbc/mysql_driver.h"
#include "C:/Program Files/MySQL/mysql-connector-c++-9.2.0-winx64/include/jdbc/mysql_connection.h"
#include "C:/Program Files/MySQL/mysql-connector-c++-9.2.0-winx64/include/jdbc/cppconn/statement.h"
#include "C:/Program Files/MySQL/mysql-connector-c++-9.2.0-winx64/include/jdbc/cppconn//resultset.h"
#include <vector>
#include <string>
#include <thread>
using namespace std;

vector<string> fetch_urls_from_db() {
    vector<string> urls;
    try {
        sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();
        unique_ptr<sql::Connection> conn(driver->connect("tcp://127.0.0.1:3306", "root", "mysql"));
        conn->setSchema("web_crawler");

        unique_ptr<sql::Statement> stmt(conn->createStatement());
        unique_ptr<sql::ResultSet> res(stmt->executeQuery("SELECT url FROM urls"));

        while (res->next()) {
            urls.push_back(res->getString("url"));
        }
    } catch (sql::SQLException& e) {
        cerr << "SQLException: " << e.what() << endl;
        cerr << "SQLState: " << e.getSQLState() << endl;
        cerr << "Error Code: " << e.getErrorCode() << endl;
    }
    return urls;
}

int main() {
    vector<string> urls = fetch_urls_from_db();

    string input;
    getline(cin, input);

    vector<string> keywords;
    size_t pos = 0;
    while ((pos = input.find(',')) != string::npos) {
        keywords.push_back(input.substr(0, pos));
        input.erase(0, pos + 1);
    }
    keywords.push_back(input);

    process_urls_multithreaded(urls, keywords);

    return 0;
}