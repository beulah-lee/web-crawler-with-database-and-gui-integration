#include "utils.h"
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>
#include <cstdio> 
using namespace std;

string exec(const char* cmd) {
    array<char, 128> buffer;
    string result;
    unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(cmd, "r"), _pclose);
    if (!pipe) {
        throw runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

string fetch_content(const string& url) {
    string cmd = "python html_parser.py " + url;
    return exec(cmd.c_str());
}