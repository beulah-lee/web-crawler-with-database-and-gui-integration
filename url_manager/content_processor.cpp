#include "utils.h"
#include <regex>
using namespace std;

bool is_content_valid(const string& content, const vector<string>& keywords) {
    for (const auto& keyword : keywords) {
        regex pattern("\\b" + keyword + "\\b", regex_constants::icase);
        if (regex_search(content, pattern)) {
            return true;
        }
    }
    return false;
}